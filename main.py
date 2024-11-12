# main.py
import constants as constant
from api_handler import get_PRISM_PAGE_MAPPING_response, get_Resource_API, post_token, get_PRISM_TOC_response
from parse_prism_toc import parse_prism_toc
from save_response import save_JSON_response, save_XML_response, createDirectory

# # Prism Mapping
def process_PRISM_MAPPING_response(token, productId):
    Mapping_response_data = get_PRISM_PAGE_MAPPING_response(token=token, productId=productId)
    if Mapping_response_data:
        file_name = f'{productId}_PRISM_Mapping.json'
        save_JSON_response(file_name, Mapping_response_data)
    else:
        print('PRISM Mapping Response not received')

# # Prism TOC
def process_PRISM_TOC_response(token, productId):
    print("token", productId)
    Toc_response_data = get_PRISM_TOC_response(token=token, productId=productId)
    if Toc_response_data:
        file_name = f'{productId}_PRISM_TOC.json'
        save_JSON_response(file_name, Toc_response_data)
        check_toc = parse_prism_toc(Toc_response_data)
        print(check_toc)
        print('PRISM TOC Response received')
    else:
        print('PRISM TOC Response not received')

# # Resource
def process_RESOURCE_response(token, productId):
    RESPONSE_data = get_Resource_API(token=token, productId=productId)
    if RESPONSE_data:
        file_name = f'{productId}_RESPONSE.json'
        save_JSON_response(file_name, RESPONSE_data)
    else:
        print('RESPONSE Response not received')

# Reading productId
def execute_request(productId,token):
    process_PRISM_TOC_response(token=token, productId=productId)
    process_PRISM_MAPPING_response(token=token, productId=productId)
    process_RESOURCE_response(token=token, productId=productId)


def inputValues(productIds,token):
    for productId in productIds:
        print(f'\nFetching for userId: {productId}')
        execute_request(productId=productId, token=token)

#  usage
# username = constant.TIBRON_USERNAME
# password = constant.TIBRON_PASSWORD

product_ids = []
with open(constant.PRODUCT_ID, 'r') as file:
    product_ids = [line.strip() for line in file.readlines()]

# # Create directory
# createDirectory()
# token = post_token(username, password)
# print(token)
# print('token generated')

print("posting")
post_response = post_token()
print('data', post_response)
token = post_response

if token:
    inputValues(productIds=product_ids, token=token)
    pass
else:
    print("Failed to get token")