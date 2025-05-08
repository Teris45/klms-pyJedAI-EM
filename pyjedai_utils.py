from pyjedai.datamodel import Data
import pandas as pd
from pyjedai.workflow import  EmbeddingsNNWorkFlow, JoinWorkflow
from pyjedai.vector_based_blocking import EmbeddingsNNBlockBuilding
from pyjedai.block_building import *
from pyjedai.block_cleaning import *
from pyjedai.clustering import *
from pyjedai.matching import * 
from pyjedai.comparison_cleaning import *
import inspect
from global_dict import *
import json
from utils.mclient import MinioClient
import copy

required_keys = {
    'ground_truth': ['separator'],
    'dataset_1': ['separator', 'id_column_name'],
    'dataset_2': ['separator', 'id_column_name']
    
}


def dict_to_str(old_dict: dict): 
    
    new_dict = {} 
    for key in old_dict: 
        new_dict[key] = copy.deepcopy(old_dict[key])
        if isinstance(new_dict[key], list): 
            for item in new_dict[key]: 
                item['method'] = item['method'].__name__
        else:
            if new_dict[key]['method']:
                new_dict[key]['method'] = new_dict[key]['method'].__name__
                
    for key in new_dict:
        print(key)
        if 'exec_params' in new_dict[key]: 
            if not 'params' in new_dict[key]:
                new_dict[key]['params'] = new_dict[key]['exec_params']
            else:
                for exec_key in new_dict[key]['exec_params']: 
                    new_dict[key]['params'][exec_key] = new_dict[key]['exec_params'][exec_key]
    
            del new_dict[key]['exec_params'] 
    
    return new_dict
    
    
    
    

def get_parameters_of_class(method) -> None:
    # Get the signature of __init__
    init_signature = inspect.signature(method)

    # Get the parameters
    parameters = init_signature.parameters

    # Extract parameter names (excluding 'self')
    param_names = [name for name in parameters if name != 'self']
    return param_names

def check_dataset(dataset: dict, dataset_name: str) -> None:
    # Get the appropriate set of required keys
    keys_required = required_keys[dataset_name]

    # Find missing keys using set operations
    missing_keys = set(keys_required) - set(dataset.keys())

    if missing_keys:
        raise Exception(f"On {dataset_name} {missing_keys} was not given")

# Check if input was correctly provided
def load_input(mc: MinioClient, input: dict, parameters: dict) -> Data:
    if 'dataset_1' not in input:
        raise Exception("No dataset_1 was given")
    
    
    data_dict = { 
            "id_column_name_1": None,
            "attributes_1" : None,
            "dataset_name_1" : None,
            "dataset_2" : None,
            "id_column_name_2" : None,
            "attributes_2" : None,
            "dataset_name_2" : None,
            "ground_truth" : None,
            "skip_ground_truth_processing" : True 
            }
    
    
    for dataset in ['dataset_1', 'dataset_2', 'ground_truth']:
        if dataset in input and dataset not in parameters:
            raise Exception(f"Must provide required_keys in parameters for {dataset} : {required_keys[dataset]}")
        elif dataset in input and dataset in parameters: 
            
            check_dataset(parameters[dataset], dataset)
            

            mc.get_object(s3_path=input[dataset][0], local_path=f".local/{dataset}.csv")
            
            
            df = pd.read_csv(f".local/{dataset}.csv", sep=parameters[dataset]["separator"], engine='python', na_filter=False)
            data_dict[dataset] = df.copy()
            
            if dataset != 'ground_truth': 
                for key in parameters[dataset]:
                    index = dataset.split('_', 1)[1]
                    data_dict_key = f'{key}_{index}'
                    if data_dict_key in data_dict and parameters[dataset][key]:
                        if key == 'attributes' and not isinstance(parameters[dataset]['attributes'],list): 
                            data_dict[data_dict_key] = list(parameters[dataset][key])
                        else: 
                            data_dict[data_dict_key] = parameters[dataset][key]
            elif dataset == 'ground_truth':
                data_dict['skip_ground_truth_processing'] = False
    
    # gt = pd.read_csv('data/ccer/D2/gt.csv', sep='|')
    # data_dict['ground_truth'] = gt
    # data_dict['skip_ground_truth_processing'] = False
    

    if isinstance(data_dict['ground_truth'], pd.DataFrame):
        columns = data_dict['ground_truth'].columns
        if isinstance(data_dict['dataset_2'], pd.DataFrame):
            data_dict['ground_truth'] = data_dict['ground_truth'][
                data_dict['ground_truth'][columns[0]].isin(data_dict['dataset_1'][data_dict['id_column_name_1']])
                & 
                data_dict['ground_truth'][columns[1]].isin(data_dict['dataset_2'][data_dict['id_column_name_2']])
            ]
        else: 
            data_dict['ground_truth'] = data_dict['ground_truth'][
                data_dict['ground_truth'][columns[0]].isin(data_dict['dataset_1'][data_dict['id_column_name_1']])
                & 
                data_dict['ground_truth'][columns[1]].isin(data_dict['dataset_1'][data_dict['id_column_name_1']])
            ]

    return Data(**data_dict)                   
                        



