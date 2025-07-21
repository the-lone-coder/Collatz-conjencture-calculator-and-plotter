# Collatz conjencture calculator
    A simple python script with the simple purpose of calculating and plotting the values of an initial number using the Collatz conjencture.
# What is the Collatz conjencture
    The Collatz conjecture is one of the most famous unsolved problems in mathematics. The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. 
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        (Source: https://en.wikipedia.org/wiki/Collatz_conjecture)

# How it works
    The script takes in a user given variable and checks whether it is odd, even or equal to 1.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        If it is odd, it multiplies the variable by 3 and adds 1 then adds the value into a list
        If it is even it divides the variable by 2 and adds the value to a list
        If it equal to 1 it just adds the value to the list without doing any calculations. (It would get stuck into a loop if it didn't do that)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Then it takes the values of the computation, and plots them using the earlier mentioned list for the values of the graph.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    After all the mathematical computations are finished it will output the time it took to crunch the numbers (without including the time it took to display the graph)
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Libraries used
## Matplotlib 
     Used for plotting the points (in code used as plt)
## Time  
     Used for displaying the time it took to do the math

# How to use
 ## The program is made to run on Linux machines only (for now)
### To download the code:
1. Open a terminal emulator    
2.  Use `cd` to move into the directory you want to keep the code in 
3. Use `git clone https://github.com/the-lone-coder/Collatz-conjencture-calculator-and-plotter.git` to clone the repository into said directory
4. Voilà! You now have the code stored into your computer.
### To execute the code:
1. Make sure you have the above mentioned libraries and python3 installed
2. Open a terminal emulator
3. Use `cd` to move into the directory where the main.py file is stored
4. When in the correct directory type `python3 main.py` and hit Enter to execute the program
5. Follow the instructions displayed and enjoy

## If you enjoyed
    Please check out my instagram: https://www.instagram.com/the_.lone._.coder