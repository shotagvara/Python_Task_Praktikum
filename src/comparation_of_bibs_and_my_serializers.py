from src.serializers.json_serializer import JSONSerializer
from src.serializers.xml_serializer import XMLSerializer
import timeit
from src.database.repository import StudentsRoomsRepository


json_serializer = JSONSerializer()
xml_serializer = XMLSerializer()

list_of_dict = StudentsRoomsRepository().get_rooms_with_student_count()

json_time = timeit.timeit(
    lambda: json_serializer.save(list_of_dict, 'output.json'), 
    number=100
)

xml_time = timeit.timeit(
    lambda: xml_serializer.save(list_of_dict, 'output.xml'), 
    number=100
)

print(f"JSON serialization time: {json_time:.6f} seconds")
print(f"XML serialization time: {xml_time:.6f} seconds")


"""
Output:

(.venv) PS C:\Users\Amstel\Desktop\Innowise Praktikum\Python> python -m src.comparation_of_bibs_and_my_serializers
JSON serialization time: 202.891826 seconds
XML serialization time: 390.783289 seconds
"""
