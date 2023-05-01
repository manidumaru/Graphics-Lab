from random import sample
from time import time_ns
from algorithm import insertion, mergeSort

def run(n):
    data = sample(range(1, n*10000), n)

    start_time = time_ns()
    # insertion(data)
    mergeSort(data)
    end_time = time_ns()
    total_time = end_time - start_time
    print(f"{n} data = {total_time/10**6} milliseconds")


if __name__ == "__main__":
    n = 10000
    for i in range(1,20,2):
        run(n*i)