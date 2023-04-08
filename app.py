# AUTHOR: TYLER WILSON 100773241
# ASSIGNMENT: TEST 2
# FILENAME: APP.PY
# PURPOSE: RUN THE PROGRAM FROM HERE. THIS IS THE MAIN
#
# 
# 
# 

import classes
import random
import csv
from datetime import datetime
from bitstring import BitArray

GENERATIONS = 5

# this creates a unique output file everytime you run this program
#  the filename is based on my credentials with the now() tagged on 
#  the end.

file_tag_time = datetime.now()
file_tag_str = file_tag_time.strftime("%d%m%Y%H%M%S")
filename = "Tyler Wilson 100773241 GA output - " + file_tag_str + ".csv"
current_out_file = open(filename, 'a')
current_out_file.close()
stars = "***************************************"


def main():


    # report_this("We need more stuff", filename)

    rprint("app started!")
    peeps = []
    gen = []
    rprint("INITIAL GENERATION" + stars + "\n")
    for i in range(6):
        peeps.append(Initial_peep_maker())

    gen.append(classes.Generation(peeps))

    rprint("INITIAL PEEPS" + stars + "\n")
    for r in range(6):
        rprint(gen[0].peeps[r])

    
    rprint(gen[0].parents[0])
    rprint(gen[0].parents[0].child1)
    rprint(gen[0].parents[0].child2)
    rprint("\n")
    rprint(gen[0].parents[1])
    rprint(gen[0].parents[1].child1)
    rprint(gen[0].parents[1].child2)
    rprint("\n")
    rprint(gen[0].parents[2])
    rprint(gen[0].parents[2].child1)
    rprint(gen[0].parents[2].child2)

    # THERE IS AN INITIAL GENERATION WHICH COUNTS AS ONE
    #  THIS CREATES A LIST OF CHILDREN FROM LAST GENERATION TO 
    #  ADD TO THE NEXT GENERATION. i IS ALWAYS THE 
    #  LAST GENERATION
    #  
    for i in range(0,GENERATIONS):
        peeps = []
        peeps.append(gen[i].parents[0].child1)
        peeps.append(gen[i].parents[0].child2)
        peeps.append(gen[i].parents[1].child1)
        peeps.append(gen[i].parents[1].child2)
        peeps.append(gen[i].parents[2].child1)
        peeps.append(gen[i].parents[2].child2)

        rprint("\n GENERATION " + str(i+2) + stars + "\n")
        # PASSING THE LAST GENERATION OF CHILDREN TO THIS GENERATION
        gen.append(classes.Generation(peeps))

        rprint("PEEPS FROM LAST GENERATION" + stars + "\n")
        # LISTING THE PEEPS IN THIS GENERATION
        for r in range(6):
            rprint(peeps[r])

        # LISTING OUT THE FAMILIES, AND CHILDREN CREATED THIS GEN
        rprint(gen[i+1].parents[0])
        rprint(gen[i+1].parents[0].child1)
        rprint(gen[i+1].parents[0].child2)
        rprint("\n")
        rprint(gen[i+1].parents[1])
        rprint(gen[i+1].parents[1].child1)
        rprint(gen[i+1].parents[1].child2)
        rprint("\n")
        rprint(gen[i+1].parents[2])
        rprint(gen[i+1].parents[2].child1)
        rprint(gen[i+1].parents[2].child2)

# GENERATING PEOPLE FOR THE 1ST/INITIAL GENERATION
def Initial_peep_maker():
        
    randomint = random.randint(1, 255) # random decimal fon converting to 8 bit binary
    code = int(randomint)
    # print(code)
    chromasome = bin(randomint)[2:].zfill(8)  # Convert to binary and remove the '0b' prefix
    # print(chromasome)
    
    sex = classes.get_peep_sex()
    name = classes.get_peep_name(sex)
    peep = classes.Peep(name['fname'], name['lname'], chromasome, sex, int(code))
    return peep

# replacement for PRINT() that will always output to the 
# .csv file created at the start of the program.
def rprint(stuff):
    report_this(str(stuff), filename)

#  for opening an writing to the .csv file created at the 
# program. File name is a global variable created above.
def report_this(row, filename):
    with open(filename, 'a') as f:
        f.write(row + "\n")

             
if __name__ == "__main__":
    main()
