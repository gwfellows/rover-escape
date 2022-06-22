from PIL import Image

im = Image.open('background.png')
pix = im.load()
width, height =  im.size

print("[")
for y in range(height):
    print("[", end="")
    for x in range(width):
        print(1 if (pix[x,y][:3] == (213, 176, 117)) else 0, end=",")
    print("],")
print("]")