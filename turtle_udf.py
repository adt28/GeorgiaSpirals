"""
User Defined Functions For Turtle:
Some of the colors available in turtle are:
yellow, gold, orange, red, maroon, violet, magenta, purple, navy,
blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen,
chocolate, brown, black, gray, white, purple etc
"""
#import pygame as pg
#import Pg_UDF as pu  # User Defined Functions
import os, sys
import math
import random
##import time

# Set Up turtle window to max size or full screen simulation as desired
def TurtleInitialSettings(turtleModule,
    windowTitle="Python-Tutle", isFullScreen=False):
    
    # Set turtle window to full size
    # Using tu (turtle.Turtle()) instead of tt (turtle) in statement below will cause error
    turtleModule.setup(1.0, 1.0)
    
    if isFullScreen:
        # Simulate full screen, by removing close,minimize,maximize buttons:
        cnv  = turtleModule.getcanvas()
        root = cnv.winfo_toplevel()
        root.overrideredirect(1)
    else:
        # Set turtle window Title
        turtleModule.title(windowTitle)    

# Color List
# Imp: In turtle, precede by setting the colormode as follows:
# turtle.colormode(255)
def ColorListRGB():
    return [
    (0, 0, 0, 255) ,
    (0, 0, 255, 255) ,
    (173, 216, 230, 255) ,
    (0, 0, 128, 255),
    (165, 42, 42, 255) ,
    (139, 69, 19, 255) ,
    (255, 215, 0, 255) ,
    (0, 255, 0, 255) ,
    (176, 176, 176, 255) ,
    (240, 240, 255, 255) ,
    (255, 52, 179, 255) ,
    (205, 102, 0, 255) ,
    (255, 105, 180, 255) ,
    (155, 48, 255, 255) ,
    (255, 0, 0, 255) ,
    (255, 255, 0, 255)]

# Color Dictionary
# Imp: In turtle, precede by setting the colormode as follows:
# turtle.colormode(255)
def ColorDict():
    return {
    'black' : (0, 0, 0, 255),
    'blue' : (0, 0, 255, 255),
    'lightblue' : (173, 216, 230, 255),
    'navyblue' : (0, 0, 128, 255), 
    'brown' : (165, 42, 42, 255),
    'chocolate' : (139, 69, 19, 255),
    'gold' : (255, 215, 0, 255),
    'green' : (0, 255, 0, 255),
    'grey' : (176, 176, 176, 255),
    'greyish' : (240, 240, 255, 255),
    'maroon' : (255, 52, 179, 255),
    'orange' : (205, 102, 0, 255),
    'pink' : (255, 105, 180, 255),
    'purple' : (155, 48, 255, 255),
    'red' : (255, 0, 0, 255),
    'yellow' : (255, 255, 0, 255)
}

# Move to a new random location (Absolute) on screen
def NewRandLoc(TurtleObject, xMin=-300, xMax=300,
               yMin=-200, yMax=200):
    tu = TurtleObject
    tu.pu()  # Pen Up
    x = random.randint(xMin, xMax)
    y = random.randint(yMin, yMax)
    tu.goto(x,y)
    tu.pd()  # Pen Dn

# Draw a Star
def drawStar(TurtleObject, size, segments, drawColor, fillColor=""):
    tu = TurtleObject
    tu.color(drawColor, fillColor)

    # The value of segments should be such that 360 is exactly divisible by it.
    starAngle = 360//segments
    stepAngle = 180-starAngle
    segments = 360//starAngle

    if len(fillColor) > 0:
        tu.begin_fill()
    for num in range (segments):
         tu.fd(size)
         tu.rt(stepAngle)

    if len(fillColor) > 0:
        tu.end_fill()

