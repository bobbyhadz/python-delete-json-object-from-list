# Delete a JSON object from a list in Python

import json

file_name = 'example.json'

with open(file_name, 'r', encoding='utf-8') as f:
    my_list = json.load(f)

    # [{'id': 1, 'name': 'Alice'},
    #  {'id': 2, 'name': 'Bob'},
    #  {'id': 3, 'name': 'Carl'}]
    print(my_list)

    for idx, obj in enumerate(my_list):
        if obj['id'] == 2:
            my_list.pop(idx)

new_file_name = 'new-file.json'

with open(new_file_name, 'w', encoding='utf-8') as f:
    f.write(json.dumps(my_list, indent=2))