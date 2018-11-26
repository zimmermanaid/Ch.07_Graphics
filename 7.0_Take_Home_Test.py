'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________


In the comment above each line of code explain what the code does.
'''

# 1.
import arcade



# 2.
arcade.open_window(500, 400, "Take Home Test")



# 3.                                                 *Also, rewrite using RGB instead
arcade.set_background_color(arcade.color.ALMOND)




# 4.
arcade.start_render()




# 5. What's the difference between the following two lines of code?
#
arcade.draw_lrtb_rectangle_filled(6, 34, 589, 571, arcade.color.BLUSH)
#
arcade.draw_rectangle_filled(200, 520, 45, 25, arcade.color.BLUSH, 45)




# 6.
arcade.draw_point(50, 580, arcade.color.RED, 5)




# 7.
arcade.draw_line(75, 590, 95, 570, arcade.color.BLACK, 2)




# 8.
arcade.draw_circle_filled(190, 580, 18, arcade.color.WISTERIA)





# 9.
arcade.draw_ellipse_filled(240, 580, 30, 15, arcade.color.AMBER)





# 10.
arcade.draw_text("I love you. I know.", 10, 450, arcade.color.BRICK_RED, 20)




# 11. Research draw_arc_filled and with one line of code create a PAC-MAN.




# 12.
arcade.finish_render()



# 13.
arcade.run()

