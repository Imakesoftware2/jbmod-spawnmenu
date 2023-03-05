import argparse
from PIL import Image, ImageOps
from pathlib import Path

THUMB_SIZE = (180, 100)

parser = argparse.ArgumentParser(description='Spawnmenu thumbnail batch tool')

parser.add_argument('paths', type=Path, nargs='+',
                    help='input image(s) to turn into spawnmenu thumbnails')

args = parser.parse_args()

for path in args.paths:
    im = Image.open(path)
    #im.thumbnail(THUMB_SIZE, Image.BILINEAR)
    thumb = ImageOps.fit(im, THUMB_SIZE, Image.BILINEAR)
    thumb.save( path.with_suffix('.tga') )
