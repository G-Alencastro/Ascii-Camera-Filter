from statistics import mean
from PIL import Image
import os
import cv2

INPUT_FOLDER = 'Input'
TUNES = '▁▁' '░░' '▒▒' '▓▓' '██'
TUNES = '▁▂▃▄▅▆▇'
TUNES = ' ░▒▓█'
TUNES = '_-;=8$@#Ñ'
TUNES = '_.,-=+:;cba!?0123456789$W#@Ñ'


res = 10

#return the relative path in 'Input' folder
def in_path(filename):
    return os.path.join(INPUT_FOLDER, filename)

#return the mean luminanse of a chosen image divided in boxes
def get_tunes(img, square_size=res):
    w, h = img.size
    
    x_squares = w//square_size
    y_squares = h//square_size

    squares = []
    
    for ys in range(y_squares):
        for xs in range(x_squares):
        
            square = []
            for y in range((ys)*square_size, ys*square_size+1):
                for x in range((xs)*square_size, xs*square_size+1):
                    pixel = img.getpixel((x, y))
                    lum = int(mean(pixel))
                    square.append(lum)

            squares.append(int(mean(square)))
    
    return squares

def get_text(boxes, img, square_size=res, tunes=TUNES):
    w, h = img.size
    x_squares = w//square_size
    text = '\n'
    
    for i in range(len(boxes)):
        text += tunes[(boxes[i])//(255//len(TUNES)+1)]*2
        if i%x_squares == 0 and i > 0:
            text += '\n'

    return text

def ascii_filter(input):
    color_converted = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(color_converted)
    boxes = get_tunes(img)
    txt = get_text(boxes, img)
    print(txt)



if __name__ == '__main__':
    pass

