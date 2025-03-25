import sys
import time

print(sys.argv)
arguments = sys.argv
seconds = int(arguments[1])
print(seconds)



for i in range(seconds):
    print(i)
    time.sleep(1)
