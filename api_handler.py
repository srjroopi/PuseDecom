# api_handler.py
import requests
import constants as constant

# # API 1: Get token
# def post_token(username, password):
#     url = constant.TOKEN_URL
#     data = {'userName': username, 'password': password}
#     # print(data)
#     headers = {
#         'Content-Type':'application/json'
#         }
#     response = requests.post(url=url, headers=headers, json=data)
#     if response.status_code == 200 or response.status_code == 201:
#         # print('Token generated')
#         token = response.json()["data"]
#         return token
#     else:
#         # print(response)
#         # print('Token generation failed')
#         return None

# API 1: Get token
def post_token():
    url = f"{constant.TOKEN_URL}"
    # data = {'userName': username, 'password': password}
    # print(url)
    headers = {
        'Content-Type':'application/x-www-form-urlencoded'
        }
    body = {
        'client_id':'8GqRlWRMZFhfJ0R3XKCrG0jx9NQ6B3ho',
        'grant_type':'password',
        'username':'tsttch1@schstage264.com',
        'password':'Test@123',
        'isMobile':'true'
    }
    response = requests.post(url=url, headers=headers, data=body)
    # print(response)
    if response.status_code in ( 200, 201 ):
        # print('Token generated')
        token = response.json()["data"]
        # print('token',token)
        access_token = token.get('access_token')
        # print(access_token)
        return access_token
    else:
        # print(response)
        # print('Token generation failed')
        return None

# API 2: Get PRISM_TOC_response
def get_PRISM_TOC_response(token, productId):
    url = f"{constant.PRISM_TOC_API}productId={productId}"
    # params = {
    #     'productId': productId
    # }
    headers = {
        #'Content-Type':'application/json',
        'X-Authorization': token,
        'isDeeplink' : 'true'
    }
    # print(url, token)
    response = requests.get(url=url, headers=headers)
    # print(response)
    if response.status_code == 200 or response.status_code == 201:
        response_data = response.json()
        # print('passed')
        return response_data
    else:
        print('not passed')
        return None

# API 3: Get PRISM_PAGE_MAPPING_response
def get_PRISM_PAGE_MAPPING_response(token, productId):
    url = f"{constant.PRISM_PAGE_MAPPING_API}/{productId}"
    headers = {
        #'Content-Type':'application/json',
        'X-Authorization': token,
        'isDeeplink' : 'true'
    }
    # print(token, productId)
    response = requests.get(url=url, headers=headers)
    print(response)
    if response.status_code == 200 or response.status_code == 201:
        response_data = response.json()
        bookId = response_data[0]["bookId"]
        print(bookId)
        print('passed')
        return response_data
    else:
        print('not passed')
        return None
    
#API 4: Post Course API
# def post_Course_API(token, bookId):
#     url = f"{constant.COURSE_API}"
#     headers = {
#         'Content-Type':'application/json',
#         'Authorization': token,
#     }
#     body = {
#         "bookIds": [
#             bookId
#         ],
#         "productIds": [
#             ""
#         ]
#     }
#     response = requests.post(url=url, headers=headers, json=body)
#     if response.status_code == 200 or response.status_code == 201:
#         response_data = response.json()
#         print('passed')
#         return response_data
#     else:
#         print('not passed')
#         return None

#API 5: Resource API
def get_Resource_API(token, productId):
    url = f"{constant.RESOURCE_API}productId={productId}&pageNo=1"
    headers = {
        'X-Authorization': token,
        'isDeeplink': 'true'
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        response_data = response.json()
        print('passed')
        return response_data
    else:
        print('not passed')
        return None
    
#API 6: CSG product API
# def post_CSG_PRODUCT_API(token, bookId):
#     url = f"{constant.CSG_PRODUCT_API}"
#     headers = {
#         'Content-Type' : 'application/json',
#         'application-id' : 'marin',
#         'Authorization': token
#     }
#     body = {
#         "fieldsToReturn": [
#           "productId",
#           "product_id",
#           "productSource",
#           "title",
#           "bookID",
#           "book_id",
#           "config",
#           "globalBookID",
#           "isbnList",
#           "isbn13",
#           "serverSideUuid",
#           "description",
#           "coverArt",
#           "language",
#           "editionTypeID",
#           "authors",
#           "author",
#           "authorList",
#           "pdfCoverArt",
#           "cover_image_url",
#           "navigationArt",
#           "thumbnailArt",
#           "thumbnail",
#           "schema:images",
#           "basePath",
#           "uPdfUrl",
#           "active",
#           "layout",
#           "bookServerUrl",
#           "index_id",
#           "productModelName",
#           "version",
#           "generalFeaturesTO.audioBook",
#           "generalFeaturesTO.serverSideUuid",
#           "generalFeaturesTO.serversideProcessed"
#         ],
#         "searchType": "FACET",
#         "queryString": bookId,
#         "responseSize": 200,
#         "searchOnMultipleIndexes": 'true',
#         "startIndex": 0
#       }
#     response = requests.post(url=url, headers=headers, json=body)
#     if response.status_code == 200 or response.status_code == 201:
#         response_data = response.json()
#         print('passed')
#         return response_data
#     else:
#         print('not passed')
#         return None
    



