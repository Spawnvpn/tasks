import turtle

memory_list = []
painter = turtle.Turtle()


def draw_triangle():
    dist = float(raw_input("Enter size of triangle: "))
    painter.forward(dist)
    painter.left(120)
    painter.forward(dist)
    painter.left(120)
    painter.forward(dist)
    func_dict = ({draw_triangle.__name__: dist})
    memory_list.append(func_dict)


def draw_square():
    dist = float(raw_input("Enter size of square: "))
    painter.forward(dist)
    painter.right(90)
    painter.forward(dist)
    painter.right(90)
    painter.forward(dist)
    painter.right(90)
    painter.forward(dist)
    func_dict = ({draw_square.__name__: dist})
    memory_list.append(func_dict)


def draw_circle():
    r = float(raw_input("Enter radius of circle: "))
    painter.circle(r)
    func_dict = ({draw_circle.__name__: r})
    memory_list.append(func_dict)


def draw_star():
    for i in range(20):
        painter.forward(i * 10)
        painter.right(144)
    func_dict = ({draw_star.__name__: None})
    memory_list.append(func_dict)


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
    func_dict = ({draw_ninja_circle.__name__: None})
    memory_list.append(func_dict)


def draw_spiral():
    x = 1
    while x < 400:
        painter.fd(50 + x)
        painter.rt(90.911)
        x += 1
    func_dict = ({draw_spiral.__name__: None})
    memory_list.append(func_dict)


def draw_conclusion():
    painter.reset()
    painter.hideturtle()
    painter.speed(0)
    c = 0
    x = 0

    colors = [
        # reddish colors
        (1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.00),
        (1.00, 0.07, 0.00), (1.00, 0.10, 0.00), (1.00, 0.12, 0.00),
        (1.00, 0.15, 0.00), (1.00, 0.17, 0.00), (1.00, 0.20, 0.00),
        (1.00, 0.23, 0.00), (1.00, 0.25, 0.00), (1.00, 0.28, 0.00),
        (1.00, 0.30, 0.00), (1.00, 0.33, 0.00), (1.00, 0.35, 0.00),
        (1.00, 0.38, 0.00), (1.00, 0.40, 0.00), (1.00, 0.42, 0.00),
        (1.00, 0.45, 0.00), (1.00, 0.47, 0.00),
        # orange colors
        (1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.00),
        (1.00, 0.57, 0.00), (1.00, 0.60, 0.00), (1.00, 0.62, 0.00),
        (1.00, 0.65, 0.00), (1.00, 0.68, 0.00), (1.00, 0.70, 0.00),
        (1.00, 0.72, 0.00), (1.00, 0.75, 0.00), (1.00, 0.78, 0.00),
        (1.00, 0.80, 0.00), (1.00, 0.82, 0.00), (1.00, 0.85, 0.00),
        (1.00, 0.88, 0.00), (1.00, 0.90, 0.00), (1.00, 0.93, 0.00),
        (1.00, 0.95, 0.00), (1.00, 0.97, 0.00),
        # yellowy colors
        (1.00, 1.00, 0.00), (0.95, 1.00, 0.00), (0.90, 1.00, 0.00),
        (0.85, 1.00, 0.00), (0.80, 1.00, 0.00), (0.75, 1.00, 0.00),
        (0.70, 1.00, 0.00), (0.65, 1.00, 0.00), (0.60, 1.00, 0.00),
        (0.55, 1.00, 0.00), (0.50, 1.00, 0.00), (0.45, 1.00, 0.00),
        (0.40, 1.00, 0.00), (0.35, 1.00, 0.00), (0.30, 1.00, 0.00),
        (0.25, 1.00, 0.00), (0.20, 1.00, 0.00), (0.15, 1.00, 0.00),
        (0.10, 1.00, 0.00), (0.05, 1.00, 0.00),
        # greenish colors
        (0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.10),
        (0.00, 0.85, 0.15), (0.00, 0.80, 0.20), (0.00, 0.75, 0.25),
        (0.00, 0.70, 0.30), (0.00, 0.65, 0.35), (0.00, 0.60, 0.40),
        (0.00, 0.55, 0.45), (0.00, 0.50, 0.50), (0.00, 0.45, 0.55),
        (0.00, 0.40, 0.60), (0.00, 0.35, 0.65), (0.00, 0.30, 0.70),
        (0.00, 0.25, 0.75), (0.00, 0.20, 0.80), (0.00, 0.15, 0.85),
        (0.00, 0.10, 0.90), (0.00, 0.05, 0.95),
        # blueish colors
        (0.00, 0.00, 1.00), (0.05, 0.00, 1.00), (0.10, 0.00, 1.00),
        (0.15, 0.00, 1.00), (0.20, 0.00, 1.00), (0.25, 0.00, 1.00),
        (0.30, 0.00, 1.00), (0.35, 0.00, 1.00), (0.40, 0.00, 1.00),
        (0.45, 0.00, 1.00), (0.50, 0.00, 1.00), (0.55, 0.00, 1.00),
        (0.60, 0.00, 1.00), (0.65, 0.00, 1.00), (0.70, 0.00, 1.00),
        (0.75, 0.00, 1.00), (0.80, 0.00, 1.00), (0.85, 0.00, 1.00),
        (0.90, 0.00, 1.00), (0.95, 0.00, 1.00)
    ]

    while x < 1000:
        idx = int(c)
        color = colors[idx]
        painter.color(color)
        painter.forward(x)
        painter.right(98)
        x += 1
        c += 0.1
    func_dict = ({draw_conclusion.__name__: None})
    memory_list.append(func_dict)
