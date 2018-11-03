import time, random

# If the timer value is 0 or negative, print an error message and 
# return without doing anything. Assume all inputs will be integer values.

def timer(n):
    'Counts from n to 0 recursively and waits 1 second per count.'

    if n <= 0:
        print("Error!  Input must be > 0.")
        return 0 
        
    elif n == 1:
        print(n)
        time.sleep(1)
        print('Timer Done')

    else:
        print(n)
        time.sleep(1)
        timer(n-1)

timer(3)
