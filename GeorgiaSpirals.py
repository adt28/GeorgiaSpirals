"""
GeorgiaSpirals - Python Turtle
By A.D.Tejpal - 25-Mar-2021

This is a Python-Turtle program demonstrating drawing of custom
configured Georgia Spirals. wiith color animation.

The user has the option to try out variations in size as well as number
of petals.
"""
import turtle as tt
import turtle_udf as tf
import sys
import time

# Create instances of  Turtle() and Screen() classes
tu1 = tt.Turtle()  # For Spiral
tu2 = tt.Turtle()  # For Overall Heading & Labels
tu3 = tt.Turtle()  # For Particulars Of Current Music Track
tu4 = tt.Turtle()  # For Current Volume Level
ts = tt.Screen()

# Following statement is needed for permitting RGB style color values
# Using Turtle() object (like tu1) instead of tt below, would attract error.
tt.colormode(255)

# Globals
isPlayOn = True
isPrevClicked = False

grpSize = 6
spiralSize = 120
colorIndexSpiral = 0
colorIndexScreen = 0
lbWidth = 114

lbAreaList = []  # Holds label coordinates (for checking mouse click)
colorListSpiral = [(0, 0, 255), (173, 216, 230),
                   (0, 0, 128), (165, 42, 42, 255), (139, 69, 19),
                   (255, 215, 0), (0, 255, 0), (176, 176, 176),
                   (240, 240, 255), (255, 52, 179), (205, 102, 0),
                   (255, 105, 180), (155, 48, 255), (255, 0, 0),
                   (255, 255, 0)]
colorCountSpiral = len(colorListSpiral)

colorListScreen = [(240, 240, 244), (208, 208, 221), (174, 174, 198),
                   (234, 235, 236), (210, 213, 215), (188, 192, 194),
                   (175, 180, 182), (235, 237, 233), (216, 220, 211),
                   (198, 203, 190), (175, 183, 164), (233, 232, 236),
                   (205, 203, 211), (180, 176, 189), (160, 155, 172),
                   (234, 234, 234)]
colorCountScreen = len(colorListScreen)

"""
# Maximize turtle window with suitable title
tf.TurtleInitialSettings(tt, "Georgia's Spirals - Python-Turtle")
"""

# Simulate turtle window to full screen
tf.TurtleInitialSettings(tt, "", isFullScreen=True)

# Set turtle screen color (first one in color list)
ts.bgcolor(colorListScreen[0])

# Set animation speed
# 0 for instantaneous, otherwise 1 (min) to 10 (max)
tu1.speed(0)
tu2.speed(0)
tu3.speed(0)
tu4.speed(0)
tu1.pensize(2)  # For Spirals

# Hide Turtles
# For un-hiding the turtles, use showturtle command like tu1.st()
tu1.ht()
tu2.ht()
tu3.ht()
tu4.ht()

# Make Labels:
lbList = [["RESUME", "green"], ["STOP", "red"],
          ["BIGGER", "black"], ["SHORTER", "black"],
          ["MORE", "black"], ["LESS", "black"], ["EXIT", "red"]]

# txtPosition=1 results in positioning the text at top left corner.
pos = tf.PositionText(tt, txtPosition=1, vMargin=105)

for s in lbList:
    tf.GoToPos(tu2, pos)
    lbAreaList.append(tf.MakeLabel(tu2, txtString=s[0], 
                 txtAlign="center", fontColor=s[1],
                 fontName="Times New Roman",
                 fontSize=14, fontWt="bold",
                  labelWd=lbWidth, labelHt=30,
                  borderThickness=4, borderColor="blue", topMargin=11))

    pos = (pos[0], pos[1] - 50)

# Main Heading - Below The Last Label
pos = (pos[0] + 75, pos[1] - 65)
tf.GoToPos(tu2, pos)
tf.ShowText(tu2, "Georgia's",
            txtAlign="center", fontColor="blue",
            fontSize=28, fontWt="bold")

pos = (pos[0], pos[1] - 40)
tf.GoToPos(tu2, pos)
tf.ShowText(tu2, "Spirals",
            txtAlign="center", fontColor="blue",
            fontSize=28, fontWt="bold")

#==========Function Code Block-Start=======
def ShowStatus():
    """
    Displays the Spiral Size & Group Size
    """
    global grpSize, spiralSize

    tu3.clear()
    
    # Update Group Size
    pos = tf.PositionText(tt, txtPosition=1, vMargin=37)
    tf.GoToPos(tu3, pos)
    tf.ShowText(tu3, "Group Size: " + str(grpSize), 
                txtAlign="left", fontColor="black", fontSize=14)

    # Update Speed Level Display
    pos = (pos[0], pos[1] - 25)
    tf.GoToPos(tu3, pos)
    tf.ShowText(tu3, "Spiral Size: " + str(spiralSize), 
                txtAlign="left", fontColor="black", fontSize=14)

def DrawCircles(TurtleObject, 
                cRed=0, cGreen=0, cBlue=255):
    """
    For using RGB style for colors, the calling code should have
    prior statement like following:
    turtle.colormode(255)
    """
    global isPlayOn, spiralSize
    
    tu = TurtleObject

    r = spiralSize
    rMin = 0.15 * spiralSize
    rStep = 2
    clrStep = 6

    while r > rMin:
        if not isPlayOn:
            break
        
        tu.pencolor(cRed, cGreen, cBlue)
        tu.circle(r)
        r=r-rStep

        # Progressive darkening of color in each cycle
        if cRed > (clrStep + 5):
            cRed = cRed - clrStep
        if cGreen > (clrStep + 5):
            cGreen = cGreen - clrStep
        if cBlue > (clrStep + 5):
            cBlue = cBlue - clrStep

