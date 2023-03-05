import os
import json

from consts import *
import item_writer

def read_spawnmenu_item(k, v):
    icon_name = None
    if "icon_name" in v:
        icon_name = v["icon_name"]

    item_writer.make_spawnmenu_item(v["cmd"], k, icon_name)

spawnmenu = {}

for root, dirs, files in os.walk(SPAWNMENU_JSON_DIR, topdown=False):
    for name in files:
        with open(os.path.join(root, name), "r") as fp:
            spawnmenu.update( json.load(fp) )

for k, v in spawnmenu["items"].items():
    read_spawnmenu_item(k, v)
