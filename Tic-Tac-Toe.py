from turtle import Turtle, Screen
import time

board = [["", "", ""], ["", "", ""], ["", "", ""]]
turn = 0
RED = "#CC3333"
BLACK = "#191919"

screen = Screen()
screen.setup(610, 610)
screen.title("Tic-Tac-Toe")
screen.tracer(0)


def home() -> None:
    """ Game Front Page. """

    reset()

    screen.bgpic("Home.png")
    screen.onscreenclick(play_style)
    screen.mainloop()


def play_style(x: float, y: float) -> None:
    """ Lets you choose how you play. """

    if -107 <= x <= 110 and -243 <= y <= -199:
        screen.clear()
        player = Turtle()
        player.hideturtle()
        player.speed(0)
        player.write("Coming Soon...", font=("Verdana", 24, "normal"), align="center")

    elif -107 <= x <= 110 and -300 <= y <= -255:
        draw_board()
        screen.onscreenclick(two_player)


def draw_board() -> None:
    """ Sketches the playing board field by Constructing a 3x3 grid. """

    board_turtle = Turtle()
    board_turtle.hideturtle()
    board_turtle.speed(0)

    screen.clear()

    axis = 100

    # Horizontal draw_line
    for i in range(3):
        board_turtle.penup()
        board_turtle.goto(-305, axis)
        board_turtle.pendown()
        board_turtle.forward(600)
        axis *= -1

    # Vertical draw_lines
    board_turtle.right(90)
    for i in range(3):
        board_turtle.penup()
        board_turtle.goto(axis, 305)
        board_turtle.pendown()
        board_turtle.forward(600)
        axis *= -1


def one_player():
    """ Coming Soon... """


def two_player(x: float, y: float) -> None:
    """ Enables multiplayer gameplay. 🎮👥 """

    global turn

    # 1, First Row, First Column
    if -300 <= x <= -100 and y >= 100 <= 300:
        if board[0][0] == "":
            if turn % 2 == 0:
                board[0][0] = "X"
                turn += 1
                draw_cross(-270, 130)
            else:
                board[0][0] = "O"
                turn += 1
                draw_circle(-202, 132)

    # 2, First Row, Second Column
    elif -100 <= x <= 100 and y >= 100 <= 300:
        if board[0][1] == "":
            if turn % 2 == 0:
                board[0][1] = "X"
                turn = turn + 1
                draw_cross(-70, 130)
            else:
                board[0][1] = "O"
                turn = turn + 1
                draw_circle(0, 132)

    # 3, First Row, Third Column
    elif 100 <= x <= 300 and y >= 100 <= 300:
        if board[0][2] == "":
            if turn % 2 == 0:
                board[0][2] = "X"
                turn = turn + 1
                draw_cross(130, 130)
            else:
                board[0][2] = "O"
                turn = turn + 1
                draw_circle(202, 132)

    # 4, Second Row, First Column
    elif -300 <= x <= -100 and y >= -100 <= 100:
        if board[1][0] == "":
            if turn % 2 == 0:
                board[1][0] = "X"
                turn = turn + 1
                draw_cross(-270, -70)

            else:
                board[1][0] = "O"
                turn = turn + 1
                draw_circle(-202, -70)

    # 5, Second Row, Second Column
    elif -100 <= x <= 100 and y >= -100 <= 100:
        if board[1][1] == "":
            if turn % 2 == 0:
                board[1][1] = "X"
                turn = turn + 1
                draw_cross(-70, -70)
            else:
                board[1][1] = "O"
                turn = turn + 1
                draw_circle(-0, -70)

    # 6, Second Row, Third Column
    elif 300 >= x >= 100 >= -100 <= y:
        if board[1][2] == "":
            if turn % 2 == 0:
                board[1][2] = "X"
                turn = turn + 1
                draw_cross(130, -70)
            else:
                board[1][2] = "O"
                turn = turn + 1
                draw_circle(202, -70)

    # 7, Third Row, First Column
    elif -300 <= x <= -100 and -300 <= y <= -100:
        if board[2][0] == "":
            if turn % 2 == 0:
                board[2][0] = "X"
                turn = turn + 1
                draw_cross(-270, -270)
            else:
                board[2][0] = "O"
                turn = turn + 1
                draw_circle(-202, -270)

    # 8, Third Row, Second Column
    elif 100 >= x >= -100 >= y >= -300:
        if board[2][1] == "":
            if turn % 2 == 0:
                board[2][1] = "X"
                turn = turn + 1
                draw_cross(-70, -270)
            else:
                board[2][1] = "O"
                turn = turn + 1
                draw_circle(0, -270)

    # 9, Third Row, Third Column
    elif 100 <= x <= 300 and -300 <= y <= -100:
        if board[2][2] == "":
            if turn % 2 == 0:
                board[2][2] = "X"
                turn = turn + 1
                draw_cross(130, -270)
            else:
                board[2][2] = "O"
                turn = turn + 1
                draw_circle(202, -270)

    score()


