import time


start = time.time()

now = time.gmtime()
print(now)

stack = time.asctime(now)
print(stack)

stop = time.time()

time.sleep(9)

print(stop - start)


