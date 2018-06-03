import time as t
import sys

# stdin
for line in sys.stdin:
    print('input:', line)

while True:
    t.sleep(2)
    # stdout
    print('hello world', flush=True)
    # stderr
    print("fatal error, lol", file=sys.stderr, flush=True)
