import json

from src.serializers.serializer import Serializer

class JSONSerializer(Serializer):
    def save(self, list_of_dict, file_name):
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(
                list_of_dict,
                f,
                indent=4,
                default=float
            )
            #indent=4 makes its format looking good with 4 spaces like:
            #[
            #   {
            #       some data
            #       some data2
            #   }
            #]
            #Could be also 2 spaces or else