# Draw Star Group
def drawStarGrp(TurtleObject,
                colorList=["white", "red", "green", "purple",
                           "orange", "chocolate", "yellow", "brown"]):   

    tu = TurtleObject

    # Top index for color list
    ct = len(colorList) - 1
    # Random start position in color list
    cr = random.randint(0, ct)

    GrpSizeMax = ct + 1
    GrpSizeMin = GrpSizeMax // 2
    #GrpSize = random.randint(GrpSizeMin, GrpSizeMax)
    GrpSize = GrpSizeMax

    #print("GrpSize: ", GrpSize)
    for n in range(GrpSize):
        if n > 0:
            NewRandLoc(tu)
            
        clr = colorList[cr]
        size = random.randint(20, 40)
        segments = random.randint(10, 20)
        drawStar(tu, size, segments, clr)
        
        size = random.randint(100, 300)
        segments = random.randint(30, 60)
        drawStar(tu, size, segments, clr)
        #print(clr)

        cr = cr + 1
        if cr > ct:
            cr = 0

# Position Text
def PositionText(turtleModule, txtPosition=2,
                 sMargin=10, vMargin=60):
    """
    Positions:
    1 (Top Left), 2 (Top Center), 3 (Top Right)
    4 (Bottom Left), 5 (Bottom Center), 6 (Bottom Right)
    7 (Center Screen)
    """
    tt = turtleModule    
    
    # Screen Width & Height obtained via turtle.screensize() function
    # represent the x & y dimensions w.r.t. centre point of screen (0, 0)
    # Overall screen width & height are therefore double these values.
    sWd = tt.screensize()[0]
    sHt = tt.screensize()[1]
    dX = sWd - sMargin
    dY = sHt - vMargin

    dictPosX = {1:-dX, 2:0, 3:dX, 4:-dX, 5:0, 6:dX, 7:0}
    dictPosY = {1:dY, 2:dY, 3:dY, 4:-dY, 5:-dY, 6:-dY, 7:0}

    # Make sure the value of txtPosition is from 1 o 7 (Otherwise 2)
    if not txtPosition in range(1, 8):
        txtPosition = 2

    return (dictPosX[txtPosition], dictPosY[txtPosition])      

def GoToPos(TurtleObject, pos=(0, 0)):
    tu = TurtleObject
    tu.pu()
    tu.goto(pos)
    tu.pd()

# Show Text
def ShowText(TurtleObject, txtString="Turtle Graphics", 
             txtAlign="center", fontColor="black",
             fontName="Times New Roman",
             fontSize=32, fontWt="bold"):
    tu = TurtleObject
    tu.color(fontColor)
    fstyle = (fontName, fontSize, fontWt)
    tu.write(txtString, font=fstyle, align=txtAlign)
    tu.hideturtle()

def MakeLabel(TurtleObject, txtString="Test Label", 
             txtAlign="center", fontColor="black",
             fontName="Times New Roman",
             fontSize=32, fontWt="bold",
              labelWd=100, labelHt=40, borderThickness=2,
              borderColor="blue", fillColor="",
              sideMargin=10, topMargin=10):
    """
    Returns a list [x1, y1, x2, y2] showing the coordinates
    of top left & bottom right corners of label
    """
    tu = TurtleObject
    # Top left corner:
    x1 = 0
    y1 = 0
    # Bottom right corner:
    x2 = 0
    y2 = 0
##    # List having label coordinates:
##    lbPosList = []
    
    # Get original size & color for Turtle object
    ps1 = tu.pensize()
    clr1 = tu.color()

    tu.pensize(borderThickness)
    tu.color(borderColor)
    for n in range(4):
        if n%2 == 0:
            s = labelWd
        else:
            s = labelHt

        tu.fd(s)
        tu.rt(90)

    # Show Text
    pos = tu.position()
    x1 = pos[0]
    y1 = pos[1]
    x2 = x1 + labelWd
    y2 = y1 - labelHt
    #posY = pos[1] - (labelHt/2) - topMargin
    posY = y1 - (labelHt/2) - topMargin
    if txtAlign == "left":
        #posX = pos[0] + sideMargin
        posX = x1 + sideMargin
    elif txtAlign == "right":
        #posX = pos[0] + labelWd - sideMargin
        posX = x1 + labelWd - sideMargin
    else:
        #posX = pos[0] + labelWd/2
        posX = x1 + labelWd/2

    pos = (posX, posY)
    GoToPos(tu, pos)
    ShowText(tu, txtString, txtAlign, fontColor,
             fontName, fontSize, fontWt)
    
    # Restore original size & color for Turtle object
    tu.pensize(ps1)
    tu.color(clr1[0], clr1[1])

    # x1, y1, x2, y2 are float values.
    # These are converted to integers to suit later use in range() function
    return [int(x1), int(y1), int(x2), int(y2)]

