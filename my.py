from numpy import  *
import matplotlib.pyplot as plt

# y = mx + b
# m is slope, b is y-intercept

def visualize(points, m, b):
    plt.plot([x[0] for x in points], [x[1] for x in points], alpha=0.5, markersize=5.0, marker='o', color='y', linestyle='None')
    plt.plot([x[0] for x in points], [m*x[0] + b for x in points])
    plt.show()

def compute_error_for_line_given_points(b, m, points):
    total_error = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        total_error += (y - (m * x + b)) ** 2
    return total_error / float(len(points))

# def step_gradient(b_current, m_current, points, learningRate):
#     b_gradient = 0
#     m_gradient = 0
#     N = float(len(points))
#     for i in range(0, len(points)):
#         x = points[i, 0]
#         y = points[i, 1]
#         b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
#         m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
#         new_b = b_current - (learningRate * b_gradient)
#         new_m = m_current - (learningRate * m_gradient)
#     return [new_b, new_m]

def step_gradient(b_current, m_current, points, learningRate):
    isFinal = False
    m = []
    m.append(m_current - (learningRate * 1))
    m.append(m_current + (learningRate * 1))
    b = []
    b.append(b_current - (learningRate * 100))
    b.append(b_current + (learningRate * 100))

    error_list = {}
    initial_error = compute_error_for_line_given_points(b_current, m_current, points)
    for slope in m:
        for offset in b:
            error_list[(slope, offset)] = compute_error_for_line_given_points(offset, slope, points)

    min_val = min(error_list.values())
    m_min, b_min = min(error_list, key = lambda x: error_list[x])

    if min_val > initial_error:
        print error_list, initial_error
        isFinal = True
    else:
        m_current += (m_min - m_current) * (initial_error - min_val)
        b_current += (b_min - b_current) * (initial_error - min_val)
    return (b_current, m_current, isFinal)

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iterations):
    b = starting_b
    m = starting_m
    for i in range(num_iterations):
        b, m, isFinal = step_gradient(b, m, array(points),learning_rate)
        if isFinal:
            break
        if i%100 == 0:
            print b, m
    return [b, m]
    
def main():
    # points = genfromtxt( "data_gen/data_1012_1.0_2.0_1000_2_250.csv", delimiter=",")
    points = genfromtxt( "data_gen/data_1003_-3.5_7000_1000_2_250.csv", delimiter=",")
    # learning_rate = 0.01
    learning_rate = 0.001
    initial_b = 0.0 # initial y-intercept guess
    initial_m = 0.0 # initial slope guess
    num_iterations = 10000
    # num_iterations = 1000
    print " Starting gardient descent b = {0}  m = {1}  error = {2}".format(initial_b, initial_m, compute_error_for_line_given_points(initial_b, initial_m, points))
    print " Running..."
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_for_line_given_points(b, m, points))

    visualize(points, m, b)
    
print "Debug: start"
if __name__ == '__main__':
    main()

print "Debug: end"
