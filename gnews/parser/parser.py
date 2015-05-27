# -*- coding: utf-8 -*-

import json
json_string = '{"nom":"Bamba", "prenom":"Mory"}'

parsed_json = json.loads(json_string)
print(parsed_json["nom"])
