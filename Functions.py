import math
x = 0
y = 0
z = 0


def input_function():
    global x
    x = int(input('Enter a whole number (-1 to quit): '))


def square_x_function(j):
    global y
    y = j ** 2


def sqrt_x_function(j):
    global z
    z = math.sqrt(j)

running = True
while running:
    input_function()

    if x == -1:
        running = False
    else:
        print('Input value', x)
        square_x_function(x)
        print('Square of x', y)
        sqrt_x_function(x)
        print('Square root of x is:', z)
        print('')

print('Done')


