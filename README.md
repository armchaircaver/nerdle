# nerdle
helper program to solve nerdle

There are three python modules:

- nerdle_solution_generator.py : A program to generate all the possible solutions and create the script of a  python dictionary that contains all solutions. This takes about 1 minute to run, so it's worth pre-generating the list of possible solutions

- nerdledict.py : contains the dictionary created by nerdle_solution_generator.py. This dictionary is imported by nerdle_helper.py

- nerdle_helper.py : a script to calculate the best option for the next line based on the lines entered so far 
