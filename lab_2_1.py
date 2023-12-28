import math

def integrate(lower, upper, N):
    delta_x = (upper - lower) / N
    result = 0.0

    for i in range(N):
        x_i = lower + i * delta_x
        area_i = abs(math.sin(x_i)) * delta_x
        result += area_i

    return result

def main():
    lower_bound = 0.0
    upper_bound = math.pi
    num_intervals = [10, 100, 1000, 10000, 100000, 1000000, 1000000]

    for N in num_intervals:
        result = integrate(lower_bound, upper_bound, N)
        print(f"N = {N}: Result = {result}")

if __name__ == "__main__":
    main()