def draw_cross(x: float, y: float) -> None:
    """ Sketches a Cross on the given axis. """

    draw_cross_turtle = Turtle()
    draw_cross_turtle.hideturtle()
    draw_cross_turtle.speed(0)
    draw_cross_turtle.color(RED)

    angle = 45
    for i in range(2):
        draw_cross_turtle.penup()
        draw_cross_turtle.goto(x, y)
        draw_cross_turtle.width(50)
        draw_cross_turtle.pendown()
        draw_cross_turtle.left(angle)
        draw_cross_turtle.forward(200)
        y += 140
        angle += 225


def draw_circle(x: float, y: float) -> None:
    """ Sketches a Circle on the given axis. """

    draw_circle_turtle = Turtle()
    draw_circle_turtle.hideturtle()
    draw_circle_turtle.speed(0)
    draw_circle_turtle.color(BLACK)
    draw_circle_turtle.penup()
    draw_circle_turtle.goto(x, y)
    draw_circle_turtle.width(50)
    draw_circle_turtle.pendown()
    draw_circle_turtle.circle(70)


def score() -> None:
    """ Confirms the winning condition. """

    x_axis = -200
    y_axis = 200

    # Horizontal Win
    for i in range(3):
        if board[i] == ["X", "X", "X"]:
            draw_line(-280, y_axis, 0, 560, BLACK)
            player_x_win()
            screen.onscreenclick(game_over)
        elif board[i] == ["O", "O", "O"]:
            draw_line(-280, y_axis, 0, 560, RED)
            player_o_win()
            screen.onscreenclick(game_over)
        y_axis -= 200

    # Vertical Win
    for i in range(3):
        if board[0][i] == "X" and board[1][i] == "X" and board[2][i] == "X":
            draw_line(x_axis, 280, 90, 560, BLACK)
            player_x_win()
            screen.onscreenclick(game_over)
        elif board[0][i] == "O" and board[1][i] == "O" and board[2][i] == "O":
            draw_line(x_axis, 280, 90, 560, RED)
            player_o_win()
            screen.onscreenclick(game_over)
        x_axis += 200

    # Diagonal Win
    if board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        draw_line(-270, 270, 45, 763, BLACK)
        player_x_win()
        screen.onscreenclick(game_over)
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        draw_line(-260, 260, 45, 735, RED)
        player_o_win()
        screen.onscreenclick(game_over)
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        draw_line(270, 270, 135, 763, BLACK)
        player_x_win()
        screen.onscreenclick(game_over)
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        draw_line(260, 260, 135, 735, RED)
        player_o_win()
        screen.onscreenclick(game_over)

    # Draw
    if turn == 9:
        draw()
        screen.onscreenclick(game_over)


def draw_line(x: int, y: int, angle: int, length: int, color: str) -> None:
    """ Marks the game’s end by drawing a line. """

    draw_line_turtle = Turtle()
    draw_line_turtle.hideturtle()
    draw_line_turtle.speed(0)
    draw_line_turtle.penup()
    draw_line_turtle.color(color)
    draw_line_turtle.width(20)
    draw_line_turtle.right(angle)
    draw_line_turtle.goto(x, y)
    draw_line_turtle.pendown()
    draw_line_turtle.forward(length)


def game_over(x, y) -> None:
    """ Returns to Homepage. """

    if -130 <= x <= 135 and -135 <= y <= -80:
        home()


def player_x_win() -> None:
    time.sleep(1)
    screen.clear()
    screen.bgpic("X.png")


def player_o_win() -> None:
    time.sleep(1)
    screen.clear()
    screen.bgpic("O.png")


def draw() -> None:
    time.sleep(1)
    screen.clear()
    screen.bgpic("Draw.png")


def reset() -> None:
    """ Resets the game board. """

    global turn
    for i in range(3):
        for j in range(3):
            board[i][j] = ""
            turn = 0


home()
