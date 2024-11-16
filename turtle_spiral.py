import turtle

a = turtle.Turtle()

screen = a.getscreen()

running = True

north = 90
east = 0
south = 270
west = 180

move_distance = 0
distance_between = 0.0001
angle = 5

turtle.speed = 0


while running:

    move_distance = move_distance + distance_between
    a.forward(move_distance)
    a.right(angle)
    a.forward(move_distance)
    a.right(angle)
   
    





   





input("asdfasdf")