import time
limit=int(input("Enter the limit: "))
def countdown(n):
    if (n==0):
        print("times up")
    else:
        print(n)
        print("*"*n)
        time.sleep(n)
        countdown(n-1)
countdown(limit)