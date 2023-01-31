# face.pyw
# Drawing Andross (mechanical form) from the 1993 SNES video game Star Fox
#   by Alexandra Wonyu

from graphics import *


def main():

    win = GraphWin("Andross", 540, 720)
    win.setCoords(0,-2,18,22)
    win.setBackground("black")

    outline = [Point(6,2), Point(12,2), Point(15,5), Point(16,10), Point(16,16), Point(13,19), Point(9,20), Point(5,19), Point(2,16), Point(2,10), Point(3,5)]
    face = Polygon(outline).draw(win)
    face.setFill(color_rgb(238,229,234))

    # Left eye and surroundings (eye -> ll -> ul -> ur -> lr)
    Polygon(Point(5,13.5), Point(7.5,14), Point(5,15), Point(2.25,14)).draw(win).setFill(color_rgb(255,66,1))
    Polygon(Point(2.25,14), Point(5,12), Point(5,13.5)).draw(win).setFill(color_rgb(109,110,138))
    Polygon(Point(2.25,14), Point(5,16), Point(5,15)).draw(win).setFill(color_rgb(101,105,141))
    Polygon(Point(5,16), Point(5,15), Point(7.5,14)).draw(win).setFill(color_rgb(226,217,221))
    Polygon(Point(5,13.5), Point(5,12), Point(7.5,14)).draw(win).setFill("white")

    # Right eye and surroundings (eye -> ll -> ul -> ur -> lr)
    Polygon(Point(10.5,14), Point(13,15), Point(15.75,14), Point(13,13.5)).draw(win).setFill(color_rgb(255,66,0))
    Polygon(Point(10.5,14), Point(13,13.5), Point(13,12)).draw(win).setFill(color_rgb(165,161,177))
    Polygon(Point(10.5,14), Point(13,16), Point(13,15)).draw(win).setFill(color_rgb(140,143,171))
    Polygon(Point(13,15), Point(13,16), Point(15.75,14)).draw(win).setFill(color_rgb(213,207,219))
    Polygon(Point(13,13.5), Point(13,12), Point(15.75,14)).draw(win).setFill(color_rgb(241,232,237))

    # Sides of the eyes (ambiguous shapes)
    leftside = Polygon(Point(5,19), Point(5,16), Point(2.25,14), Point(5,12), Point(2,10), Point(2,16))
    leftside.draw(win).setFill(color_rgb(130,130,154))
    rightside = Polygon(Point(13,19), Point(13,16), Point(15.75,14), Point(13,12), Point(16,10), Point(16,16))
    rightside.draw(win).setFill(color_rgb(245,236,241))
    
    # Nose (nose -> philtrum -> bridge)
    Polygon(Point(7.5,9), Point(8.5,9.5), Point(9.5,9.5), Point(10.5,9)).draw(win).setFill(color_rgb(154,148,168))
    Polygon(Point(9,7.5), Point(10.5,9), Point(7.5,9)).draw(win).setFill(color_rgb(109,114,146))
    Rectangle(Point(8.5,9.5), Point(9.5,14.5)).draw(win).setFill(color_rgb(207,196,210))

    # Philtrum sides (left -> right)
    Polygon(Point(9,7.5), Point(7.5,9), Point(5.5,6)).draw(win).setFill(color_rgb(129,130,158))
    Polygon(Point(9,7.5), Point(10.5,9), Point(12.5,6)).draw(win).setFill(color_rgb(238,229,234))

    # Nose direct surroundings (ll -> ul -> ur -> lr)
    Polygon(Point(7.5,14), Point(8.5,9.5), Point(7.5,9)).draw(win).setFill(color_rgb(98,103,135))
    Polygon(Point(7.5,14), Point(8.5,9.5), Point(8.5,14.5)).draw(win).setFill(color_rgb(147,144,171))
    Polygon(Point(9.5,9.5), Point(10.5,14), Point(10.5,9)).draw(win).setFill(color_rgb(231,221,229))
    Polygon(Point(9.5,9.5), Point(10.5,14), Point(9.5,14.5)).draw(win).setFill(color_rgb(212,204,215))

    # Sides of the nose (left -> right)
    Polygon(Point(7.5,14), Point(7.5,9), Point(5,12)).draw(win).setFill("white")
    Polygon(Point(10.5,14), Point(10.5,9), Point(13,12)).draw(win).setFill(color_rgb(197,189,202))

    # Mouth
    Polygon(Point(9,4.5), Point(12.5,6), Point(9,7), Point(5.5,6)).draw(win).setFill("black")

    # Lips (ll -> ul -> ur -> lr)
    Polygon(Point(5.5,6), Point(9,4.5), Point(9,4)).draw(win).setFill(color_rgb(162,159,178))
    Polygon(Point(9,7.5), Point(9,7), Point(5.5,6)).draw(win).setFill(color_rgb(152,150,173))
    Polygon(Point(9,7.5), Point(9,7), Point(12.5,6)).draw(win).setFill("white")
    Polygon(Point(12.5,6), Point(9,4.5), Point(9,4)).draw(win).setFill("white")

    # Cheeks (ll -> ul -> ur -> lr)
    Polygon(Point(2,10), Point(5.5,6), Point(7.5,9)).draw(win).setFill(color_rgb(199,193,205))
    Polygon(Point(2,10), Point(7.5,9), Point(5,12)).draw(win).setFill(color_rgb(162,159,176))
    Polygon(Point(10.5,9), Point(16,10), Point(13,12)).draw(win).setFill(color_rgb(236,226,234))
    Polygon(Point(10.5,9), Point(16,10), Point(12.5,6)).draw(win).setFill(color_rgb(249,238,244))  

    # Forehead (centre -> top to bottom left -> top to bottom right)
    Polygon(Point(8.5,14.5), Point(9,20), Point(9.5,14.5)).draw(win).setFill(color_rgb(226,216,224))
    Polygon(Point(9,20), Point(5,19), Point(5,16)).draw(win).setFill(color_rgb(203,195,208))
    Polygon(Point(9,20), Point(5,16), Point(8.5,14.5)).draw(win).setFill(color_rgb(236,230,234))
    Polygon(Point(5,16), Point(7.5,14), Point(8.5,14.5)).draw(win).setFill(color_rgb(224,214,223))
    Polygon(Point(9,20), Point(13,16), Point(13,19)).draw(win).setFill(color_rgb(212,204,215))
    Polygon(Point(9,20), Point(13,16), Point(9.5,14.5)).draw(win).setFill(color_rgb(210,202,215))
    Polygon(Point(9.5,14.5), Point(13,16), Point(10.5,14)).draw(win).setFill(color_rgb(250,241,246))

    # Extended chin (left -> right)
    Polygon(Point(3,5), Point(5.5,6), Point(2,10)).draw(win).setFill(color_rgb(183,179,193))
    Polygon(Point(3,5), Point(5.5,6), Point(6,2)).draw(win).setFill(color_rgb(189,186,198))
    Polygon(Point(6,2), Point(9,4), Point(5.5,6)).draw(win).setFill(color_rgb(134,132,154))
    Polygon(Point(6,2), Point(9,4), Point(12,2)).draw(win).setFill(color_rgb(172,168,185))
    Polygon(Point(12,2), Point(9,4), Point(12.5,6)).draw(win).setFill(color_rgb(252,243,246))
    Polygon(Point(12.5,6), Point(15,5), Point(12,2)).draw(win).setFill("white")
    Polygon(Point(12.5,6), Point(15,5), Point(16,10)).draw(win).setFill("white")

    # Polygonal tiles being spat out
    cubetop = Polygon(Point(11,3), Point(13,4), Point(14,6), Point(12,5))
    cubetop.draw(win).setFill(color_rgb(197,189,202))
    cubeleft = Polygon(Point(11,3), Point(13,4), Point(13.5,3.5), Point(11.5,2.5))
    cubeleft.draw(win).setFill(color_rgb(255,65,1))
    cuberight = Polygon(Point(13,4), Point(14,6), Point(14.5,5.5), Point(13.5,3.5))
    cuberight.draw(win).setFill(color_rgb(255,65,1))
    
    for i in range(2):
        cubetop = cubetop.clone().draw(win)
        cubetop.move(3,-1)
        cubeleft = cubeleft.clone().draw(win)
        cubeleft.move(3,-1)
        cuberight = cuberight.clone().draw(win)
        cuberight.move(3,-1)

    # Name
    Andross = Text(Point(9, 0.5), "Andross").draw(win)
    Andross.setTextColor(color_rgb(255,65,1))
    Andross.setSize(25)
    Andross.setStyle("bold")

    win.getMouse()
    win.close()
    
main()