def get_new_dict(workflow_step: str, old_dict: dict) -> dict:
    if 'method' not in old_dict or old_dict['method'] not in methods_dict[workflow_step]:
        return None
    
    
    new_dict = { "method": methods_mapping[old_dict["method"]] }
    if 'params' in old_dict:
        # new_params = {}
        old_params = get_parameters_of_class(new_dict['method'].__init__) 
    
        new_params = {
                        key : old_dict['params'][key]
                        for key in old_params if key in old_dict['params']
                    }

        # for key in old_params:
        #     if key in old_dict['params']: 
        #         new_params[key] = old_dict['params'][key]
        if new_params:
            new_dict['params'] = new_params
    
    if workflow_step == 'clustering':
        if 'params' in old_dict and 'similarity_threshold' in old_dict['params']:
            old_dict['similarity_threshold'] = old_dict['params']['similarity_threshold']
        if 'similarity_threshold' in old_dict: 
            new_dict['exec_params'] = dict(similarity_threshold=old_dict['similarity_threshold'])
            return new_dict

    for key in old_dict:
        if key not in ['method', 'params'] and old_dict[key]:    
            new_dict[key] = old_dict[key]

    return new_dict


def keep_first_unique_method(methods_list: list) -> list:
    seen_methods = set()
    unique_data = []
    i = 0 
    for item in methods_list:
        method = item['method']
        if method not in seen_methods:
            seen_methods.add(method)
            unique_data.append(item)
            i += 1
        if i==2: 
            break

    return unique_data


def load_embeddings(mc: MinioClient, input: dict, parameters: dict) -> dict:


    
    if "embeddings_dataset_1" in input:
        mc.get_object(s3_path=input["embeddings_dataset_1"][0], local_path=f".local/emb_1.npy")
        parameters["load_path_if_exist"] = True
        parameters['load_path_d1'] = '.local/emb_1.npy'
    

    if "embeddings_dataset_2" in input:
        mc.get_object(s3_path=input["embeddings_dataset_2"][0], local_path=f".local/emb_2.npy")
        parameters["load_path_if_exist"] = True
        parameters['load_path_d2'] = '.local/emb_2.npy'
        


    return parameters



def get_EmbeddingsNNWorkFlow(data: Data, parameters: dict) -> EmbeddingsNNWorkFlow:

    print(f"""
Parameters given as : {json.dumps(parameters, indent=4)}
The parameters will be checked and processed to input them correctly to pyJedAI Embeddings-NN Workflow.
Read the docs and see how each function is called.
""")


    workflow_parameters = {'name' : parameters.get('name')}
    if not workflow_parameters['name']:
        del workflow_parameters['name']
        
    block_building_parameters = parameters['block_building']
    block_building_dict = {'method': EmbeddingsNNBlockBuilding}

    if 'params' in block_building_parameters: 
        for key in block_building_parameters['params']:
            block_building_parameters[key] = block_building_parameters['params'][key]
        del block_building_parameters['params']
    # __init__ 
    block_building_dict['params'] = {'vectorizer': block_building_parameters['vectorizer'] if 'vectorizer' in block_building_parameters else 'smpnet'}
        
    # build_blocks
    block_building_dict['exec_params'] = {
        "vector_size" : 300,
        "num_of_clusters": 5,
        "top_k": 30,
        "max_word_embeddings_size": 256,
        "input_cleaned_blocks": None,
        "similarity_distance": 'cosine',
        "custom_pretrained_model": None,
    }


    for key in block_building_dict['exec_params']:
        if key in block_building_parameters: 
            block_building_dict['exec_params'][key] = block_building_parameters[key]

    for key in ["load_embeddings_if_exist", "load_path_d1", "load_path_d2"] :
        if key in block_building_parameters:
            block_building_dict['exec_params'][key] = block_building_parameters[key]

    keys = block_building_dict['exec_params'].copy()

    for key in keys:
        if block_building_dict['exec_params'][key] == None:
            del block_building_dict['exec_params'][key]

    print(block_building_parameters)
    if "attributes_1" in block_building_parameters:
        block_building_dict['attributes_1'] = block_building_parameters['attributes_1']
    if "attributes_2" in block_building_parameters:
        block_building_dict['attributes_2'] = block_building_parameters['attributes_2']
    
        
    workflow_parameters['block_building'] = block_building_dict
    clustering_parameters = parameters['clustering']

    if (new_dict := get_new_dict(workflow_step='clustering', old_dict=clustering_parameters)): 
        workflow_parameters['clustering'] = new_dict

    print(f""" 
After processing input...
The workflow-parameters are : {json.dumps(dict_to_str(workflow_parameters), indent=4)} 
    """)


    return EmbeddingsNNWorkFlow(**workflow_parameters)



def get_JoinWorkflow(data: Data, parameters: dict) -> JoinWorkflow:
    print(f"""
Parameters given as : {json.dumps(parameters, indent=4)}
The parameters will be checked and processed to input them correctly to pyJedAI Embeddings-NN Workflow.
Read the docs and see how each function is called.
""")


    workflow_parameters = {'name' : parameters.get('name')}
    if not workflow_parameters['name']:
        del workflow_parameters['name']
        
    join_parameters = get_new_dict('join', parameters['join'])
    
    if 'reverse_order' in parameters['join']['params']:
        join_parameters['exec_params'] = {
            "reverse_order" : parameters['join']['params']['reverse_order']
        }
    
    workflow_parameters['join'] = join_parameters
    clustering_parameters = parameters['clustering']
    if (new_dict := get_new_dict(workflow_step='clustering', old_dict=clustering_parameters)): 
        workflow_parameters['clustering'] = new_dict

    print(f""" 
After processing input...
The workflow-parameters are : {json.dumps(dict_to_str(workflow_parameters), indent=4)} 
    """)

    return JoinWorkflow(**workflow_parameters)




