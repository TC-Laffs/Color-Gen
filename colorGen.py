import math
import colour as color
import random
import PIL
import PIL.Image
import tkinter
from PIL import Image, ImageTk,ImageOps
from PIL import ImageFont, ImageDraw
from tkinter import *
from tkinter import filedialog
import os
from os import listdir
from os.path import isfile, join
import sys
if sys.version_info[0] < 3:
   import Tkinter as tk
else:
   import tkinter as tk
dirname = os.path.dirname(__file__)
arialBig = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf",32)
arialSmol = ImageFont.truetype(r"C:\Windows\Fonts\arial.ttf",24)
lucky = random.randrange(0,100000)
if lucky == 69:
   autoSave = input("Would you like to enable autosave for this session?\nPro tip: Input anything other than 'Y' or 'N' to skip the next save prompt!\n(Y/N)\n ")
   autoSave = utoSave.upper()
else:
   autoSave = input("Would you like to enable autosave for this session?\n(Y/N)\n ")
   autoSave = autoSave.upper()
skip = input("Would you like to enable previews for this session?\n(Y/N)\n ")
skip = skip.upper()
validrgbSeed = 0
def reqSeed():
   seed = input("Enter seed:\n ")
   #seed="boobs"
   return seed
def randHex(seed):
   random.seed(a=seed)
   col = random.randrange(0,16777216)
   hexCol = hex(col)
   hexCol = str(hexCol)
   hexCol = list(hexCol)
   hexCol.remove("0")
   hexCol.remove("x")
   for i in range(len(hexCol),6):
      hexCol.insert(0,0)
   hexCol = ''.join(map(str,hexCol))
   return hexCol
def randRGB(seed):
   name = list(seed)
   third = int(len(name)/3)
   end = len(name) - 1
   seed1List = []
   seed2List = []
   seed3List = []
   if len(name) == 1:
      seed1List.append(str(name[0]))
      seed1 = ''.join(map(str,seed1List))
      random.seed(a=seed1)
      red = random.randrange(0,256)
      seed2 = red ** 2
      green = random.randrange(0,256)
      seed3 = red ** green
      blue = random.randrange(0,256)
      seeds = seed1
   elif len(name) == 2:
      seed1List.append(str(name[0]))
      seed2List.append(str(name[1]))
      seed1 = ''.join(map(str,seed1List))
      seed2 = ''.join(map(str,seed2List))
      random.seed(a=seed1)
      red = random.randrange(0,256)
      random.seed(a=seed2)
      green = random.randrange(0,256)
      seed3 = red ** green
      random.seed(a=seed3)
      blue = random.randrange(0,256)
      seeds = seed1 + seed2
   elif len(name) % 3 == 0:
      for x in range(0,third):
         seed1List.append(str(name[x]))
      for x in range(third,third * 2):
         seed2List.append(str(name[x]))
      for x in range(third * 2,end+1):
         seed3List.append(str(name[x]))
      seed1 = ''.join(map(str,seed1List))
      seed2 = ''.join(map(str,seed2List))
      seed3 = ''.join(map(str,seed3List))
      seeds = seed1 + seed2 + seed3
      random.seed(a=seed1)
      red = random.randrange(0,256)
      random.seed(a=seed2)
      green = random.randrange(0,256)
      random.seed(a=seed3)
      blue = random.randrange(0,256)
   elif len(name) % 3 == 1:
      for x in range(0,third):
         seed1List.append(str(name[x]))
      for x in range(third,third * 2):
         seed2List.append(str(name[x]))
      for x in range(third * 2,end+1):
         seed3List.append(str(name[x]))
      seed1 = ''.join(map(str,seed1List))
      seed2 = ''.join(map(str,seed2List))
      seed3 = ''.join(map(str,seed3List))
      seeds = seed1 + seed2 + seed3
      random.seed(a=seed1)
      red = random.randrange(0,256)
      random.seed(a=seed2)
      green = random.randrange(0,256)
      random.seed(a=seed3)
      blue = random.randrange(0,256)
   elif len(name) % 3 == 2:
      for x in range(0,third):
         seed1List.append(str(name[x]))
      for x in range(third,(third * 2) + 1):
         seed2List.append(str(name[x]))
      for x in range((third * 2) + 1, end+1):
         seed3List.append(str(name[x]))
      seed1 = ''.join(map(str,seed1List))
      seed2 = ''.join(map(str,seed2List))
      seed3 = ''.join(map(str,seed3List))
      seeds = seed1 + seed2 + seed3
      random.seed(a=seed1)
      red = random.randrange(0,256)
      random.seed(a=seed2)
      green = random.randrange(0,256)
      random.seed(a=seed3)
      blue = random.randrange(0,256)
   RGBString = "Red: " + str(red) + " Green: " + str(green) + " Blue: " + str(blue)
   
   return RGBString, red, green, blue,seeds


