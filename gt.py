from PIL import Image, ImageDraw, ImageFont
from colour import Color
import numpy as np

def asciiart(in_f, SC, GCF,  out_f, color1='black', color2='blue', bgcolor='white'):

    
    chars = np.asarray(list(' .,:irs?@9B&#'))

    font = ImageFont.load_default()
    letter_width = font.getsize("x")[0]
    letter_height = font.getsize("x")[1]

    WCF = letter_height/letter_width

    
    img = Image.open(in_f)

    
    widthByLetter=round(img.size[0]*SC*WCF)
    heightByLetter = round(img.size[1]*SC)
    S = (widthByLetter, heightByLetter)

    
    img = img.resize(S)
    
    
    img = np.sum(np.asarray(img), axis=2)
    
    
    img -= img.min()
    img = (1.0 - img/img.max())**GCF*(chars.size-1)
    
    
    lines = ("\n".join( ("".join(r) for r in chars[img.astype(int)]) )).split("\n")

    
    nbins = len(lines)
    colorRange =list(Color(color1).range_to(Color(color2), nbins))

    
    newImg_width= letter_width *widthByLetter
    newImg_height = letter_height * heightByLetter
    newImg = Image.new("RGBA", (newImg_width, newImg_height), bgcolor)
    draw = ImageDraw.Draw(newImg)

    
    leftpadding=0
    y = 0
    lineIdx=0
    for line in lines:
        color = colorRange[lineIdx]
        lineIdx +=1

        draw.text((leftpadding, y), line, color.hex, font=font)
        y += letter_height

    
    newImg.save(out_f)

# main() 
if __name__=='__main__':

    inputf = " "  # Input image file name

    SC = 0.1    # pixel sampling rate in width
    GCF= 2      # contrast adjustment

    asciiart(inputf, SC, GCF, "results.png")   #default color, black to blue
    asciiart(inputf, SC, GCF, "results_pink.png","blue","pink")
