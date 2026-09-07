from src.application import Application
from src.loaders.json_loaders import JSONLoader

from src.serializers.json_serializer import JSONSerializer
from src.serializers.xml_serializer import XMLSerializer

from src.database.repository import StudentsRoomsRepository

import argparse

def main():
    parser = argparse.ArgumentParser()

    # All 3 arguments are required.
    # The format must be either JSON or XML. Other values are not allowed.
    parser.add_argument("--students", required=True)
    parser.add_argument("--rooms", required=True)
    parser.add_argument("--format", choices=["json", "xml"], required=True)


    args = parser.parse_args()


    if args.format == "json":
        serializer = JSONSerializer()
        extension = "json"
    else:
        serializer = XMLSerializer()
        extension = "xml"


    # Create a repository object to access database operations.
    repository = StudentsRoomsRepository()

    try:
        app = Application(
            repository,
            JSONLoader,
            serializer,
            extension
        )

        app.run(
            args.rooms,
            args.students
        )
    finally: 
        repository.close_connection()

if __name__ == "__main__":
    main()


