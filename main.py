# main.py
import constants as constant
from api_handler import get_PRISM_PAGE_MAPPING_response, get_Resource_API, post_Course_API, post_csg_token, post_sys_token, get_PRISM_TOC_response
from save_response import save_JSON_response, createDirectory

# # Prism TOC
def process_PRISM_TOC_response(token, productId):
    print("token", productId)
    Toc_response_data = get_PRISM_TOC_response(token=token, productId=productId)
    if Toc_response_data:
        file_name = f'{productId}_PRISM_TOC.json'
        save_JSON_response(file_name, Toc_response_data)
        print('PRISM TOC Response received')
    else:
        print('PRISM TOC Response not received')

# # Prism Mapping
def process_PRISM_MAPPING_response(token, productId):
    Mapping_response_data = get_PRISM_PAGE_MAPPING_response(token=token, productId=productId)
    if Mapping_response_data:
        file_name = f'{productId}_PRISM_Mapping.json'
        save_JSON_response(file_name, Mapping_response_data)
        print('PRISM Page Mapping received')
    else:
        print('PRISM Mapping Response not received')

# # Resource
def process_RESOURCE_response(token, productId):
    RESOURCE_data = get_Resource_API(token=token, productId=productId)
    if RESOURCE_data:
        file_name = f'{productId}_RESOURCE.json'
        save_JSON_response(file_name, RESOURCE_data)
        print('Resource received')
    else:
        print('RESOURCE Response not received')

# Course or paper api
def process_course(token, productId):
    COURSE_DATA = post_Course_API(token=token, productId=productId)
    if COURSE_DATA:
        file_name = f'{productId}_Course.json'
        save_JSON_response(file_name, COURSE_DATA)
        print('course received')
    else:
        print('Course not received')

# Reading productId
def execute_request(productId,token):
    process_PRISM_TOC_response(token=token, productId=productId)
    process_PRISM_MAPPING_response(token=token, productId=productId)
    process_RESOURCE_response(token=token, productId=productId)
    process_course(token=token,productId=productId)


def inputValues(productIds,token):
    for productId in productIds:
        print(f'\nFetching for productId: {productId}')
        execute_request(productId=productId, token=token)

#  usage
csg_username = constant.CSG_TOKEN_USERNAME
csg_password = constant.CSG_TOKEN_PASSWORD

sys_username = constant.SYS_TOKEN_USERNAME
sys_password = constant.SYS_TOKEN_PASSWORD

product_ids = []
with open(constant.PRODUCT_ID, 'r') as file:
    product_ids = [line.strip() for line in file.readlines()]

# Create directory
createDirectory()
csg_token = post_csg_token(csg_username, csg_password)
print(csg_token)
print('csg token generated')

createDirectory()
sys_token = post_sys_token(sys_username, sys_password)
print(sys_token)
print('sys token generated')

token = sys_token

if token:
    inputValues(productIds=product_ids, token=token)
    pass
# elif csg_token:
#     csgValues(csg_token)
#     pass
else:
    print("Failed to get token")