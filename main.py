import sympy as sym
import time

# The Func im using is 4*x**5-3*x-5


def get_func():
    return str(input("Please enter the function: "))


def place_X_in_func(func: str, num: float):
    func = func.replace(' ', '')
    equation = ''
    for i in range(len(func)):
        c = func[i];
        if c == 'X' or c == 'x':
            c = str(num)
        equation += c

    ans = float(eval(equation))
    return ans


def get_derivative_of_func(func: str):
    x = sym.Symbol('x')
    return str(sym.diff(eval(func)))


def get_guess(func: str):
    func = func.replace(' ', '')
    for i in range(-15, 0):
        a, b = abs(i), i
        if place_X_in_func(func=func, num=a) > 0:
            if place_X_in_func(func=func, num=b) < 0:
                return float(abs(a-b) / 2)
        elif place_X_in_func(func, a) < 0:
            if place_X_in_func(func=func, num=b) > 0:
                return float(abs(b - a) / 2)


function = get_func()  # The Func
dx = get_derivative_of_func(function)  # The derivative

start_time = time.time()
x = get_guess(function)
if x is None:
    x = float(input("Enter a guess that close to the root of the function: "))
for i in range(100):
    xnew = x - (place_X_in_func(function, x)) / (place_X_in_func(dx, x))
    if abs(xnew - x) < 0.000000000000000000000000001:
        break
    x = xnew

print(xnew, 'found, in', i, 'iterations.')
finish_time = time.time()
print('\n')
print('RunTime:', finish_time - start_time)
