"""Drawing a pattern using fractals
Developer: Turchinovich Maria
"""

from turtle import *
import random

speed(0)

points_for_triangle = [[[-80, 100], [0, 300], [80, 100]], [[80, 100], [295,135], [135,-20]],
                       [[135, -20], [165, -240], [0, -70]], [[0, -70], [-150, -240], [-135, -20]],
                       [[-135, -20], [-295, 135], [-80, 100]]]

colors = ['red', 'black', 'blue', '#006400', '#D2691E', '#FFFF00', '#00FFFF', '#BC8F8F',
              '#FF1493', '#FF4500', '#FF7F50', '#008080', '#808080', '#000080', '#00FFFF']

colors_for_circle = ['#000080', '#000000', '#2F4F4F', '#006400', '#8B0000', '#CD5C5C', '#FF4500', '#A0522D']

def middle(point_1, point_2):
    """Division of coordinates for triangles"""
    return ((point_1[0] + point_2[0]) / 2, (point_1[1] + point_2[1]) / 2)

def triangle(points, depth):
    """Drawing a triangle"""
    up()
    goto(points[0][0], points[0][1])
    down()
    goto(points[1][0], points[1][1])
    goto(points[2][0], points[2][1])
    goto(points[0][0], points[0][1])

    if depth == 0:
        return

    num_color = colors[random.randint(0,14)]
    color(num_color)
    triangle([points[0], middle(points[0], points[1]), middle(points[0], points[2])], depth - 1)
    triangle([points[1], middle(points[0], points[1]), middle(points[1], points[2])], depth - 1)
    triangle([points[2], middle(points[2], points[1]), middle(points[0], points[2])], depth - 1)

def squares(num_start, num_end):
    """Drawing squares"""
    if num_start == num_end:
        return
    pensize(1)
    num_color = colors_for_circle[random.randint(0, 7)]
    color(num_color)
    circle(num_start)
    left(45)
    return squares(num_start + 0.5, num_end)

def star(start_number, number_of_lines):
    """Drawing a star"""
    if start_number == number_of_lines:
        return
    num_color = colors[random.randint(0, 14)]
    color(num_color)
    forward(start_number)
    left(190)
    star(start_number + 1, number_of_lines)

# Drawing triangles in the form of a star
for i in range(5):
    triangle(points_for_triangle[i], 5)

# Drawing a star in the center
up()
home()
goto(0, 20)
down()
star(0, 160)
points_for_circle = [[-185, 230], [185, 225], [270, -70], [0, -240], [-270, -70]]

# Drawing a circular pattern
for i in range(5):
    up()
    goto(points_for_circle[i])
    down()
    squares(0, 50)

hideturtle()
mainloop()