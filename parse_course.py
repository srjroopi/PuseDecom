import json
from save_response import file_exist

def find_course(json_file):
    if file_exist(json_file):
        with open(json_file, 'r') as f:
            response_json = json.load(f)
        return parse_course(course_response_data=response_json)
    else:
        return [set([]),set([])]

def parse_course(course_response_data):
    resource_data = course_response_data[0]
    if resource_data.get("bookId") and resource_data.get("downloadURL"):
        result = ('course passed')
        return result
    else:
        result=('course not passed')
        return result