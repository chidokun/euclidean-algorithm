import gc
from math import floor
import random as rd
from time import time_ns

NUMBER_FILE_PATH = './data/number.txt'
RESULT_PATH = './data/result2.csv'
NUMBER_OF_PAIRS = 100
BIT_LENGTH = 64
NEGATIVE_SIGN_THRESHOLD=30

def random_number(bit_length):
    s = '0'
    for i in range(bit_length - 1):
        s += str(rd.randint(0, 1))
    return s

def get_negative_sign():
    return rd.randint(1, 100) <= NEGATIVE_SIGN_THRESHOLD

def get_number(bin_string, is_negative):
    num = int(bin_string, 2)
    return -num if is_negative else num

def random_file(path: str):
    f = open(path, "w")
    for i in range(NUMBER_OF_PAIRS):
        a = random_number(BIT_LENGTH)
        negative_a = get_negative_sign()
        b = random_number(BIT_LENGTH)
        negative_b = get_negative_sign()
        
        f.write(str(get_number(a, negative_a)) + " " + str(get_number(b, negative_b)) + "\n")
    f.close()

def read_file(path: str):
    f = open(path, "r")
    ls = f.readlines()
    f.close()
    result = []
    for s in ls:
        nums = s.split(" ")
        result.append([ int(nums[0]), int(nums[1])])
    
    return result;

def euclid_mod(a, b):
    return a % -b if b < 0 else a % b

def euclid_gcd(a, b, step=0): 
    step += 1
    if b == 0:
        return abs(a), step
    return euclid_gcd(b, euclid_mod(a, b), step)

# 1 gcd(-13, 3) = gcd(3, -13 mod 3) = gcd(3, 2)
# 2 gcd(3, 2) = gcd(2, 3 mod 2) = gcd(2, 1)
# 3 gcd(2, 1) = gcd(1, 2 mod 1) = gcd(1, 1)
# 4 gcd(1, 0) = 1

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

def write_result(rs, path: str):
    f = open(path, "w+")
    f.write(",".join(["a", "b", "gcd", "step", "time_ms"]) + '\n')
    for r in rs:
        print(r)
        f.write("%d,%d,%d,%d,%d\n" % (r["a"], r["b"], r["gcd"], r["step"], r["time_ms"]))
    f.close()

def main():
    print(euclid_gcd(13, 3))
    print(euclid_gcd(13, -3))
    print(euclid_gcd(-13, 3))
    print(euclid_gcd(-13, -3))
    print(euclid_gcd(3, 0))
    print(euclid_gcd(0, 3))
    print(euclid_gcd(0, 0))

    random_file(NUMBER_FILE_PATH)
    ls = read_file(NUMBER_FILE_PATH)
    print(ls)

    result = experiment()
    print(result)
    write_result(result, RESULT_PATH)

if __name__ == "__main__":
    main()
