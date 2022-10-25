import arcade

student_file = open("student_file.txt", "r")
all_lines = student_file.readlines()


myWindow = arcade.open_window(800, 800,  'project 4')
arcade.set_background_color(arcade.color.GRAY)
arcade. start_render()
arcade.draw_line( 160,160,160, 800 , arcade.color.GREEN)
current_y = 160
current_x = 160
scale_y = (800 - 160) / len(range(100, 1500, 100))
scale_x = (800 - 160) / len(all_lines)
arcade.draw_line(160,160,800,160,arcade.color.WHITE)
for i in range (100,1500, 100):
    currentLabel = arcade.Text(f'{i}M', 100, current_y)
    currentLabel.draw()
    current_y += scale_y
for country_file in all_lines:
    split_lines = country_file.split(",")
    currentLabel = arcade.Text(split_lines[0], current_x + scale_x/2, 150)
    currentLabel.rotation = -90;
    currentLabel.draw()
    pop = int(split_lines[1])
    color = arcade.color.WHITE
    if(float(split_lines[2]) < 0):
        color = arcade.color.RED
    else:
        color = arcade.color.GREEN
    arcade.draw_xywh_rectangle_filled(current_x + scale_x/4, 160, scale_x - 10, (pop / 1_400_000_000) * (800-200), color)

    print(f'{split_lines[0]} {split_lines[2]} ')
    current_x += scale_x

arcade.finish_render()
arcade.run()