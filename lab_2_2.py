from flask import Flask, request, jsonify
import math

app = Flask(__name__)

def integrate(lower, upper, N):
    delta_x = (upper - lower) / N
    result = 0.0

    for i in range(N):
        x_i = lower + i * delta_x
        area_i = abs(math.sin(x_i)) * delta_x
        result += area_i

    return result

@app.route('/numericalintegralservice/<lower>/<upper>', methods=['GET'])
def numerical_integral_service(lower, upper):
    lower = float(lower)
    upper = float(upper)
    
    num_intervals = [10, 100, 1000, 10000, 100000, 1000000]
    results = {}

    for N in num_intervals:
        result = integrate(lower, upper, N)
        results[N] = result

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
