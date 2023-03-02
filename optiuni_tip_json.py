import json
import os
from configsx import file_path, fisier_optiuni_denumire

Optiuni = {'elemente':
    [
        {"Optiune_1": [{"alergare si volei": 700}]},
        {"Optiune_2": [{"inot si plimbare": 500}]},
        {"Optiune_3": [{"bicicleta si pilates": 800}]}
    ]
}


try:
    os.mkdir(file_path)
except Exception as e:
    pass

with open(f'{file_path}/{fisier_optiuni_denumire}', 'w') as f:
    f.write(json.dumps(Optiuni, indent=2))

