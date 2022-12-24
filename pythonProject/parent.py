#!/usr/bin/python

import os
import sys
import random


def run_children():
    child = os.fork()
    if child == 0:
        argument = str(random.randint(5, 10))
        os.execl("./child.py", "child.py", argument)
    print(f"Parent [{os.getpid()}]: I ran children process with PID {child}")


child_num = sys.argv[1]
child_num = int(child_num)

for i in range(0, child_num):
    run_children()

while child_num > 0:
    child_pid, status = os.wait()
    status = status / 256
    status = int(status)
    print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {status}.")
    if status == 0:
        child_num = child_num - 1
    else:
        run_children()