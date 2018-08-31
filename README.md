# xls_json_covert_validate
This program first converts Excel file to JSON object, and then compares that object with valid schema. 

### INPUT FORMAT:
```sh
$ python converter.py <excel_file_name> <excel_sheet_name> <output.json> <schema_file_from_validate.json>
```

For example, to validate output of test.xls against schema.json, I will use following input
```sh
$ python test.xls test out.json schema.json
```

### OUTPUT FORMAT:

If no error, blank output, else output saying where the validation check has failed:

> jsonschema.exceptions.SchemaError: 'float' is not valid under any of the given schemas
>
> Failed validating 'anyOf' in schema['properties']['properties']['additionalProperties']['properties']['type']:
>    {'anyOf': [{'$ref': '#/definitions/simpleTypes'},
>              {'items': {'$ref': '#/definitions/simpleTypes'},
>               'minItems': 1,
>                'type': 'array',
>                'uniqueItems': True}]}
>
> On instance['properties']['marks']['type']:
>    'float'

