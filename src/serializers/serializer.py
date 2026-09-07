# Abstract base class for serializers.
# Defines the common save() method that all serializers must implement.


import abc 

class Serializer(abc.ABC):
    @abc.abstractmethod
    def save(self, list_of_dict, file_name):
        pass