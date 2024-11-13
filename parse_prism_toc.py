import json
from save_response import file_exist


def find_prism_toc(json_file):
    if file_exist(json_file):
        with open(json_file, 'r') as f:
            response_json = json.load(f)
        return parse_prism_toc(Toc_response_data=response_json)
    else:
        return [set([]),set([])]

def parse_prism_toc(Toc_response_data):
    if Toc_response_data.get("productId") and len(Toc_response_data.get("children", [])) > 1:
        result = ('TOC passed')
        return result
    else:
        result='TOC not passed'
        return result