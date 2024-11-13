import json
from save_response import file_exist


def find_prism_map(json_file):
    if file_exist(json_file):
        with open(json_file, 'r') as f:
            response_json = json.load(f)
        return parse_page_map(Mapping_response_data=response_json)
    else:
        return [set([]),set([])]

def parse_page_map(Mapping_response_data):
    mapping_data = Mapping_response_data[0]
    if mapping_data.get("bookId") and len(mapping_data.get("children", [])) > 1:
        result = ('Page Mapping passed')
        return result
    else:
        result = 'Page mapping not passed'
        return result