# Imports necessary functions / libraries
import matplotlib.pyplot as plt
import time

# Starts an internal timer
start_time = time.time()

# Defines a function that calculates the collatz sequence and saves the numbers into a list
def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n%2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        sequence.append(n)
        print(n)
    return sequence

# Asks for input and takes in the variable (as an integer)
print('Please input a natural number')
initial_num = int(input())

# Calls the function with the input as a variable
seq = collatz_sequence(initial_num)

# Prints execution time accortding to the internal timer
print('---Time spent crunching numbers---')
print("--- %s seconds ---" % (time.time() - start_time))

# Plots the graph
plt.plot(range(len(seq)), seq, marker = 'o')
plt.title("Collatz Conjecture for Starting Value:" + str(initial_num))
plt.xlabel('X Value')
plt.ylabel('Y Value')
plt.grid (True)
plt.show()




