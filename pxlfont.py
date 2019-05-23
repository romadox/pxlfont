# Converts an image + text file alphabet into Angelcode BitmapFont format.
# Very simple, not many features.

# Arguments:
#   1 - image file
#   2 - config file

# Config File Options:
#   Usage: "option value" (i.e. "alph 0123456789" or "width 8")
#   name -- The font name
#   alph -- The characters in your pixel font
#   lheight -- Line height for this Font
#   base -- Pixels from top of line to base of glyphs (defaults to lheight)
#   width -- The width / widths. Separate multiple widths with commas
#   tail-- The amount of unused space at the end of the lines.

from PIL import Image
from sys import argv

img = ""
cfg = None
alph = ""
name = ""
lheight = 12
base = -1
widths = []
tails = []

if(len(argv) > 1):
    img = argv[1]
else:
    print("Image Filename: ")
    img = input()

if(len(argv) > 2):
    cfg = open(argv[2],"r")
else:
    print("Do you have a config file? (y/n): ")
    if(input().startswith(("Y","y"))):
        print("Config filename: ")
        cfg = open(input())

if(cfg != None):
    for line in cfg:
        if(line.startswith(("name","NAME"))):
            name = line.split(" ")[1].strip()
        elif(line.startswith(("alph","ALPH"))):
            alph = line.split(" ",1)[1]
        elif(line.startswith(("lheight","LHEIGHT"))):
            lheight = int(line.split(" ")[1].strip())
        elif(line.startswith(("base","BASE"))):
            base = int(line.split(" ")[1].strip())
        elif(line.startswith(("width","WIDTH"))):
            widths = line.split(" ",1)[1].strip()
            widths = widths.split(",")
            wd = []
            for w in widths:
                wd.append(int(w))
            widths = wd
        elif(line.startswith(("tail","TAIL"))):
            tails = line.split(" ",1)[1].strip()
            tails = tails.split(",")
            tl = []
            for t in tails:
                tl.append(int(t))
            tails = tl
else:
    print("Font name: ")
    name = input()

    print("Enter alphabet (all chars in your img, in order, no line breaks):")
    alph = input()

    print("Line height (pixels):")
    lheight = int(input())

    print("Enter widths (use commas for multiple): ")
    widths = input()
    widths = widths.split(",")
    ws = []
    for w in widths:
        ws.append(int(w.strip()))
    widths = ws

    print("Enter the tail sizes (use commas for multiple): ")
    tails = input()
    tails = tails.split(",")
    ts = []
    for t in tails:
        ts.append(int(t.strip()))
    tails = ts

image = Image.open(img)
image.load()
outname = img.rsplit(".",1)[0] + ".fnt"

if(img.find("/")>=0):
    img = img[img.rfind("/"):len(img)]
if(img.find("\\")>=0):
    img = img[img.rfind("\\"):len(img)]

rows = image.height // lheight

inx = 0
x = 0
y = 0
row = 0
tail = tails[row % len(tails)]
width = widths[inx]
done = inx >= len(alph)

output = "info face=\"" + name + "\"\n"
output = output + "common lineHeight=" + str(lheight) + " base=" + str(lheight)
output = output + " scaleW=" + str(image.width) + " scaleH=" + str(image.height)
output = output + " pages=1 packed=0 alphaChnl=0 redChnl=0 greenChnl=0 blueChnl=0\n"
output = output + "page id=0 file=\"" + img + "\"\n"
output = output + "chars count=" + str(len(alph)) + "\n"

while(not done):
    if(x >= image.width - tail):
        row += 1
        if(row >= rows):
            done = True
        else:
            x = 0
            y = lheight * row
            tail = tails[row % len(tails)]
    if(not done):
        output = output + "char id=" + str(ord(alph[inx])) + " x=" + str(x)
        output = output + " y=" + str(y) + " width=" + str(width) + " height=" + str(lheight)
        output = output + " xoffset=0 yoffset=0 page=0 chnl=15\n"
        x += width
        inx += 1
        width = widths[inx % len(widths)]
        if(inx >= len(alph)):
            done = True

out = open(outname, "w")
out.write(output)
out.close()
