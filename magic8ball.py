# Python Assignment
# Mikal Abu Omar, 000784979
# assignment.txt has to be in the same directory as the assignment.py

import random
import time

with open("assignment.txt") as x:
    answer = x.read()

answer = answer.split('|')

print(
"""  __  __          _____ _____ _____    ___    ____          _      _      
 |  \/  |   /\   / ____|_   _/ ____|  / _ \  |  _ \   /\   | |    | |     
 | \  / |  /  \ | |  __  | || |      | (_) | | |_) | /  \  | |    | |     
 | |\/| | / /\ \| | |_ | | || |       > _ <  |  _ < / /\ \ | |    | |     
 | |  | |/ ____ \ |__| |_| || |____  | (_) | | |_) / ____ \| |____| |____ 
 |_|  |_/_/    \_\_____|_____\_____|  \___/  |____/_/    \_\______|______|
                                                                          
                                                                          """)
question = input("Ask a question to the magic 8 ball \n")

print("The Ball is thinking")
time.sleep(4)

print(random.choice(answer))