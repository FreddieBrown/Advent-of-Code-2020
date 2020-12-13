import sys
import numpy as np


def p1(arrival, buses):
    min_wait = sys.maxsize
    bus_time = 0
    for bus in buses:
        diff = arrival/bus[1]
        wait_time = ((int(diff)+1) * bus[1]) - arrival
        if wait_time < min_wait:
            min_wait = wait_time
            bus_time = bus[1]

    return min_wait * bus_time


def p2(buses):
    N = 1
    for bus in buses:
        N = N * bus[1]

    return sum((m - r) * N // m * pow(N // m, -1, m) for r, m in buses) % N


with open("data/day13.txt") as f:
    arrival = int(f.readline())
    buses = [
        (i, int(bus))
        for i, bus in enumerate(f.readline().strip().split(","))
        if bus != "x"
    ]

print("Part 1: "+str(p1(arrival, buses)))
print("Part 2: "+str(p2(buses)))
