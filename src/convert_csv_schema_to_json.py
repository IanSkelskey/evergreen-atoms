import csv
import json

# Input and output file paths
csv_file_path = 'Biblio-Schema.csv'
json_file_path = 'Biblio-Schema-Output.json'

# Initialize a dictionary to hold the schemas
schemas = {}

# Read the CSV file
with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    
    # Skip the first row
    next(reader)
    
    # Iterate over each row in the CSV
    for row in reader:
        # Each row is a JSON string, so parse it
        table_info = json.loads(row[0])
        
        schema_name = table_info['table_schema']
        table_name = table_info['table_name']
        columns = table_info['columns']
        
        # Create a new schema entry if it doesn't exist
        if schema_name not in schemas:
            schemas[schema_name] = {}
        
        # Add the table and its columns to the schema
        schemas[schema_name][table_name] = []
        for column in columns:
            schemas[schema_name][table_name].append({
                'column_name': column['column_name'],
                'column_type': column['udt_name']
            })

# Convert the schemas dictionary to a list of schemas with tables and columns
output_json = []
for schema_name, tables in schemas.items():
    schema_entry = {
        'schema_name': schema_name,
        'tables': []
    }
    for table_name, columns in tables.items():
        table_entry = {
            'table_name': table_name,
            'columns': columns
        }
        schema_entry['tables'].append(table_entry)
    output_json.append(schema_entry)

# Write the JSON output to a file
with open(json_file_path, 'w') as json_file:
    json.dump(output_json, json_file, indent=4)

print(f"JSON file saved to: {json_file_path}")