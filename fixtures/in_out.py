import time as t
import sys


for line in sys.stdin:
    print('input:', line)

while True:
    t.sleep(2)
    print('hello world')
    print("fatal error, lol", file=sys.stderr)

