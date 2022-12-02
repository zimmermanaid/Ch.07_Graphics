'''
PYCASSO PROJECT
---------------
Your job is to make a cool picture.
You must use multiple colors.
You must have a coherent picture. No abstract art with random shapes.
You must use multiple types of graphic functions (e.g. circles, rectangles, lines, etc.)
Somewhere you must include a WHILE or FOR loop to create a repeating pattern.
Do not just redraw the same thing in the same location 10 times. 
You can contain multiple drawing commands in a loop, so you can draw multiple train cars for example.
Please use comments and blank lines to make it easy to follow your program. 
If you have 5 lines that draw a robot, group them together with blank lines above and below. 
Then add a comment at the top telling the reader what you are drawing.
IN THE WINDOW TITLE PLEASE PUT YOUR NAME.
When you are finished Pull Request your file to your instructor.
'''
import arcade
import arcade
arcade.open_window (400,400)
arcade.set_background_color(arcade.color.COOL_GREY)
arcade.start_render()

#chess board
x=25
y=375
for i in range (0,4):
    for i in range(0,8):
        arcade.draw_rectangle_filled(x,y,50,50,arcade.color.ALMOND)
        x+=100
    y-=100
    x=25
x=75
y=325
for i in range (0,4):
    for i in range (0,8):
        arcade.draw_rectangle_filled(x,y,50,50,arcade.color.ALMOND)
        x+=100
    y-=100
    x=75
#chess board

    #chess pieces

#blackpawn
x=25
for i in range (0,8):
    blackPawn=arcade.load_texture("chesspieces/blackPawn.png")
    arcade.draw_texture_rectangle(x,325,blackPawn.width*.1,blackPawn.height*.1,blackPawn)
    x+=50

#whitepawn
x=25
for i in range (0,8):
    whitePawn=arcade.load_texture("chesspieces/whitePawn.png")
    arcade.draw_texture_rectangle(x,75,whitePawn.width*.12,whitePawn.height*.12,whitePawn)
    x+=50

#blackrook
x=25
for i in range (0,2):
    blackRook=arcade.load_texture("chesspieces/blackRook.png")
    arcade.draw_texture_rectangle(x,375,blackRook.width*.15,blackRook.height*.15,blackRook)
    x+=350

#whiterook
x=25
for i in range (0,2):
    whiteRook=arcade.load_texture("chesspieces/whiteRook.png")
    arcade.draw_texture_rectangle(x,25,whiteRook.width*.15,whiteRook.height*.15,whiteRook)
    x+=350

#blackknight
x=75
for i in range (0,2):
    blackKnight=arcade.load_texture("chesspieces/blackKnight.png")
    arcade.draw_texture_rectangle(x,375,blackKnight.width*.12,blackKnight.height*.12,blackKnight)
    x+=250

#whiteknight
x=75
for i in range (0,2):
    whiteKnight=arcade.load_texture("chesspieces/whiteKnight.png")
    arcade.draw_texture_rectangle(x,25,whiteKnight.width*.12,whiteKnight.height*.12,whiteKnight)
    x+=250

#blackBishop
x=125
for i in range (0,2):
    blackBishop=arcade.load_texture("chesspieces/blackBishop.png")
    arcade.draw_texture_rectangle(x,375,blackBishop.width*.17,blackBishop.height*.17,blackBishop)
    x+=150

#whiteBishop
x=125
for i in range (0,2):
    whiteBishop=arcade.load_texture("chesspieces/whiteBishop.png")
    arcade.draw_texture_rectangle(x,25,whiteBishop.width*.17,whiteBishop.height*.17,whiteBishop)
    x+=150

#blackqueen
blackQueen=arcade.load_texture("chesspieces/blackQueen.png")
arcade.draw_texture_rectangle(175,375,blackQueen.width*.17,blackQueen.height*.17,blackQueen)

#whitequeen
whiteQueen=arcade.load_texture("chesspieces/whiteQueen.png")
arcade.draw_texture_rectangle(175,25,whiteQueen.width*.17,whiteQueen.height*.17,whiteQueen)

#blackking
blackKing=arcade.load_texture("chesspieces/blackKing.png")
arcade.draw_texture_rectangle(225,375,blackKing.width*.17,blackKing.height*.17,blackKing)

#whiteking
whiteKing=arcade.load_texture("chesspieces/whiteKing.png")
arcade.draw_texture_rectangle(225,25,whiteKing.width*.17,whiteKing.height*.17,whiteKing)


arcade.finish_render()
arcade.run()