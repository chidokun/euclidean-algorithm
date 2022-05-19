from app import random_file, read_file, write_result
from time import time_ns

NUMBER_FILE_PATH = './data/bezout_number.txt'
EUCLID_NUMBER_FILE_PATH = './data/number.txt'
RESULT_PATH = './data/bezout_result.csv'

def write_result(rs, path: str):
    f = open(path, "w+")
    f.write(",".join(["a", "b", "gcd", "x", "y", "step", "time_ms"]) + '\n')
    for r in rs:
        print(r)
        f.write("%d,%d,%d,%d,%d,%d,%d\n" % (r["a"], r["b"], r["gcd"], r["x"], r["y"], r["step"], r["time_ms"]))
    f.close()

def extended_gcd(a, b):
    old_r, r = abs(a), abs(b)
    old_x, x = 1, 0
    old_y, y = 0, 1

    step = 0
    while r != 0:
        step += 1
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    gcd, x, y, step = old_r, old_x, old_y, step

    if a < 0:
        x *= -1

    if b < 0:
        y *= -1

    return gcd, x, y, step

def experiment(ls):
    result = []
    for i in ls:
        a = i[0]
        b = i[1]

        begin = time_ns() / 1000
        d, x, y, step = extended_gcd(a, b)
        end = time_ns() / 1000
        result.append({ 
            "a": a,
            "b": b,
            "gcd": d,
            "x": x,
            "y": y,
            "step": step,
            "time_ms": (end - begin)
        })
    return result

def main():
    # random_file(NUMBER_FILE_PATH)
    ls = read_file(EUCLID_NUMBER_FILE_PATH)
    print(ls)

    result = experiment(ls)
    print(result)
    write_result(result, RESULT_PATH)

    experiment_test = [(13, 3), (13, -3), (-13, 3), (-13, -3), (3, 0), (0, 3), (0, 0)]

    for (a, b) in experiment_test:
        gcd, x, y, step = extended_gcd(a, b)
        a = a if a >= 0 else f"({a})"
        b = b if b >= 0 else f"({b})"
        x = x if x >= 0 else f"({x})"
        y = y if y >= 0 else f"({y})"
        print(f"{gcd} = {a} x {x} + {b} x {y}")

if __name__ == "__main__":
    main()
