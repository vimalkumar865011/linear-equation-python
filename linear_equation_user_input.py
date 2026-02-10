def linear_equation(m, x, c):
    return m * x + c

# User input
m = float(input("Enter value of m: "))
x = float(input("Enter value of x: "))
c = float(input("Enter value of c: "))

y = linear_equation(m, x, c)
print(f"For equation y = {m}*x + {c}, the result is y = {y}")
