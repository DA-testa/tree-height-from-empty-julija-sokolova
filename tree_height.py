# python3

import sys
import threading


def compute_height(n, parents):
    dop={}
    def height(i):
        if i in dop:
            return dop[i]
        if i==-1:
            return 0
        h=1+height(parents[i])
        dop[i]=h
        return h
    max_height=0
    for i in range(n):
        max_height=max(max_height, height(i))
    return max_height


def main():
    b=input()
    if "I" in b:
        c=input()
        put=list(map(int,input().split()))
        print(computer_height(put))
    if "F" in b:
        files=input()
        if "a" not in b:
            with open("./test/"+files) as file:
            g=int(file.readline())
            output=list(map(int, file.readline().split()))
            print(compute_height(output))              
            
            
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
