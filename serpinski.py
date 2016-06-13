import turtle


def draw_triangle(painter, position):
    painter.penup()
    painter.setpos(position[0][0], position[0][1])
    painter.pendown()
    painter.setpos(position[1][0], position[1][1])
    painter.setpos(position[2][0], position[2][1])
    painter.setpos(position[0][0], position[0][1])


def half_triangle(one, two):
    new_x = (one[0] + two[0]) / 2
    new_y = (one[1] + two[1]) / 2
    return new_x, new_y


def serp_algorithm(position, depth, painter):
    draw_triangle(painter, position)
    if depth != 0:
        serp_algorithm([position[0],
                        half_triangle(position[0], position[1]),
                        half_triangle(position[0], position[2])],
                       depth - 1, painter)

        serp_algorithm([position[1],
                        half_triangle(position[0], position[1]),
                        half_triangle(position[1], position[2])],
                       depth - 1, painter)

        serp_algorithm([position[2],
                        half_triangle(position[2], position[1]),
                        half_triangle(position[0], position[2])],
                       depth - 1, painter)


def main():
    painter = turtle.Turtle()
    painter.speed(12)
    position = [[-400, -300], [0, 300], [400, -300]]
    depth = raw_input("Input depth of triangle ")
    depth = int(depth)
    serp_algorithm(position, depth, painter)

main()
turtle.done()
