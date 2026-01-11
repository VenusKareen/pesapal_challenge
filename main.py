from src.simple_db import SimpleDB
import sys

def run_repl():
    db = SimpleDB()
    print("="*40)
    print("PESAPAL CHALLENGE DB (v1.0)")
    print("Type 'exit' to quit.")
    print("Supported Commands:")
    print("  - CREATE TABLE table_name (col1, col2)")
    print("  - INSERT INTO table_name VALUES (val1, val2)")
    print("  - SELECT * FROM table_name")
    print("  - GET FROM table_name WHERE id=value")
    print("="*40)

    while True:
        try:
            user_input = input("SQL> ")
            
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
            
            result = db.execute(user_input)
            
            if isinstance(result, list):
                print(f"Returned {len(result)} rows:")
                for row in result:
                    print(f"  {row}")
            else:
                print(result)
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    run_repl()