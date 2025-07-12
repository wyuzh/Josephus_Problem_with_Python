# Made by Mike_Zhang
# https://ultrafish.io

from queue import Queue
n = int(input("Step 1: Input n (the total number of people, integer > 1) and press 'Enter' to confirm: "))
m = int(input("Step 2: Input m (the number of counts for each step, integer > 0) and press 'Enter' to confirm: "))

print("Calculating ...")

position = 1 # mark next eliminated position
nowposition = 1 # mark now position
outqueue = Queue() # store the output
nqueue = Queue() # store the numbers without the eliminated one in one counting loop
for i in range(1,n+1): # creat a queue from 1 to n
    nqueue.put(i)

while nqueue.empty() is False: # loop until it is empty
    # >>>the first step is getting the next elimination position<<<
    position = (m - 1) % nqueue.qsize() + 1 # use remainder % to locate the next elimination position("-1" and "+1" is for the situation that m is a multiple of nqueue.rear)
    # >>>the second step is removing the person to the rear or the output queue<<<
    if nowposition != position: # when is not the eliminated one, just remove it to the rear
        nqueue.put(nqueue.get())
        nowposition += 1 # step to next position
    else: # when is the eliminated one, remove it to the output queue
        outqueue.put(nqueue.get())
        nowposition = 1 # back to the front position

out_list = []
while not outqueue.empty():
    out_list.append(outqueue.get())

print(f"Result of {n} people and {m} counts:")
print(f">>> SAFE Number: {out_list[-1]}")

# Made by Mike_Zhang
# https://ultrafish.io
