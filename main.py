import json
import sys
import traceback
from utils.mclient import MinioClient
from pyjedai_utils import *
import time 
from pyjedai_utils import *
import subprocess


    

def run(json_input):
    try:

        
        ################################## MINIO INIT #################################
        minio_id = json_input['minio']['id']
        minio_key = json_input['minio']['key']
        minio_skey = json_input['minio']['skey']
        minio_endpoint = json_input['minio']['endpoint_url']

        if 'https://' in minio_endpoint:
            minio_endpoint = minio_endpoint.replace('https://', '')
        
        mc = MinioClient(access_key=minio_id, secret_key= minio_key, session_token=minio_skey, endpoint=minio_endpoint)

        # It is strongly suggested to use the get_object and put_object methods of the MinioClient
        # as they handle input paths provided by STELAR API appropriately. (S3 like paths)
        ###############################################################################

        input = json_input['input'] if 'input' in json_input else json_input['inputs']
        params = json_input['parameters']
        for key in ['source', 'target']:
            if key not in input or key not in params:
                raise AttributeError(f"\"{key}\" should be in \"input\" and in \"parameters\"" )
        if 'algorithm' not in params:
            raise AttributeError(f"\"algorithm\" should be in  \"parameters\"" )
        
        java_dict = load_input(mc, input=input, parameters=params)
        java_dict['algorithm'] = params['algorithm']
        java_dict['output_path'] = '.local/results.nt'

        # Write dictionary to JSON file
        with open('.local/input.json', 'w+') as json_file:
            json.dump(java_dict, json_file, indent=4)

        jar_path = 'serial/target/geospatialinterlinking-1.0-SNAPSHOT-jar-with-dependencies.jar'
        
        # With arguments
        subprocess.run(["java", "-cp", jar_path, 'jsonWorkflow.JsonWorkflow', ".local/input.json", ".local/metrics.json"])
        # Method 1: Using json.load() with a file object
        with open('.local/metrics.json', 'r', encoding='utf-8') as file:
            metrics_dict = json.load(file)

        output = json_input['output'] if 'output' in json_input else json_input['outputs']
        if 'metrics' in output:
            mc.put_object(file_path='.local/metrics.json', s3_path=output['metrics'])

        if 'pairs' in output:
            print('mpika?')
            mc.put_object(file_path='.local/results.nt', s3_path=output['pairs'])
            

        json_output = {
                'message': 'Tool Executed Succesfully',
                'metrics': metrics_dict,
                'status': "success",
        }
        
        print(json_output)

        return json_output
    except Exception as e:
        print(traceback.format_exc())
        return {
            'message': 'An error occurred during data processing.',
            'error': traceback.format_exc(),
            'status': 500
        }
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise ValueError("Please provide 2 files.")
    with open(sys.argv[1]) as o:
        j = json.load(o)
    response = run(j)
    with open(sys.argv[2], 'w') as o:
        o.write(json.dumps(response, indent=4))
