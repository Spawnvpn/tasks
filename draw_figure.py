import functools
import collections
from figures import *
import json


def decor(commands=None):
    def dec(function):
        @functools.wraps(function)
        def wrap(*args):
            if args:
                function(args[0])
                return wrap
            namelist = []
            for key, value in collections.OrderedDict(sorted(commands.items(),
                                                      key=lambda t: int(t[0]))).items():
                if callable(value):
                    command_value = value.__name__
                else:
                    command_value = value
                command_value = command_value.replace(".", " ")
                command_value = command_value.replace("_", " ")
                command_value = command_value.title()
                namelist.append(key + " - " + command_value)
            print "Enter command:"
            print "\n".join(namelist)
            try:
                multi = commands[raw_input()]
                function(multi)
            except KeyError:
                print "Undefined Key, try again"
                return
        return wrap
    return dec


def isfloat(value):
    try:
        float(value)
        return True
    except TypeError:
        return False
    except ValueError:
        return False


def terminate():
    exit()


def cancel():
    pass


def edit_doc():
    new_memory_list = []
    filename = raw_input('Enter name: ') + ".txt"
    buff = json.load(file(filename))
    for element in buff:
        couple = element.items()
        func = couple[0][0]
        func = func.encode("UTF-8")
        arg = couple[0][1]
        print func + ": ", arg
        command = raw_input("Edit this operation? y / n / exit ")
        if command == "y":
            func = raw_input("Enter new operation: ")
            arg = raw_input("Enter value: ")
        elif command == "exit":
            return
        func_dict = {func: arg}
        new_memory_list.append(func_dict)
    f = open(filename, "w")
    json.dump(new_memory_list, f)
    f.close()


def make_save():
    f = open(raw_input('Enter name: ') + ".txt", 'w')
    json.dump(memory_list, f)
    f.close()


def make_reset():
    painter.reset()
    func_dict = ({make_reset.__name__: None})
    memory_list.append(func_dict)


def open_doc():
    buff = json.load(file(raw_input("Enter filename: ") + ".txt"))
    for element in buff:
        couple = element.items()
        func = couple[0][0]
        func = func.encode("UTF-8")
        func = eval(func)
        arg = couple[0][1]
        if type(arg) == list:
            func(arg)
        elif isfloat(arg) or arg == 0:
            func(arg)
        elif unicode(arg) and arg is not None:
            arg = arg.encode("UTF-8")
            func(arg)
        else:
            func()


def setup_speed(speed=None):
    if speed or speed == 0:
        painter.speed(speed)
    else:
        painter.speed(int(raw_input("Enter turtle speed: ")))
    func_dict = ({setup_speed.__name__: painter.speed()})
    memory_list.append(func_dict)


def pen_size(size=None):
    if not size:
        size = float(raw_input("Enter pen size: "))
    painter.pensize(size)
    func_dict = ({pen_size.__name__: size})
    memory_list.append(func_dict)


def set_position(*args):
    if not args:
        x = float(raw_input("Enter X: "))
        y = float(raw_input("Enter Y: "))
    else:
        x = args[0][0]
        y = args[0][1]
    painter.setpos(x, y)
    func_dict = ({set_position.__name__: (x, y)})
    memory_list.append(func_dict)


def draw_forward(distance=None):
    if not distance:
        distance = float(raw_input("Enter distance: "))
    painter.forward(distance)
    func_dict = ({draw_forward.__name__: distance})
    memory_list.append(func_dict)


def set_angle(angle=None):
    if not angle:
        angle = float(raw_input("Enter angle: "))
    painter.setheading(angle)
    func_dict = ({set_angle.__name__: angle})
    memory_list.append(func_dict)


@decor(commands={
    '1': draw_triangle,
    '2': draw_square,
    '3': draw_circle,
    '4': draw_star,
    '5': draw_ninja_circle,
    '6': draw_spiral,
    '7': draw_conclusion,
    '0': cancel
})
def set_figure(func=None):
    func()


@decor(commands={
    '1': 'red',
    '2': 'blue',
    '3': 'green',
    '4': 'magenta',
    '5': 'yellow',
    '6': 'pink',
    '7': 'grey',
    '8': 'black',
    '9': 'white',
    '0': cancel
})
def pen_color(func=None):
    if func == cancel:
        return
    painter.pencolor(func)
    func_dict = ({pen_color.__name__: func})
    memory_list.append(func_dict)


@decor(commands={
    '1': 'red',
    '2': 'blue',
    '3': 'green',
    '4': 'magenta',
    '5': 'yellow',
    '6': 'pink',
    '7': 'grey',
    '8': 'black',
    '9': 'white',
    '0': cancel
})
def fill_color(func=None):
    if func == cancel:
        return
    painter.fillcolor(func)
    func_dict = ({fill_color.__name__: func})
    memory_list.append(func_dict)


@decor(commands={
    '1': painter.begin_fill,
    '2': painter.end_fill,
    '3': painter.showturtle,
    '4': painter.hideturtle,
    '5': setup_speed,
    '6': painter.home,
    '7': pen_size,
    '9': edit_doc,
    '0': terminate,
    '10': open_doc,
    '11': make_save,
    '12': cancel
})
def set_options(func):
    if func == painter.begin_fill or func == painter.end_fill\
            or func == painter.showturtle or\
            func == painter.hideturtle or func == painter.home:
        func_dict = ({"painter." + func.__name__: None})
        memory_list.append(func_dict)
    func()


@decor(commands={
    '1': draw_forward,
    '2': set_angle,
    '3': set_position,
    '4': painter.penup,
    '5': painter.pendown,
    '6': set_figure,
    '7': pen_color,
    '8': fill_color,
    '9': make_reset,
    '0': set_options,
})
def main(func=None):
    if func == painter.penup or func == painter.pendown:
        func_dict = ({"painter." + func.__name__: None})
        memory_list.append(func_dict)
    func()


if __name__ == '__main__':
    turtle.Screen()
    while True:
        main()
