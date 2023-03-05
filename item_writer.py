import os
import shutil

from spawnmenu_index import SPAWNMENU_INDEX
from pathlib import Path

INVALID_CHARS = r'<>:"/\|?*'
PADDED_STRING_LEN_MAX = 65

BASE_SAV_FILE = "base.sav"
SPAWNMENU_ITEM_FILE = ";%s;wait .sav"
ICON_FILE = "icons/%s.tga"

def check_filename(filename):
    return any(c in INVALID_CHARS for c in filename)

def make_padded_bytes(string, truncate=False):
    if len(string) > PADDED_STRING_LEN_MAX:
        if not truncate:
            raise ValueError(f"string is longer than max length ({PADDED_STRING_LEN_MAX})")

        # truncate the string from the max
        return string[:PADDED_STRING_LEN_MAX]

    return string.ljust(PADDED_STRING_LEN_MAX)

def make_spawnmenu_item(command, spawmenu_name, icon=None):
    padded_name = make_padded_bytes(spawmenu_name.encode("utf-8"))

    if isinstance(command, list):
        filename = SPAWNMENU_ITEM_FILE % ';'.join(command)
    else:
        filename = SPAWNMENU_ITEM_FILE % command

    if check_filename(filename):
        raise Exception(f'Invalid filename "{filename}"')

    filename = os.path.join("items", filename)

    shutil.copy(BASE_SAV_FILE, filename)

    if icon:
        icon_filename = Path( filename ).with_suffix('.tga')
        shutil.copy(ICON_FILE % icon, icon_filename)

    with open(filename, "r+b") as fp:
        fp.seek(SPAWNMENU_INDEX)
        fp.write(padded_name)
