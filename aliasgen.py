import os
import json
from consts import *
from enum import Enum

class CmdType(Enum):
    DEFAULT = '%s'
    SPAWN_PROP = 'ent_create prop_physics model %s'
    SPAWN_RAGDOLL = 'ent_create prop_ragdoll model %s'
    SPAWN = 'ent_create %s'

def get_cmd_format(cmd_type):
    if not (cmd_type in CmdType.__members__):
        print(f"{ os.path.basename(__file__) }: '{cmd_type}' is not a valid {CmdType.__name__}, using defaults")
        return CmdType.DEFAULT.value

    return CmdType[cmd_type].value

# if not ALIAS_JSON.exists():
#     ALIAS_JSON.touch()

aliases = {}

for root, dirs, files in os.walk(ALIAS_JSON_DIR, topdown=False):
    for name in files:
        with open(os.path.join(root, name), "r") as fp:
            aliases.update( json.load(fp) )

with open(ALIAS_CFG, "w") as fp:
    for k, v in aliases.items():
        if isinstance(v['args'], list):
            cmd = get_cmd_format(v["cmd_type"]) % ';'.join( v["args"] )
        else:
            cmd = get_cmd_format(v["cmd_type"]) % v["args"]

        fp.write(f'alias {k} "{ cmd }"\n')

