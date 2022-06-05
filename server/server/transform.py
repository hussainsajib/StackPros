import json

from filesystem.models import FileTypes, FileStructure


def transform_file_structure():
    with open("./structure.json", "r") as file:
        data = json.loads(file.read())
        name, cat, value = "", data["type"], data["children"]
        children = [[name, cat, value]]
        while children:
            if isinstance(value, str):
                file_type, _ = FileTypes.objects.get_or_create(name=value)
            else:
                for name, child_attributes in value.items():
                    for cat, child in child_attributes.items():
                        if child_attributes[cat] == "file":
                            print(name)
                        children.append([name, cat, child])
            name, cat, value = children.pop()

