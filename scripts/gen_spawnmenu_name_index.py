SPAWNMENU_NAME_IDENT = b"!SPAWNMENUNAME!"
SPAWNMENU_INDEX_PY = "SPAWNMENU_INDEX = %d"

with open('../base.sav', 'rb') as fp:
    content = fp.read()
    ident_index = content.index(SPAWNMENU_NAME_IDENT)

with open('../spawnmenu_index.py', 'w') as fp:
    if not ident_index:
        raise Exception("spawnmenu name index not found or invalid")
    fp.write(SPAWNMENU_INDEX_PY % ident_index)
