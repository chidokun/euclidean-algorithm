from app import random_file, read_file, write_result
from time import time_ns

NUMBER_FILE_PATH = './data/bezout_number.txt'
RESULT_PATH = './data/bezout_result.csv'

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

  return old_r, old_x, old_y, step

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
            "step": step,
            "time_ms": (end - begin) 
        })
    return result

random_file(NUMBER_FILE_PATH)
ls = read_file(NUMBER_FILE_PATH)
print(ls)

result = experiment(ls)
print(result)
write_result(result, RESULT_PATH)

print(extended_gcd(13, 3))
print(extended_gcd(13, -3))
print(extended_gcd(-13, 3))
print(extended_gcd(-13, -3))
print(extended_gcd(3, 0))
print(extended_gcd(0, 3))
print(extended_gcd(0, 0))
