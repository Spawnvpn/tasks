import turtle


def draw_diagram(words, type_diagram):
    association_list = words_counter(words)
    if type_diagram == 'sectors':
        draw_sectors(association_list)
    if type_diagram == 'rays':
        draw_rays(association_list)


def words_counter(words):
    list_words = words.split(" ")
    association_list = []
    seen = []
    for word in list_words:
        if word in seen:
            continue
        seen.append(word)
        association_list.append([word, list_words.count(word),
                                list_words.count(word) * 360.0 / len(list_words)])
    print association_list
    return association_list


def draw_sectors(association_list):
    angle = 0
    col = 0
    interval = 200
    colors = ['#a61212', '#b36d6d', '#7650e6', '#10c0c9', '#13c910', '#edea47',
              '#6e2626', '#9c9c9c', '#ce21d1', '#9a86c4', '#275a6b', '#067550',
              '#293826', '#cf7304', '#332b20', '#4f2d29', '#b88ab7', '#231e3d']
    painter = turtle.Turtle()
    for x in association_list:
        painter.setpos(0, 0)
        painter.pendown()
        painter.fillcolor(colors[col])
        painter.fill(True)
        painter.setpos(0, 0)
        painter.left(angle)
        painter.forward(200)
        painter.left(90)
        painter.circle(200, x[2])
        painter.fill(False)
        painter.setpos(0, 0)
        angle += x[2]
        painter.setheading(0)
        painter.penup()
        painter.setpos(300, interval)
        painter.dot(20, colors[col])
        painter.setpos(320, interval)
        painter.write(x[0])
        painter.setpos(360, interval)
        painter.write(x[1])
        painter.setpos(370, interval)
        painter.write("times")
        interval -= 25
        col += 1
    painter.hideturtle()


def draw_rays(association_list):
    col = 0
    colors = ['#a61212', '#b36d6d', '#7650e6', '#10c0c9', '#13c910', '#edea47',
              '#6e2626', '#9c9c9c', '#ce21d1', '#9a86c4', '#275a6b', '#067550',
              '#293826', '#cf7304', '#332b20', '#4f2d29', '#b88ab7', '#231e3d']
    painter = turtle.Turtle()
    angle_interval = 360 / len(association_list)
    painter.pensize(2)
    for x in association_list:
        painter.setpos(0, 0)
        painter.left(angle_interval)
        for i in xrange(x[1]):
            painter.fill(1)
            painter.pencolor(colors[col])
            painter.forward(60)
            painter.dot(5, colors[col])
            col += 1
            if col > 16:
                col = 0
        painter.write(x[0])
        painter.penup()
        painter.setpos(0, 0)
        painter.pendown()

words = "one two three lel kek " \
        "azaz lel bob patric two kek lel " \
        "two one one kek lel two azaz hello wow"
type_diagram = raw_input("Enter type ")

draw_diagram(words, type_diagram)
turtle.done()
