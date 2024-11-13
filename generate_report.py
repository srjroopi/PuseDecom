import pandas as pd
import constants as constant
from parse_course import find_course
from parse_page_map import find_prism_map
from parse_prism_toc import find_prism_toc
from parse_resource import find_resource
from save_response import get_full_path

def save_to_csv(product_id,parse_prism_toc,prism_page_map_files,resource_files,course_files):
    csv_file_name = constant.GENERATE_CSV_FILE_NAME
    field_productId = 'Product ID'
    field_prism_toc_response = 'Prism TOC'
    field_prism_page_mapping_response = 'Prism Page Mapping'
    field_prism_resource = 'Resource'
    field_Course = 'Course/Paper API'

    try:
        df = pd.read_csv(csv_file_name)
    except FileNotFoundError:
        df = pd.DataFrame ({
            field_productId:pd.Series(dtype='string'),
            field_prism_toc_response:pd.Series(dtype='string'),
            field_prism_page_mapping_response:pd.Series(dtype='string'),
            field_prism_resource:pd.Series(dtype='string'),
            field_Course:pd.Series(dtype='string')
        })
    
    prism_toc = parse_prism_toc
    prism_page_map = prism_page_map_files
    resource = resource_files
    course = course_files
    
    mask = df[field_productId] == product_id
    if mask.any():
        df.loc[mask, field_prism_toc_response] = prism_toc
        df.loc[mask, field_prism_page_mapping_response] = prism_page_map
        df.loc[mask, field_prism_resource] = resource
        df.loc[mask, field_Course] = course
    else:
        new_row = pd.DataFrame({
            field_productId: product_id,
            field_prism_toc_response: prism_toc,
            field_prism_page_mapping_response:prism_page_map,
            field_prism_resource:resource,
            field_Course:course
            }, index=[0])  # Create a new DataFrame with one row
        df = pd.concat([df, new_row], ignore_index=False)
    df.to_csv(csv_file_name, index=False)

product_ids = []
with open(constant.PRODUCT_ID, 'r') as file:
    product_ids = [line.strip() for line in file.readlines()]

for product_id in product_ids:
    print(f'Getting report for Product Id --> {product_id}\n')

    #for toc
    prism_file_name = f'{product_id}_PRISM_TOC.json'
    prism_file_path = get_full_path(file_name=prism_file_name)
    prism_files = find_prism_toc(json_file=prism_file_path)

    #for page mapping
    prism_page_map_file_name=f'{product_id}_PRISM_Mapping.json'
    prism_page_file_path=get_full_path(file_name=prism_page_map_file_name)
    prism_page_map_files=find_prism_map(json_file=prism_page_file_path)

    #for resources
    resource_file_name=f'{product_id}_RESOURCE.json'
    resource_file_path=get_full_path(file_name=resource_file_name)
    resource_files = find_resource(json_file=resource_file_path)
    
    #for course
    course_file_name=f'{product_id}_Course.json'
    course_file_path=get_full_path(file_name=course_file_name)
    course_files = find_course(json_file=course_file_path)

    save_to_csv(product_id,prism_files,prism_page_map_files,resource_files, course_files)
print('CSV File generated successfully')