import inspect
import json
import sys
from jsonConfig import JsonConfig

# import table names
classes = inspect.getmembers(sys.modules['tables'], inspect.isclass)

is_user_config = True
# loading config.json
jsonConfig = JsonConfig()
if is_user_config:
    jsonConfigFile = open('data_hack_team_name/config.json', 'r')
    configString = jsonConfigFile.read()
    jsonConfig.updateConfig(configString)
