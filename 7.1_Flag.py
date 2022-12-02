'''
FLAG PROJECT
---------------
Make your flag 260 pixels tall
Use the scaling image on the website to determine other dimensions
The hexadecimal colors for the official flag are red: #BF0A30 and blue: #002868
Title the window, "The Stars and Stripes"
You can use a draw_text command and used 20 pt. asterisks for the stars.
We will have a competition to see who can make this flag in the least lines of code.
The record is 16! You will have to use some loops to achieve this.
CHALLENGE: Can you make the entire flag parametrically? This means if I change the hoist to 520px the flag will resize accordingly.
'''
import arcade
arcade.open_window (500,260)
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

#stripes
y=250
for i in range (0,260,20):
    arcade.draw_rectangle_filled(200,y,600,20,(191,10,48))
    y-=40

arcade.draw_rectangle_filled(100,190,210,140,(0,40,104)) #blue part

#first list stars
x=10
y=230
for h in range(0,5):
    for z in range (0,6):
        arcade.draw_text("*",x,y,arcade.color.WHITE,25)
        x+=34
    y-=28
    x=10

#second list stars
x=27
y=216
for t in range (0,4):
    for p in range (0,5):
        arcade.draw_text("*",x,y, arcade.color.WHITE, 25)
        x += 34
    y-=28
    x=27


arcade.finish_render()
arcade.run()