import xml.etree.ElementTree as ET

from src.serializers.serializer import Serializer

class XMLSerializer(Serializer):
    # Creates root element  <result>
    # Creates subelement 

    def save(self, list_of_dict, file_name):
        root=ET.Element("result")

        for item in list_of_dict:
            item_element=ET.SubElement(root, "item")

            for key, value in item.items():
                element=ET.SubElement(item_element, key)
                element.text=str(value)

        ET.indent(root, space="     ")
        tree = ET.tostring(
        root,
        encoding="utf-8",
        xml_declaration=True
        )

        with open(file_name, "wb") as f:
            f.write(tree)






