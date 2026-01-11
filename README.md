Implementation of a RDBMS


Language: Python 3.8+
Framework: Flask (for the web demo)

Project Overview

This project is a custom-built Relational Database Management System (RDBMS) designed from scratch for the Pesapal Junior Dev Challenge 2026.

Features:

-Custom Storage Engine: Persists data to disk using JSON files (mimicking table storage).
-SQL Parser: Supports a subset of standard SQL (`CREATE`, `INSERT` and `SELECT`).
-Performance Indexing: Implements a Primary Key index using Hash Maps (Python Dictionaries) for O(1) retrieval time.
-Interactive REPL: A command-line interface to interact with the database directly.
-Web Integration: A Flask-based web app that interfaces with the custom database engine.

Architecture & Design

The project is split into three layers:

1. The Interface (Front): `main.py` (CLI) and `app.py` (Web) to handle user input.
2. The Processor (Middle): `simple_db.py` that parses SQL strings and routes them to the correct logic.
3. The Storage (Back): The `data/` directory acts as the hard drive, storing each table as a distinct `.json` file.

Why JSON?
For this challenge, I chose JSON for storage because it is what I understand ,human-readable and allows for rapid debugging of the storage engine logic without needing binary hex editors.

Why Hash Map Indexing?
To satisfy the "ingenuity" requirement as per the instructions, I implemented a custom `GET` command that bypasses table scanning. It uses an in-memory dictionary to map Primary Keys directly to row indices, making lookups nearly instantaneous regardless of table size.

Installation & Setup

Prerequisites

-Python 3.x installed
-Git

Steps:

1. Clone the repository
```bash
git clone https://github.com/VenusKareen/pesapal_challenge.git
cd pesapal_challenge

```


2. Create and Activate Virtual Environment
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate

```


3. Install Dependencies
```bash
pip install -r requirements.txt

```



 How to Run:

1. The Interactive CLI (REPL)

Run the database engine directly in your terminal:

```bash
python main.py

```

Sample Commands I used:

```sql
CREATE TABLE users (id, name, role)
INSERT INTO users VALUES (1, 'Admin', 'Superuser')
SELECT * FROM users
GET FROM users WHERE id=1
exit

```

2. The Web Demo

Launch the phonebook application to see the DB in action:

```bash
cd web_demo
python app.py

```

-Open your browser to `http://127.0.0.1:5000`
- Add a record using the form.
- The data is processed by the custom engine and saved to `data/students.json`.

