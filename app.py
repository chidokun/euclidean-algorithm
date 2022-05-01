import gc
from math import floor
import random as rd
from time import time_ns

NUMBER_FILE_PATH = './data/number.txt'
RESULT_PATH = './data/result.csv'
NUMBER_OF_PAIRS = 100
BIT_LENGTH = 64

def random_number(bit_length):
    s = '0'
    for i in range(bit_length - 1):
        s += str(rd.randint(0, 1))
    return s

def random_file():
    f = open(NUMBER_FILE_PATH, "w")
    for i in range(NUMBER_OF_PAIRS):
        a = random_number(BIT_LENGTH)
        b = random_number(BIT_LENGTH)
        f.write(str(int(a, 2)) + " " + str(int(b, 2)) + "\n")
    f.close()

def read_file():
    f = open(NUMBER_FILE_PATH, "r")
    ls = f.readlines()
    f.close()
    result = []
    for s in ls:
        nums = s.split(" ")
        result.append([ int(nums[0]), int(nums[1])])
    
    return result;

def euclid_mod(a, b):
    return euclid_mod(a, -b) if b < 0 else a % b

def euclid_gcd(a, b, step=0): 
    step += 1

    if a == 0:
        return b, step
    return euclid_gcd(euclid_mod(b, a), a, step)

def experiment():
    result = []
    for i in ls:
        a = i[0]
        b = i[1]

        begin = time_ns() / 1000
        gcd, step = euclid_gcd(a, b)
        end = time_ns() / 1000
        result.append({ 
            "a": a, 
            "b": b, 
            "gcd": gcd, 
            "step": step,
            "time_ms": (end - begin) 
        })
    return result

def write_result(rs):
    f = open(RESULT_PATH, "w+")
    f.write(",".join(["a", "b", "gcd", "time_ms", "step"]) + '\n')
    for r in rs:
        print(r)
        f.write("%d,%d,%d,%d,%d\n" % (r["a"], r["b"], r["gcd"], r["step"], r["time_ms"]))
    f.close()


print(euclid_gcd(13, 3))
print(euclid_gcd(13, -3))
print(euclid_gcd(-13, 3))
print(euclid_gcd(-13, -3))
print(euclid_gcd(3, 0))
print(euclid_gcd(0, 3))
print(euclid_gcd(0, 0))

random_file()
ls = read_file()
print(ls)

result = experiment()
print(result)
write_result(result)



