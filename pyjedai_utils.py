from utils.mclient import MinioClient



data_type = {
    "csv" : "CSV",
    "tsv" : "TSV",
    "geojson" : "GeoJSON",
    "jsonrdf" : "JSONRDF",
    "rdf": "RDF"
}



# Check if input was correctly provided
def load_input(mc: MinioClient, input: dict, parameters: dict) -> dict:
    
    java_dict = {"source": {}, "target": {}} 
    
    for key in ["source", "target"]: 
        key_dict = java_dict[key]

        mc.get_object(s3_path=input[key][0], local_path=f".local/{key}")
        key_dict["path"] = f".local/{key}"


        d_type = parameters[key]["data_type"].lower()
        key_dict["data_type"] = data_type[d_type]
        
        if d_type in ['csv', 'tsv']:
            key_dict["geo_index"] = parameters[key]['geo_index']
            key_dict["attributes_first_row"] = parameters[key]['attributes_first_row']
        if d_type=='jsonrdf':
            key_dict["prefix_RDF"] = parameters[key]["prefix_RDF"]
        
        java_dict[key] = key_dict
    
    
    return java_dict
      
                        

