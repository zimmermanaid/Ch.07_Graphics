#Sign your name:________________

'''
Recreate, exactly the Test Picture from the website. The arcade colors used in this picture in no particular order are:
BLACK, ALMOND, PHLOX, BLUSH, RED, BLUE, WISTERIA, AMBER, BRICK_RED and YELLOW.
The picture is 500px wide and 400px tall. Look up ARC in the documentation to do the PAC-MAN.
'''

import arcade

#window
arcade.open_window (500,400,"My Drawing")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()
y=400
x=0
for horizontal in range (0,501,20):
    arcade.draw_line(0,y,500,y,(0,0,0),1)
    y-=20
for vertical in range (0,501,20):
    arcade.draw_line(x,0,x,400,(0,0,0),1)
    x+=20
arcade.draw_circle_filled(250,200,40,arcade.color.WISTERIA)
arcade.draw_rectangle_filled(50,370,60,20,arcade.color.PHLOX)
arcade.draw_rectangle_filled(200,260,40,20,arcade.color.BLUSH,135)
arcade.draw_text("I love you. I know.",20,160,arcade.color.BRICK_RED,20,2)
arcade.draw_line(80,20,120,60,arcade.color.BLUE)
arcade.draw_ellipse_filled(100,100,120,40,arcade.color.AMBER)
arcade.draw_rectangle_filled(460,10,5,5,arcade.color.RED)
arcade.draw_arc_filled(400,320,120,120,arcade.color.YELLOW,30,330)

#arcade stuff
arcade.finish_render()
arcade.run()