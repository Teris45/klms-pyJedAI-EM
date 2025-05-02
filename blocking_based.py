from pyjedai.datamodel import Data
from pyjedai.workflow import BlockingBasedWorkFlow
from pyjedai.block_building import *
from pyjedai.block_cleaning import *
from pyjedai.clustering import *
from pyjedai.matching import * 
from pyjedai.comparison_cleaning import *
from pyjedai_utils import *

import json

def get_BlockingBasedWorkflow(data: Data, parameters: dict) -> BlockingBasedWorkFlow:

    required_keys = [
            "block_building",
            "entity_matching",
    ]

    optional_keys = [
        "block_cleaning",
        "comparison_cleaning",
        "clustering"
        ]
    
    print(f"""
Parameters given as : {json.dumps(parameters, indent=4)}
The parameters will be checked and processed to input them correctly to pyJedAI BlockingBased Workflow.\nIf you give no input parameters, best workflow will be used (read the docs).
If you skip one or both of the required parameters: {required_keys}, the defaults will be used.
Read the docs and see how each function is called.
""")
    
    
    new_parameters = {}

    for key in optional_keys:
        if key in parameters:
            if parameters[key]:
                if key == 'block_cleaning':
                    block_cleaning_list = list()
                    if isinstance(parameters[key], list):
                        for filtering_dict in parameters[key]:
                            if (new_filtering_dict := get_new_dict(workflow_step=key, old_dict=filtering_dict)):
                                block_cleaning_list.append(new_filtering_dict)
                    if isinstance(parameters[key], dict):
                        if (new_filtering_dict := get_new_dict(workflow_step=key, old_dict=parameters[key])):
                            block_cleaning_list.append(new_filtering_dict)
                    if block_cleaning_list:
                        new_parameters[key] = keep_first_unique_method(block_cleaning_list)
                else: 
                    if (new_dict := get_new_dict(workflow_step=key, old_dict=parameters[key])): 
                        new_parameters[key] = new_dict
    

    for key in required_keys:
        if key in parameters:
            if parameters[key]:
                if (new_dict := get_new_dict(workflow_step=key, old_dict=parameters[key])):
                    new_parameters[key] = new_dict

    if not new_parameters:
        w = BlockingBasedWorkFlow()
        if data.is_dirty_er:
            w.best_blocking_workflow_der()
        else: 
            w.best_blocking_workflow_ccer()
        
        new_parameters = {
            "block_building": w.block_building,
            "block_cleaning" : w.block_cleaning,
            "comparison_cleaning": w.comparison_cleaning,
            "entity_matching": w.entity_matching,
            "clustering": w.clustering
        }
        
        if 'name' in parameters:
            w.name = parameters['name']
            new_parameters['name'] = w.name
    
        print(f""" 
After processing input...
The workflow-parameters are : {json.dumps(dict_to_str(new_parameters), indent=4)} 
        """)

        return w

    if 'block_building' not in new_parameters:
        new_parameters["block_building"] = dict(method=StandardBlocking)
    if 'entity_matching'not in new_parameters:
        new_parameters["entity_matching"] = dict(method=EntityMatching,
                                                params=dict(metric='cosine', 
                                                similarity_threshold=0.55))
                    
    if 'name' in parameters: 
        new_parameters['name'] = parameters['name']
    
    print(f""" 
After processing input...
The workflow-parameters are : {json.dumps(dict_to_str(new_parameters), indent=4)} 
          """)
    
    return BlockingBasedWorkFlow(**new_parameters)