def DrawCirclesGrp(TurtleObject, 
                   cRed=0, cGreen=0, cBlue=255):
    global isPlayOn, spiralSize, grpSize
    
    tu = TurtleObject
    for i in range (grpSize):
        if not isPlayOn:
            break
        
        DrawCircles(tu, cRed, cGreen, cBlue)
        tu.right(360/grpSize)

# Draw Georgia Spiral
def DrawGeorgiaSpiral():
    global colorIndexSpiral, colorListSpiral, colorCountSpiral
    global colorIndexScreen, colorListScreen, colorCountScreen
    global musicIndex, musicCount, mVol
    global musicListFullPaths, musicListFileNames
    global isPlayOn, spiralSize, grpSize
    """
    Apparently, global declaration is not needed for object variables.
    """
    
    while True:
        if not isPlayOn:
            # Stop music & display Stop notice
            tu3.clear()        
            pos = tf.PositionText(tt, txtPosition=1, vMargin=35)
            tf.GoToPos(tu3, pos)
            tf.ShowText(tu3,
                        "Play Stopped: Click RESUME To Start Afresh" , 
                        txtAlign="left", fontColor="red", fontSize=14)
            break
        
        # Display Status:
        ShowStatus()
        
        # Set screen color as per color list
        clr = colorListScreen[colorIndexScreen]
        ts.bgcolor(clr)
        
        # Set spiral color as per color list
        clr = colorListSpiral[colorIndexSpiral]
        rr = clr[0]
        gg = clr[1]
        bb = clr[2]
        
        DrawCirclesGrp(tu1,
                       cRed=rr, cGreen=gg, cBlue=bb)

        colorIndexSpiral = colorIndexSpiral + 1
        if colorIndexSpiral > (colorCountSpiral - 1):
            colorIndexSpiral = 0

        colorIndexScreen = colorIndexScreen + 1
        if colorIndexScreen > (colorCountScreen - 1):
            colorIndexScreen = 0

def CallSpirals():
    tu1.home()
    tu1.fd(lbWidth/2)
    tu1.clear()
    tu3.clear()
    DrawGeorgiaSpiral()

# Function for use in mouse click event
def ClickAction(x, y):
    global lbAreaList, isPlayOn
    global colorIndexSpiral, colorIndexScreen
    global colorCountSpiral, colorCountScreen
    global spiralSize, grpSize

    lbResume = lbAreaList[0]
    lbStop = lbAreaList[1]
    lbBigger = lbAreaList[2]
    lbShorter = lbAreaList[3]
    lbMore = lbAreaList[4]
    lbLess = lbAreaList[5]
    lbExit = lbAreaList[6]
    if (x in range(lbResume[0], lbResume[2]) 
                  and y in range(lbResume[3], lbResume[1])):
        if not isPlayOn:
            isPlayOn = True
            CallSpirals()

    elif (x in range(lbStop[0], lbStop[2]) 
                  and y in range(lbStop[3], lbStop[1])):
        isPlayOn = False      

    elif (x in range(lbBigger[0], lbBigger[2]) 
                  and y in range(lbBigger[3], lbBigger[1])):
        spiralSize = spiralSize + 10
        if spiralSize > 150:
            spiralSize = 150
        else:
            CallSpirals()

    elif (x in range(lbShorter[0], lbShorter[2]) 
                  and y in range(lbShorter[3], lbShorter[1])):
        if spiralSize > 50:
            spiralSize = spiralSize - 10
            CallSpirals()
        else:
            spiralSize = spiralSize - 5
            if spiralSize < 15:
                spiralSize = 15
            else:
                CallSpirals()

    elif (x in range(lbMore[0], lbMore[2]) 
                  and y in range(lbMore[3], lbMore[1])):
        grpSize = grpSize + 1
        if grpSize > 15:
            grpSize = 15
        else:
            CallSpirals()
        
    elif (x in range(lbLess[0], lbLess[2]) 
                  and y in range(lbLess[3], lbLess[1])):
        grpSize = grpSize - 1
        if grpSize < 2:
            grpSize = 2
        else:
            CallSpirals()

    elif (x in range(lbExit[0], lbExit[2]) 
                  and y in range(lbExit[3], lbExit[1])):
        if isPlayOn:
            isPlayOn = False
            tu4.clear()

            pos =(lbExit[2] + 10, lbExit[3])
            tf.GoToPos(tu4, pos)
            tf.ShowText(tu4,
                        "Please Click Exit Again" , 
                        txtAlign="left", fontColor="red", fontSize=14)

        else:
            time.sleep(1)  # Prevents trce-back error messages on python shell
            # Close turtle window
            ts.bye()
            sys.exit()

#==========Function Code Block-End========

# Call function ClickAction() on mouse click
# (Use of tt (i.e. turtle) or tu (i.e. turtle.Turtle())
# instead of ts (turtle.Screen()) would cause error)
ts.onclick(ClickAction)  # (A)

"""
Imp:  Line (B) below, meant for drawing the spirals
has to AFTER the mouse-click event line (A) above.
If (B) is placed before (A), the mouse click event stops responding
"""
DrawGeorgiaSpiral()

# mainloop() tells the window to wait for the user to do something
# It serves to prevent automatic disappearance of turtle window
# (when run in other than IDLEX) immediately after execution.
tt.mainloop()

"""
The statement below also serves to prevent automatic disappearance of turtle window immediately after execution.
However, tt.mainloop() is preferred in this module as mouse click event is needed otherwise.
tt.exitonclick()

Note: Code for a function should precede the calling code
"""
