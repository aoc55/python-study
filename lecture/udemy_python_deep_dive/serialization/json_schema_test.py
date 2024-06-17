# [ json_schema 실습 ]
# pip install jsonschema

from jsonschema import validate
from jsonschema.exceptions import ValidationError
from json import loads, dumps, JSONDecodeError


# - Schema 정의
person_schema_simple = {
    "type": "object",
    "properties": {
        "firstName": {
            "type" : "string",
            "minLength": 1
        },
        "middleInitial": {"type": "string"},
        "lastName": {"type": "string"},
        "age": {"type": "number"}

    }
}


# - 샘플데이터
sample_data_ok = '''
{
    "firstName": "John",
    "middleInitial": "M",
    "lastName": "Cleese",
    "age": 79
}
'''

sample_data_simple = '''
{
    "firstName": "John",
    "age": 100
}
'''

sample_data_wrong = '''
{
    "firstName": "John",
    "middleInitial": "M",
    "lastName": "Cleese",
    "age": "Unknown"
}
'''

sample_data_wrong_enum = '''
{
    "firstName": "John",
    "middleInitial": "M",
    "lastName": "Cleese",
    "age": "Unknown",
    "eyeColor": "WRONG_COLOR"
}
'''


person_schema_detail = {
    "type": "object",
    "properties": {
        "firstName": {
            "type" : "string",
            "minLength": 1
        },
        "middleInitial": {
            "type": "string",
            "minLength": 1,
            "maxLength": 1
        },
        "lastName": {
            "type": "string",
            "minLength": 1
        },
        "age": {
            "type": "number",
            "minimum": 0
        },
        "eyeColor": {
            "type": "string",
            "enum": ["blue", "brown", "gray", "black"]
        }
    },
    "required": ["firstName", "lastName"]
}


def custom_validate(json_data, json_schema):
    try:
        validate(loads(json_data), json_schema)
    except JSONDecodeError as ex:
        print(f'Invalid Json -> {ex}')
    except ValidationError as ex:
        print(f'Validation Error -> {ex}')
    else:
        print("JSON is valid and conforms to Schema !!")


custom_validate(sample_data_ok, person_schema_simple)
custom_validate(sample_data_simple, person_schema_simple)
custom_validate(sample_data_wrong, person_schema_simple)  # 'Unknown' is not of type 'number'

print("------------------------------------------------")


custom_validate(sample_data_ok, person_schema_detail)
custom_validate(sample_data_simple, person_schema_detail)  # 'lastName' is a required property
custom_validate(sample_data_wrong, person_schema_detail)   # Failed validating 'type' in schema['properties']['age']:
custom_validate(sample_data_wrong_enum, person_schema_detail)   # Failed validating 'enum' in schema['properties']['eyeColor']:

print("------------------------------------------------")



# [ Draft4Validator 실습 ]
# - JSON 스키마의 초안 버전 4(Draft 4)를 지원하는 검증 클래스
from jsonschema import Draft4Validator
validator = Draft4Validator(person_schema_detail)

sample_data_wrong_complex = '''
{
    "firstName": "John",
    "middleInitial": "M",
    "lastName": "Cleese",
    "age": "Unknown",
    "eyeColor": "WRONG_COLOR"
}
'''


for error in validator.iter_errors(loads(sample_data_wrong_complex)):
    print(error, end='\n **** \n')

# - 아래와 같이 '모든' 실패에 대해 한번에 얻을 수 있음
# 'Unknown' is not of type 'number'
#
# Failed validating 'type' in schema['properties']['age']:
#     {'minimum': 0, 'type': 'number'}
#
# On instance['age']:
#     'Unknown'
#  ****
# 'WRONG_COLOR' is not one of ['blue', 'brown', 'gray', 'black']
#
# Failed validating 'enum' in schema['properties']['eyeColor']:
#     {'enum': ['blue', 'brown', 'gray', 'black'], 'type': 'string'}
#
# On instance['eyeColor']:
#     'WRONG_COLOR'
#  ****
