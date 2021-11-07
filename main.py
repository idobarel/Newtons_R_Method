#SOLVER.

# func = "x**104000-19.5*x+1"

func = input("[?] Enter the function / equation you want to solve >> ")


def make_a_func(func):
    pass


def place_X_in_func(func, num: float, get_string=False):
    func = func.replace(' ', '')
    equation = ''
    for i in range(len(func)):
        c = func[i];
        if c == 'X' or c == 'x':
            c = str(num)
        equation += c

    if get_string:
        return equation
    ans = float(eval(equation))
    return ans

def solve_line(b, m):
    x = (0 - b) / m
    return x

def get_d_root(x, delta=0.000000001):
    global func
    x1 = x
    x2 = x1 - delta
    delta_y = place_X_in_func(func, x1) - place_X_in_func(func, x2)
    delta_x = x1 - x2
    slope = delta_y / delta_x
    y = place_X_in_func(func, x1)
    b = y - slope * x1
    linear_root = solve_line(b, slope)
    return linear_root


def get_root(x):
    for i in range(100):
        xnew = get_d_root(x)
        if abs(xnew - x) < 0.001:
            break
        x = xnew

    x = "{:.3f}".format(float(x))
    return(x)


#call the get root function one with -100, 0, 100

roots = []
roots.append((get_root(-100), 0))
roots.append((get_root(0), 0))
roots.append((get_root(100), 0))
print(roots)
