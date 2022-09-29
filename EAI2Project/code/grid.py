import argparse

from PIL import Image, ImageDraw, ImageFont

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("width", help="width of image in pixels",
                        type=int)
    parser.add_argument("height", help="height of image in pixels",
                        type=int)
    parser.add_argument("step_count", help="how many steps across the grid",
                        type=int)
    args = parser.parse_args()
    step_count = args.step_count
    height = args.height
    width = args.width

    image = Image.open("rsz_mappagrande.jpg")

    # Draw some lines
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / step_count)
    

    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=128)
        

    x_start = 0
    x_end = image.width

    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=128)

    font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSansBold.ttf", 20)
    x = 0
    y = 1
    for i in range(0,image.width,step_size):
        x+=1
        
        for j in range(0,image.height,step_size):
            txt = str(y)+","+str(x) 
            draw.text((i,j),txt,fill="black",align="center",font=font)
            y+=1
        y=1 

    del draw

    image.show()
