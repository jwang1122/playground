import scipy

N = 10000
x_array = scipy.random.rand(N)
y_array = scipy.random.rand(N)
# generate N pseudorandom independent x and y-values on interval [0,1)
N_qtr_circle = sum(x_array ** 2 + y_array ** 2 < 1)
# Number of pts within the quarter circle x^2 + y^2 < 1 centered at the origin with radius r=1.
# True area of quarter circle is pi/4 and has N_qtr_circle points within it.
# True area of the square is 1 and has N points within it, hence we approximate pi with
pi_approx = 4 * float(N_qtr_circle) / N  # Typical values: 3.13756, 3.15156

print(pi_approx)
print("Done.")