# From the video
# https://www.youtube.com/watch?v=55iwMYv8tGI

density = 'N@#W$86420?!abc;:+=-,._ '
#          0---------------------255

imgSize = 1000

def setup():
    size(imgSize, imgSize)

    img = loadImage("retrato2.jpg")
    
    background(0)
#    image(img, 0, 0, width, height)
    
    w = width / img.width
    h = height / img.height
    
    loadPixels()
    
    for i in range(img.width):
        for j in range(img.height):
            pixelIndex = i + j * img.width
            
            r = red(img.pixels[pixelIndex])
            g = green(img.pixels[pixelIndex])
            b = blue(img.pixels[pixelIndex])
            avg = (r + g + b) / 3
            
            densityLength = len(density)
            charIndex = floor(map(avg, 0, 250, densityLength-1, 0))
            
            fill(255)
            textSize(w)
            textAlign(CENTER, CENTER)
            text(density[charIndex], i*w + w*0.5, j*h + h*0.5)
    
    saveFrame("AsciiSelfie2.jpg")
