import json
import os
import re

class SimpleDB:
    def __init__(self, storage_dir="data"):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)
        self.tables = {}

    def _get_table_path(self, table_name):
        return os.path.join(self.storage_dir, f"{table_name}.json")

    def _load_table(self, table_name):
        """Load table data from disk into memory."""
        path = self._get_table_path(table_name)
        if not os.path.exists(path):
            return None
        with open(path, 'r') as f:
            return json.load(f)

    def _save_table(self, table_name, data):
        """Persist memory data to disk."""
        path = self._get_table_path(table_name)
        with open(path, 'w') as f:
            json.dump(data, f, indent=4)

    def execute(self, query):
        """The Main SQL Parser."""
        query = query.strip()
        
       # Table Creation starts here:
        if query.upper().startswith("CREATE TABLE"):
            match = re.match(r"CREATE TABLE (\w+)\s*\((.+)\)", query, re.IGNORECASE)
            if match:
                table_name, columns_str = match.groups()
                columns = [c.strip() for c in columns_str.split(',')]
                
                table_data = {
                    "columns": columns,
                    "rows": [],      
                    "pk_index": {}   
                }
                self._save_table(table_name, table_data)
                return f"Table '{table_name}' created."

        #Adding data starts here:
        elif query.upper().startswith("INSERT INTO"):
            match = re.match(r"INSERT INTO (\w+) VALUES\s*\((.+)\)", query, re.IGNORECASE)
            if match:
                table_name, values_str = match.groups()
                
                
                values = [v.strip().strip("'").strip('"') for v in values_str.split(',')]
                
                table_data = self._load_table(table_name)
                if not table_data: return f"Error: Table '{table_name}' does not exist."

                if len(values) != len(table_data['columns']):
                    return "Error: Column count mismatch."

                pk_id = values[0]
                if pk_id in table_data['pk_index']:
                     return f"Error: Duplicate Primary Key '{pk_id}'."

                table_data['rows'].append(values)

                table_data['pk_index'][pk_id] = len(table_data['rows']) - 1
                
                self._save_table(table_name, table_data)
                return "1 row inserted."

        #Selecting data starts here:
        elif query.upper().startswith("SELECT * FROM"):
            match = re.match(r"SELECT \* FROM (\w+)", query, re.IGNORECASE)
            if match:
                table_name = match.group(1)
                table_data = self._load_table(table_name)
                if not table_data: return f"Error: Table '{table_name}' not found."
                return table_data['rows']

        elif query.upper().startswith("GET FROM"):
            match = re.match(r"GET FROM (\w+) WHERE id=(.+)", query, re.IGNORECASE)
            if match:
                table_name, target_id = match.groups()
                table_data = self._load_table(table_name)

                if target_id in table_data['pk_index']:
                    row_index = table_data['pk_index'][target_id]
                    return table_data['rows'][row_index]
                else:
                    return "Record not found."

        return "Syntax Error or Unsupported Command."