def DrawRectangle(TurtleObject, wd=100,
                  ht=40, thick=2, clr="black"):
    tu = TurtleObject

    # Get original size & color for Turtle object
    ps1 = tu.pensize()
    clr1 = tu.color()

    tu.pensize(thick)
    tu.color(clr)
    for n in range(4):
        if n%2 == 0:
            s = wd
        else:
            s = ht

        tu.fd(s)
        tu.rt(90)

    # Restore original size & color for Turtle object
    tu.pensize(ps1)
    tu.color(clr1[0], clr1[1])

def GetDir(data_folder="data"):
    # os.path.split(os.path.abspath(__file__)) returns a tuple,
    # having folder path & this file's name as its elements.
    # main_dir as first element of this tuple, stands for folder path.
    main_dir = os.path.split(os.path.abspath(__file__))[0]
    # folder named "data" is located in the folder holding this
    # code file. data_dir thus represents path of data folder.
    # It is equivalent to: main_dir + "\data"
    # data_dir holds images & sounds needed for our program
    data_dir = os.path.join(main_dir, data_folder)
    return [main_dir, data_dir]

def GetFilePath(datafolder_name, file_name):
    data_dir = GetDir(datafolder_name)[1]
    return os.path.join(data_dir, file_name)

def GetFileList(folderName, fileExtn=""):
    path = GetDir(folderName)[1]
    """
    Returns a list consisting of 2 elements.
    The first element is a list of full paths for the files.
    The second element is a list of file names only.
    """

    fileList = []
    fileListFullPath = []
    fileListFileNames = []
    # r=root, dd=directories (incl subdirectories if any), ff = files
    for r, dd, ff in os.walk(path):
        for f in ff:
            if len(fileExtn) > 0:
                if fileExtn in f:
                    fileListFullPath.append(os.path.join(r, f))
                    fileListFileNames.append(f)
            else:
                fileListFullPath.append(os.path.join(r, f))
                fileListFileNames.append(f)

    fileList.append(fileListFullPath)
    fileList.append(fileListFileNames)
    
    return fileList

def LoadPlayMusic(pygameModule, datafolder_name,
                  file_name, m_vol=0.4, loop=True):
    pg = pygameModule
    file_path = GetFilePath(datafolder_name, file_name)
    pg.mixer.music.load(file_path)

    if loop:
        pg.mixer.music.play(-1)
    else:
        pg.mixer.music.set_endevent(
            pg.constants.USEREVENT)
        pg.mixer.music.play()
    
    pg.mixer.music.set_volume(m_vol)

def LoadPlayMusic_A(pygameModule, musicFileFullPath,
                    mVol=0.4, loop=True):
    pg = pygameModule
    pg.mixer.music.load(musicFileFullPath)

    if loop:
        pg.mixer.music.play(-1)
    else:
        pg.mixer.music.set_endevent(
            pg.constants.USEREVENT)
        pg.mixer.music.play()
    
    pg.mixer.music.set_volume(mVol)

def RandomColor_255(turtleModule):
    # Multiplying factors of 0.9, 0.5 & 0.7 - to ensure darker colors
    turtleModule.colormode(255)
    return (0.9*random.randrange(255),
            0.5*random.randrange(255),
            0.7*random.randrange(255))

def RandomColor_1(turtleModule):
    # Multiplying factors of 0.9, 0.5 & 0.7 - to ensure darker colors
    turtleModule.colormode(1.0)
    return (0.9*random.randrange(1000)/1000,
            0.5*random.randrange(1000)/1000,
            0.7*random.randrange(1000)/1000)
