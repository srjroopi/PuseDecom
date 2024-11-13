import json
from save_response import file_exist

def find_resource(json_file):
    if file_exist(json_file):
        with open(json_file, 'r') as f:
            response_json = json.load(f)
        return parse_resource(resource_response_data=response_json)
    else:
        return [set([]),set([])]

def parse_resource(resource_response_data):
    resource_data = resource_response_data[0]
    if resource_data.get("productId") and len(resource_data.get("resources", [])) > 1:
        result = ('resources passed')
        return result
    else:
        result=('resource not passed')
        return result