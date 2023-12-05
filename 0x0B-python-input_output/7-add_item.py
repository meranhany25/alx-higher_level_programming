#!/usr/bin/python3
""" module """
import json
import sys

save_to_json_file = _import_('5-save_to_json_file').save_to_json_file
load_from_json_file = _import_('6-load_from_json_file').load_from_json_file
mylist = []

try:
    filename = "add_item.json"
    mylist = load_from_json_file(filename)
except (FileNotFoundError, json.decoder.JSONDecodeError):
    pass
finally:
    for arg in sys.argv:
        if arg == sys.argv[0]:
            continue
        mylist.append(arg)
    save_to_json_file(mylist, filename)
