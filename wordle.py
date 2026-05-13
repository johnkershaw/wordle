import turtle

WHITE = 'white'
GREY = '#787C7E'
YELLOW = '#C9B458'
GREEN = '#6AAA64'
BLACK = 'black'

WIDTH, HEIGHT = (400, 400)
TILE_W = WIDTH / 4
TILE_H = TILE_W
GAP = TILE_W / 10
ORIGIN_X = 0 - TILE_W * 2.5 - GAP * 2.0
ORIGIN_Y = 0 + TILE_H * 3.0 + GAP * 2.5

target = 'PLUME'

guesses = ['STOCK', 'ARISE', 'BUDGE', 'PLUME', '     ', '     ']
guesses = [' ' * 5] * 6

scr = turtle.Screen()
scr.setup(WIDTH, HEIGHT)
scr.bgcolor(BLACK)
scr.tracer(0)

t = turtle.Turtle()

def teleport(t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def draw_rect(t:turtle.Turtle, x:float, y:float, w:float, h:float, letter:str, colour:str):
    t.color(BLACK)
    teleport(t, x, y)
    t.fillcolor(colour)
    t.begin_fill()
    for side in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    teleport(t, x + TILE_W / 2, y + TILE_H / 6)
    t.color(WHITE)
    t.write(letter, align = "center", font = ("Arial", 36, "bold"))

def draw_guess(letters, colours, x, y):
    for column in range(len(letters)):
        letter = letters[column]
        colour = colours[column]
        x = ORIGIN_X + column * (TILE_W + GAP)
        draw_rect(t, x, y, TILE_W, TILE_H, letter, colour)
    

def output(target, guesses):
    for row, guess in enumerate(guesses):
        x = ORIGIN_X
        y = ORIGIN_Y - row * (TILE_H + GAP)
        teleport(t, x, y)
        colours = compare(target, guess)
        draw_guess(guess, colours, x, y)
        

def compare(target, guess):
    results = []
    for i, letter in enumerate(guess):
        result = GREY
        if letter == ' ':
            result = WHITE
        if letter in target:
            result = YELLOW
        if letter == target[i]:
            result = GREEN
        results.append(result) 
    return results
assert compare('PLUME', 'KEVIN') == [GREY, YELLOW, GREY, GREY, GREY]
# assert compare('PLUME', 'POPPY') == [GREEN, GREY, GREY, GREY, GREY]

play = True
while play: 
    output(target, guesses)   # draw the empty grid

    turn = 0
    while turn < 6:
        guess = input('Enter 5-letter word: ').upper()
        guesses[turn] = guess
        output(target, guesses)
        scr.update()   
        turn += 1
        if guess == target:
            print('You win!')
            break
    else:
        print('LOSERRRRRRRRR!!!!')

    play = input('Play again? ')[0].upper() == 'Y'