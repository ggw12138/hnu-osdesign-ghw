import cvxpy as cp
import numpy as np
x = cp.Variable(3, integer=True)
a = np.array([5, 8, 10])
b = np.array([20, 25, 30])
F = np.array([[4, 2.5, -10], [2.5, 36, -15], [-10, -15, 100]])
obj = cp.Minimize(cp.quad_form(x, F))
con = [x >= 0, b@x <= 5000, a@x >= 1000]
prob = cp.Problem(obj, con)
prob.solve(solver='GLPK_MI',)
print(x.value)
print(prob.value)
