# Students and Rooms

## Description
This application loads rooms and students data from JSON files and stores it in a PostgreSQL database.
It executes four SQL queries for analyzing students and rooms.
All calculations are performed on the database side.
The query results can be exported in JSON or XML format.


## Technologies
- Python 3
- PostgreSQL
- psycopg 3
- python-dotenv
- SQL


## Project Structure
data/
        rooms.json
        students.json

    sql/
        schema.sql
        indexes.sql

    src/
        database/
            connection.py
            repository.py
        loaders/
            json_loaders.py
        serializers/
            serializer.py
            json_serializer.py
            xml_serializer.py
        application.py

    main.py
    requirements.txt
    .env


## Database Setup
Create a PostgreSQL database and execute:

    sql/schema.sql

Optional indexes for query optimization can be created using:

    sql/indexes.sql


## Installation
Create a virtual environment:

    python -m venv .venv

Activate it on Windows:

    .venv\Scripts\Activate.ps1

Install the dependencies:

    pip install -r requirements.txt


## Configuration
Create a `.env` file in the project root based on `.env.example`.

Example:

    DATABASE_URL=postgresql://username:password@localhost:5432/database_name


## Usage
JSON output:

    python main.py --students data/students.json --rooms data/rooms.json --format json

XML output:

    python main.py --students data/students.json --rooms data/rooms.json --format xml


## Output
The application creates four output files:

- `task_1.json/xml` — rooms and the number of students in each room
- `task_2.json/xml` — five rooms with the smallest average student age
- `task_3.json/xml` — five rooms with the largest student age difference
- `task_4.json/xml` — rooms with students of different sexes


## Database Queries
The application performs four database queries:

1. List of rooms and the number of students in each room.
2. Five rooms with the smallest average student age.
3. Five rooms with the largest difference in student ages.
4. Rooms where students of different sexes live.

All calculations and aggregations are performed in PostgreSQL.


## Index Optimization
## Index Optimization

The proposed indexes are defined in `sql/indexes.sql`.

Indexes are created for:

- `students(room)`
- `students(room, birthday)`
- `students(room, sex)`

The indexes are intended to support joins, grouping and queries involving student age and sex.

PostgreSQL may still choose a sequential scan when it estimates that scanning the whole table is more efficient. Index creation does not guarantee that an index will be used for every query.