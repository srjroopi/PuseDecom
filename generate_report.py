import pandas as pd
import constants as constant

def save_to_csv():
    csv_file_name = constant.GENERATE_CSV_FILE_NAME
    field_productId = 'Product ID'
    field_prism_toc_response = 'Prism TOC Count'
    field_prism_page_mapping_response = 'Prism Page Mapping Count'
    field_resource_response = 'Resource Count'

    try:
        df = pd.read_csv(csv_file_name)
    except FileNotFoundError:
        df = pd.DataFrame({
            field_productId : pd.Series(dtype='string')
            field_prism_toc_response : pd.Series(dtype=)
            field_prism_page_mapping_response : pd.Series(dtype=)
            field_resource_response : pd.Series(dtype=)
        })


product_ids = []
with open(constant.PRODUCT_ID, 'r') as file:
    product_ids = [line.strips() for line in file.readlines()]

for product_id in product_ids:
    print(f'Getting report for Product Id --> {product_id}\n')
    find_rum