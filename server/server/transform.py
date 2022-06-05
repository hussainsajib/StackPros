import json

from filesystem.models import FileTypes, FileStructure


def transform_file_structure():
    with open("./structure.json", "r") as file:
        data = json.loads(file.read())
        name, cat, value = "root", data["type"], data["children"]
        root_node, created = file_object_factory(name, cat)
        stack = [[name, cat, value]]
        while stack:
            if isinstance(value, str):
                file_type, _ = FileTypes.objects.get_or_create(name=value)
            else:
                for child_name, child_attributes in value.items():
                    for key, val in child_attributes.items():
                        if key == "type" and val == "file":
                            f, _ = file_object_factory(child_name, val)
                            f.parent = root_node
                            f.save()
                        elif key == "type" and val == "dir":
                            d, _ = file_object_factory(child_name, val)
                            d.parent = root_node
                            d.save()
                            root_node = d
                        if key == "children" and val:
                            stack.append([child_name, child_attributes["type"], child_attributes["children"]])
            name, cat, value = stack.pop()


def file_object_factory(name, category):
    file_type = FileTypes.objects.get(name=category)
    file, created = FileStructure.objects.get_or_create(
        name=name,
        file_type=file_type,
        defaults={
            "child": None,
            "parent": None
        }
    )
    return file, created
