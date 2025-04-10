from pyjedai.datamodel import Data
import pandas as pd
from pyjedai.workflow import  EmbeddingsNNWorkFlow
from pyjedai.block_building import *
from pyjedai.block_cleaning import *
from pyjedai.clustering import *
from pyjedai.matching import * 
from pyjedai.comparison_cleaning import *
import inspect
from global_dict import *


def get_parameters_of_class(method) -> None:
    # Get the signature of __init__
    init_signature = inspect.signature(method)

    # Get the parameters
    parameters = init_signature.parameters

    # Extract parameter names (excluding 'self')
    param_names = [name for name in parameters if name != 'self']
    return param_names



def check_dataset(dataset: dict, dataset_name: str) -> None:
    required_keys = {
        'ground_truth': ['csv_path', 'separator'],
        'other': ['csv_path', 'separator', 'id_column']
    }

    # Get the appropriate set of required keys
    keys_required = required_keys.get(dataset_name.lower(), required_keys['other'])

    # Find missing keys using set operations
    missing_keys = set(keys_required) - set(dataset.keys())

    if missing_keys:
        raise Exception(f"On {dataset_name} {missing_keys} was not given")

# Check if input was correctly provided
def check_input(input: dict) -> None:
    if 'dataset_1' not in input:
        raise Exception("No dataset_1 was given")
    
    for dataset in ['dataset_1', 'dataset_2', 'ground_truth']:
        if dataset in input:
            check_dataset(input[dataset], dataset)
        

def load_input(input: dict) -> Data:
    check_input(input)

    dataset_1 = input['dataset_1']
    d1 = pd.read_csv(dataset_1['csv_path'], 
                    sep=dataset_1['separator'],
                    engine='python', na_filter=False)
    
    if 'attributes' not in dataset_1:
        dataset_1['attributes'] = None
        
    if 'name' not in dataset_1:
        dataset_1['name'] = None
    
    if 'ground_truth' in input: 
        ground_truth = input['ground_truth']
        gt = pd.read_csv(ground_truth['csv_path'], 
                sep=ground_truth['separator'],
                engine='python', na_filter=False)
        skip_ground_truth_processing = False
    else:
        gt = None
        skip_ground_truth_processing = True
    
    if 'dataset_2' in input:
        dataset_2 = input['dataset_2']
        d2 = pd.read_csv(dataset_2['csv_path'], 
                    sep=dataset_2['separator'],
                    engine='python', na_filter=False)

        if 'attributes' not in dataset_2:
            dataset_2['attributes'] = None
            
        if 'name' not in dataset_2:
            dataset_2['name'] = None
    else: 
        d2 = None
        dataset_2 = {
            'attributes': None,
            'name': None,
            'id_column': None
        }        

    return Data(dataset_1=d1,
            id_column_name_1=dataset_1['id_column'],
            attributes_1=dataset_1['attributes'],
            dataset_name_1=dataset_1['name'],
            dataset_2=d2,
            id_column_name_2=dataset_2['id_column'],
            attributes_2=dataset_2['attributes'],
            dataset_name_2=dataset_2['name'],
            ground_truth=gt,
            skip_ground_truth_processing=skip_ground_truth_processing
        )


def get_new_dict(workflow_step: str, old_dict: dict) -> dict:
    new_dict = {}
    if 'method' not in old_dict:
        return None
    else: 
        if old_dict['method'] not in methods_dict[workflow_step]:
            return None
    
    new_dict['method'] = methods_mapping[old_dict["method"]]
    if 'params' in old_dict:
        new_params = {}
        old_params = get_parameters_of_class(new_dict['method'].__init__) 
        for key in old_params:
            if key in old_dict['params']: 
                new_params[key] = old_dict['params'][key]
        if new_params:
            new_dict['params'] = new_params
    
    if workflow_step == 'clustering':
        if 'similarity_threshold' in old_dict: 
            new_dict['exec_params'] = dict(similarity_threshold=old_dict['similarity_threshold'])
            return new_dict
        


    for key in old_dict:
        if key in ['method','params']: 
            continue
       
        if old_dict[key]:    
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


    

def get_EmbeddingsNNWorkFlow(data: Data, parameters: dict) -> EmbeddingsNNWorkFlow:
    new_parameters = {'data': data}
    
    parameters_keys = [
        "block_building",
        "clustering"
    ]


    return EmbeddingsNNWorkFlow(**new_parameters)








