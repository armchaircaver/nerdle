# nerdle
helper program to solve nerdle

There are three python modules:

- nerdle_solution_generator.py : A program to generate all the possible solutions and create the script of a  python dictionary that contains all solutions. This takes about 1 minute to run, so it's worth pre-generating the list of possible solutions

- nerdledict.py : contains the dictionary created by nerdle_solution_generator.py. This dictionary is imported by nerdle_helper.py

- nerdle_helper.py : a script to calculate the best option for the next line based on the lines entered so far 

The solution generator makes a few assumptions about what constitutes a valid solution:

- the first number is positive. e.g. -5+4+3=2 is not allowed

- none of the components of the expression on the left side of the equation is zero

- multiplication by 1 is not allowed in the expression

- division by 1 is not allowed in the expression
- the right hand side isn't negative
