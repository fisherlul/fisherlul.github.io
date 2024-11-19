# TP Newton
def newton_raphson(f, df, x_0, tolerance=1e-6, max_iterations=100):
    x = x_0
    for _ in range(max_iterations):
        f_x = f(x)
        if abs(f_x) < tolerance:
            return x
        
        derivative = df(x)
        if derivative == 0:
            raise ValueError("Derivative is zero at x={}".format(x))
        x -= f_x / derivative