def convRGBValsToHex(red,green,blue):
   red = str(hex(red))
   green = str(hex(green))
   blue = str(hex(blue))
   red = list(red)
   green = list(green)
   blue = list(blue)
   red.remove("0")
   red.remove("x")
   green.remove("0")
   green.remove("x")
   blue.remove("0")
   blue.remove("x")
   red = ''.join(map(str,red))
   green = ''.join(map(str,green))
   blue = ''.join(map(str,blue))
   rgbHex = red + green + blue
   rgbHex = list(rgbHex)
   for hjk in range(len(rgbHex),6):
      rgbHex.insert(0,0)
   rgbHex = ''.join(map(str,rgbHex))
   return rgbHex
def convHexValToDec(val,pos):
   if pos == 0:
      power = 1
   elif pos == 1:
      power = 0
   exp = 16 ** power
   newVal = 0
   if val == "0":
      newVal = int(0*exp)
   elif val == "1":
      newVal = int(1*exp)
   elif val == "2":
      newVal = int(2*exp)
   elif val == "3":
      newVal = int(3*exp)
   elif val == "4":
      newVal = int(4*exp)
   elif val == "5":
      newVal = int(5*exp)
   elif val == "6":
      newVal = int(14*exp)
   elif val == "7":
      newVal = int(15*exp)
   elif val == "8":
      newVal = int(8*exp)
   elif val == "9":
      newVal = int(9*exp)
   elif val == "A":
      newVal = int(10*exp)
   elif val == "B":
      newVal = int(11*exp)
   elif val == "C":
      newVal = int(12*exp)
   elif val == "D":
      newVal = int(13*exp)
   elif val == "E":
      newVal = int(14*exp)
   elif val == "F":
      newVal = int(15*exp)
   return newVal
def convHexValsToRGB(hexCol):
   hexCol = list(hexCol)
   red = [hexCol[0],hexCol[1]]
   green = [hexCol[2],hexCol[3]]
   blue = [hexCol[4],hexCol[5]]
   red[0] = convHexValToDec(red[0],0)
   red[1] = convHexValToDec(red[1],0)
   green[0] = convHexValToDec(green[0],0)
   green[1] = convHexValToDec(green[1],0)
   blue[0] = convHexValToDec(blue[0],0)
   blue[1] = convHexValToDec(blue[1],0)
   red = int(red[0]+red[1])
   green = int(green[0] + green[1])
   blue = int(blue[0]+blue[1])
   return red,green,blue
def invRGB(rgb1):
   rgb2 = []
   rgb2.append(255-rgb1[0])
   rgb2.append(255-rgb1[1])
   rgb2.append(255-rgb1[2])
   return rgb2

