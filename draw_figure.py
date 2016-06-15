import turtle

painter = turtle.Turtle()


def set_figure():
    figures = {
        '1': draw_triangle,
        '2': draw_square,
        '3': draw_circle,
        '4': draw_star,
        '5': draw_ninja_circle,
        '6': draw_spiral,
        '7': 'grey',
        '8': 'black',
        '9': 'white',
        '0': main
    }
    figure = figures[raw_input("Enter command:\n"
                               "1 - Draw triangle\n"
                               "2 - Draw square\n"
                               "3 - Draw circle\n"
                               "4 - Draw star\n"
                               "5 - Draw ninja circle\n"
                               "6 - Draw spiral\n"
                               "7 - Grey\n"
                               "8 - Black\n"
                               "9 - White\n"
                               "0 - Cancel\n")]()


def draw_triangle():
    dist = float(raw_input("Enter size of triangle: "))
    painter.forward(dist)
    painter.left(120)
    painter.forward(dist)
    painter.left(120)
    painter.forward(dist)


def draw_square():
    dist = float(raw_input("Enter size of square: "))
    painter.forward(dist)
    painter.right(90)
    painter.forward(dist)
    painter.right(90)
    painter.forward(dist)
    painter.right(90)
    painter.forward(dist)


def draw_circle():
    r = float(raw_input("Enter radius of circle: "))
    painter.circle(r)


def draw_star():
    for i in range(20):
        painter.forward(i * 10)
        painter.right(144)


def draw_ninja_circle():
    for i in range(180):
        painter.forward(100)
        painter.right(30)
        painter.forward(20)
        painter.left(60)
        painter.forward(50)
        painter.right(30)

        painter.penup()
        painter.setposition(0, 0)
        painter.pendown()

        painter.right(2)


def draw_spiral():
    x = 1
    while x < 400:
        painter.fd(50 + x)
        painter.rt(90.911)
        x += 1


def pen_color():
    color = {
        '1': 'red',
        '2': 'blue',
        '3': 'green',
        '4': 'magenta',
        '5': 'yellow',
        '6': 'pink',
        '7': 'grey',
        '8': 'black',
        '9': 'white',
        '0': painter.pencolor()
    }
    color = color[raw_input("Enter command:\n"
                            "1 - Red\n"
                            "2 - Blue\n"
                            "3 - Green\n"
                            "4 - Magenta\n"
                            "5 - Yellow\n"
                            "6 - Pink\n"
                            "7 - Grey\n"
                            "8 - Black\n"
                            "9 - White\n"
                            "0 - Cancel\n")]
    painter.pencolor(color)


def fill_color():
    color = {
        '1': 'red',
        '2': 'blue',
        '3': 'green',
        '4': 'magenta',
        '5': 'yellow',
        '6': 'pink',
        '7': 'grey',
        '8': 'black',
        '9': 'white',
        '0': painter.fillcolor()
    }
    color = color[raw_input("Enter command:\n"
                            "1 - Red\n"
                            "2 - Blue\n"
                            "3 - Green\n"
                            "4 - Magenta\n"
                            "5 - Yellow\n"
                            "6 - Pink\n"
                            "7 - Grey\n"
                            "8 - Black\n"
                            "9 - White\n"
                            "0 - Cancel\n")]
    painter.fillcolor(color)


def pen_size():
    painter.pensize(float(raw_input("Enter pen size: ")))


def make_save():
    pass


def make_reset():
    painter.reset()


def set_options():
    commands = {
      '1': painter.begin_fill,
      '2': painter.end_fill,
      '3': painter.showturtle,
      '4': painter.hideturtle,
      '5': setup_speed,
      '6': painter.home,
      '7': pen_size,
      '9': create_new_doc,
      '0': exit,
      'o': open_doc,
      's': make_save(),
      'b': main
    }
    mult = commands[raw_input("Enter command:\n"
                              "1 - Fill enable\n"
                              "2 - Fill disable\n"
                              "3 - Show turtle\n"
                              "4 - Hide turtle\n"
                              "5 - Speed turtle\n"
                              "6 - Home\n"
                              "7 - Pen size\n"
                              "9 - Create new document\n"
                              "0 - Exit\n"
                              "o - Open\n"
                              "s - Save\n"
                              "b - Back")]()
    if mult == painter.speed:
        painter.speed(int(raw_input("Enter turtle speed 0 - 10: ")))


def create_new_doc():
    f = open(raw_input('Enter name: ') + ".txt", 'w')


def open_doc():
    pass


def setup_speed():
    painter.speed(int(raw_input("Enter turtle speed: ")))


def main():
    while True:
        turtle.Screen()
        commands = {
            '1': painter.setpos,
            '2': painter.penup,
            '3': painter.pendown,
            '4': set_figure,
            '5': pen_color,
            '6': fill_color,
            '7': 0,
            '8': 0,
            '9': 0,
            '0': set_options,
        }
        try:
            mult = commands[raw_input("Enter command:\n"
                                      "1 - Set position\n"
                                      "2 - Pen Up\n"
                                      "3 - Pen Down\n"
                                      "4 - Set figure\n"
                                      "5 - Set pen color\n"
                                      "6 - Set fill color\n"
                                      "7 - \n"
                                      "8 - \n"
                                      "9 - \n"
                                      "0 - Options\n")]()
        except KeyError as e:
            raise ValueError('Undefined command: {}'.format(e.args[0]))


if __name__ == '__main__':
    main()
