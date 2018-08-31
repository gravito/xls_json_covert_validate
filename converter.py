import jsonschema
import json
import sys
import xlrd

#Importing xls workbook and sheet name
workbook = xlrd.open_workbook(sys.argv[1])
worksheet = workbook.sheet_by_name(sys.argv[2])

data = []
keys = [v.value for v in worksheet.row(0)]

for row_number in range(worksheet.nrows):
    #skipping first row which is Heading
    if row_number == 0:
        continue
    row_data = {}

    #using column number as keys to fill data
    for col_number, cell in enumerate(worksheet.row(row_number)):
        row_data[keys[col_number]] = cell.value
    data.append(row_data)

#writing converting xls file to json object
with open(sys.argv[3], 'w') as json_file:
    json_file.write(json.dumps({'data': data}))

#loading up schema object
with open(sys.argv[4], 'r') as f:
    schema_data = f.read()
schema = json.loads(schema_data)

#loading up converted json object
with open(sys.argv[3], 'r') as f:
    new_schema_data = f.read()
new_schema = json.loads(new_schema_data)

#validating schemas, if no output, schema is correct
jsonschema.validate(new_schema, schema)