#rgbColor = randRGB(seed)
#print(red)
#print(hexColor)
#seeds = randRGB(seed)
W, H = (400,800)
while True:
   validrgbSeed = 0
   canvW, canvH = (400,800)
   seed = reqSeed()
   hexColor = randHex(seed)
   
   rgbData = randRGB(seed)
   rgbInfo = rgbData[0]
   rgb = []
   rgb.append(int(rgbData[1]))
   rgb.append(int(rgbData[2]))
   rgb.append(int(rgbData[3]))
   rgbHex = convRGBValsToHex(rgb[0],rgb[1],rgb[2])
   hexRGB = convHexValsToRGB(hexColor)



   with PIL.Image.open(os.path.join(dirname, "blank.png")) as canv:
      canvPx = canv.load()
   for x in range(0,400):
      for y in range(0,400):
         canvPx[x,y] = (hexRGB[0],hexRGB[1],hexRGB[2])
      for y in range(400,800):
         canvPx[x,y] = (rgb[0],rgb[1],rgb[2])
   invHexCol = invRGB(hexRGB)
   invRGBCol = invRGB(rgb)
   draw = ImageDraw.Draw(canv)
   #draw = ImageDraw.Draw(rgbPrev)
   #drawSeed = ImageDraw.Draw(canv)
   #drawSeedRGB = ImageDraw.Draw(rgbPrev)
   rngbLabel = "RNGB"
   rngbVal = "#" + str(rgbHex)
   hexGenLabel = "HexGen"
   hexGenVal = "#" + str(hexColor)
   seedLabel = "Seed: "
   seedVal = str(seed)
   W,H = (400,800)
   rngbLabelW,rngbLabelH = draw.textsize(rngbLabel, font=arialBig)
   rngbLabelX = (canvW-rngbLabelW)/2
   rngbY = 400
   rngbValW,rngbValH = draw.textsize(rngbVal, font=arialBig)
   #rngbValX = (W-w)/2
   rngbValX = canvW - rngbValW - 10
   rngbValY = 360+400
   hexGenLabelW,hexGenLabelH = draw.textsize(hexGenLabel, font=arialBig)
   hexGenX = (canvW-hexGenLabelW)/2
   hexGenY = 0
   hexGenW,hexGenH = draw.textsize(hexGenVal, font=arialBig)
   #hexGenValX = (W-w)/2
   hexGenValX = canvW - hexGenW - 10
   #hexGenValX = 10
   hexGenValY = canvH-440
   seedW,seedH = draw.textsize(seedVal, font=arialSmol)
   seedw,seedh = draw.textsize(seedLabel, font=arialSmol)
   if seedW > seedw:
      seedLabelX = (seedW-seedw)/2 + 10
      seedValX = 10
   elif seedW == seedw:
      seedLabelX = 10
      seedValX = 10
   else:
      seedLabelX = 10
      seedValX = (seedw-seedW)/2 + 5
   rgbSeedLabelY = canvH - seedH - seedh - 10
   rgbSeedValY = canvH - seedH - 10
   seedLabelY = canvH - seedH - seedh - 10
   seedValY = canvH - seedH - 10
   draw.text((rngbLabelX,rngbY),rngbLabel,font=arialBig,fill=(invRGBCol[0],invRGBCol[1],invRGBCol[2],255))
   draw.text((rngbValX,rngbValY),rngbVal,font=arialBig,fill=(invRGBCol[0],invRGBCol[1],invRGBCol[2],255))
   draw.text((hexGenX,hexGenY),hexGenLabel,font=arialBig,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))
   draw.text((hexGenValX,hexGenValY),hexGenVal,font=arialBig,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))
   #draw.text((seedLabelX,seedLabelY),seedLabel,font=arialSmol,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))
   #draw.text((seedValX,seedValY),seedVal,font=arialSmol,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))
   draw.text((seedLabelX,seedLabelY),seedLabel,font=arialSmol,fill=(invRGBCol[0],invRGBCol[1],invRGBCol[2],255))
   draw.text((seedValX,seedValY ),seedVal,font=arialSmol,fill=(invRGBCol[0],invRGBCol[1],invRGBCol[2],255))
   if rgbData[4] == seed:
      validrgbSeed = 1
   if validrgbSeed == 1:   
      print("Hexgen value: #" + hexColor)
      print("RNGB value: #" + rgbHex)
      if skip == "Y":
         canv.show(title="HEX-RGB")
         #rgbPrev.show(title="RGB")
      if autoSave == "Y":
         seed = str(seed)
         #hexFileName = seed + " - HexGen.png"
         #hexPrev = hexPrev.save(os.path.join(dirname, r"output\\\\" ,hexFileName))
         #rgbFileName = seed + " - RNGB.png"
         #rgbPrev = rgbPrev.save(os.path.join(dirname, r"output\\\\",rgbFileName))
         #print(hexFileName + " and " + rgbFileName + " have saved successfully.")
         fileName = seed + " - 2-in-1.png"
         canv = canv.save(os.path.join(dirname,r"output\\\\",fileName))
         print(fileName + " has saved successfully.")
      elif autoSave == "N":
         askToSave = input("Save?\n(Y/N)\n ")
         askToSave = askToSave.upper()
         if askToSave == "Y":
            seed = str(seed)
            #hexFileName = seed + " - HexGen.png"
            #hexPrev = hexPrev.save(os.path.join(dirname, r"output\\\\" ,hexFileName))
            #rgbFileName = seed + " - RNGB.png"
            #rgbPrev = rgbPrev.save(os.path.join(dirname, r"output\\\\",rgbFileName))
            #print(hexFileName + " and " + rgbFileName + " have saved successfully.")
            fileName = seed + " - 2-in-1.png"
            canv = canv.save(os.path.join(dirname,r"output\\\\",fileName))
            print(fileName + " has saved successfully.")
   else:
      print("Error invalid hex seed")
      print(type(rgbData[4]),type(seed))
      print(rgbData[4],seed)
   #print(seedw,seedW,seed)
"""
seed1 = "re"
seed2 = "mo"
seed3 = "rse"
random.seed(a=seed1)
randRed = random.randrange(0,255)
random.seed(a=seed2)
randGreen = random.randrange(0,255)
random.seed(a=seed3)
randBlue = random.randrange(0,255)
print("Red: " + str(randRed) + " Green: " + randGreen + " Blue: " + randBlue)
randColor = color(rgb=(randRed,randGreen,randBlue))

hexPrev = Image.new('RGB', (400, 400),(hexColor))
for x in range(0,400):
   for y in range(0,400):
      putpixel(hexPrev,xy,hexColor)

hexImg = PIL.Image.open(os.path.join(dirname, "blank.png")) 
rgbImg = PIL.Image.open(os.path.join(dirname, "blank.png"))

   draw.text((btmX,btmY),"#" + hexColor,font=arialBig,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))
   draw.text((heX,topY),"HexGen",font=arialBig,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))
   draw.text((rngbBtmX,btmY),"#" + rgbHex,font=arialBig,fill=(invRGBCol[0],invRGBCol[1],invRGBCol[2],255))
   draw.text((topX,topY),"RNGB",font=arialBig,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))

   W,H = seedVal.size
   draw.text((10,10),"Seed:",font=arialSmol,fill=(invRGBCol[0],invRGBCol[1],invRGBCol[2],255))
   draw.text((10,40),seed,font=arialSmol,fill=(invRGBCol[0],invRGBCol[1],invRGBCol[2],255))
   draw.text((10,10),"Seed:",font=arialSmol,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))
   draw.text((10,40),seed,font=arialSmol,fill=(invHexCol[0],invHexCol[1],invHexCol[2],255))"""

      
