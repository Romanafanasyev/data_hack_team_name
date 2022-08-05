import inspect
import json
import sys
from tables import args_dict

# import table names
classes = inspect.getmembers(sys.modules['tables'], inspect.isclass)

# loading config.json
jsonConfigFile = open('data_hack_team_name/config.json', 'r')
configJson = jsonConfigFile.read()
configData = json.loads(configJson)

# update arguments values from config.json
for class_name in classes:
    if class_name[0] in configData:
        for arg_name in args_dict.keys():
            if arg_name in configData[class_name[0]]:
                args_dict[arg_name] = configData[class_name[0]][arg_name]

print(args_dict)