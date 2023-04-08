# AUTHOR: TYLER WILSON 100773241
# ASSIGNMENT: TEST 2
# FILENAME: CLASSES.PY
# PURPOSE: A PLACE TO PUT MY CLASSES SO THEY ARE
#           OUT OF THE WAY
#
# 
# 
# 

import random
import names
from math import sqrt



# INITIAL POPULATION
NUM_IDS = 6 # CHOOSE AN EVEN NUMBER SO WE CAN MAKE PAIRS OF PEEPS CALLED COUPLES
MUTATION_CHANCE = 90
CROSSOVER_THRESHOLD = 50


# Making parent groups
class Parentals():
    def __init__(self, mom, dad):
        self.mom = mom
        self.dad = dad
        # print(self.dad.lastName)
        self.child1 = self.Babymaker(self.dad.chromasome)
        self.child2 = self.Babymaker(self.mom.chromasome)
        self.lastname = self.dad.lastName
    def __str__(self):
        return "Family {} \nMom: {} \nDad: {} \nCHILDREN\n".format(self.lastname, self.mom, self.dad)
    
    # making baby peeps
    def Babymaker(self, OG_chromasome): 
        
        # randomly crossing over genes
        def cross_over(self, OG_chromasome):
            if (random.randint(1,100) < CROSSOVER_THRESHOLD):
                # CROSSING OVER
                momside = self.mom.chromasome[4:]
                dadside = self.dad.chromasome[:4]
                new_chromasome = str(momside + dadside)
                # print("this is the new chromasome " + new_chromasome)
                return new_chromasome
            else:
                return OG_chromasome
        
        # randomly mutating a gene
        def mutation(self, OG_chromasome):
            if (random.randint(1,100) < MUTATION_CHANCE):
                chromasome_position_to_mutate = random.randint(0,7)
                temp = list(OG_chromasome)

                if(OG_chromasome[chromasome_position_to_mutate]=="1"):
                    temp[chromasome_position_to_mutate]="0"
                else:
                    temp[chromasome_position_to_mutate]="1"

                return "".join(temp)
            else:
                return OG_chromasome

        og_chromasome = OG_chromasome
        sex = get_peep_sex()
        name = get_peep_name(sex)
        l_name = self.dad.lastName

        new_chromasome = cross_over(self, og_chromasome)
        new_chromasome = mutation(self, new_chromasome)

        new_code = int(new_chromasome,2)
        # print(new_code)


        new_kid = Peep(name['fname'], l_name, new_chromasome, sex, new_code)

        return new_kid
            # return new_peep()

class Peep():
    def __init__(self, firstname, lastname, chromasome, sex, code):
        self.firstName = firstname
        self.lastName = lastname
        self.chromasome = chromasome
        self.fitness = sqrt(((code * 15) - (code)**2)**2)
        self.sex = sex
        self.code = code
        self.fitnessRatio = 0.0 #property(fget = self.get_fitnessRatio, fset = self.set_fitnessRatio)
        self.roulette = 0.0 #property(fget = self.get_roulette, fset = self.set_roulette)

    def __str__(self):
        return "{} - {} {} {} \nCode - {}, fitness - {}, ratio - {}, roulette - {}\n".format(self.sex, self.firstName, self.lastName, str(self.chromasome),
                                      self.code, self.fitness, self.fitnessRatio, self.roulette )

    # FITNESS RATIOS
    def set_fitnessRatio(self, ratio):
        self.fitnessRatio = ratio

    def get_fitnessRatio(self):
        return self.fitnessRatio
    
    # ROULETTE RANGE
    def set_roulette(self, roulette):
        self.roulette = roulette

    def get_roulette(self):
        return self.roulette

class Generation():

    def __init__(self, peeps ):
        
        self.parents=[]
        x=0
        # IMPORTING LIST OF PEEPS TO THIS GEN
        self.peeps = peeps
        _upper_range = len(self.peeps)-1

        fitness_total = 0
        
        # getting the total fitness of the peeps
        for i in range(0,_upper_range):
            fitness_total += self.peeps[i].fitness


        # calculating fitness ratio and roulette for each peep
        for i in range(0,_upper_range+1):  
            new_fitness_ratio = round(((self.peeps[i].fitness / fitness_total)*100),2)
            self.peeps[i].set_fitnessRatio(new_fitness_ratio)  
 
        for i in range(1,_upper_range+1):
            self.peeps[i].set_roulette(new_fitness_ratio)
        
        for i in range(0,_upper_range+1,2):
            
        # shuffle peeps and create parents
            roll = random.randint(1,100)
            
            for i in range(0,5):
                if roll >= self.peeps[i].roulette:
                    chosen_one1 = i

            for i in range(0,5):
                if roll >= self.peeps[i].roulette:
                    chosen_one2 = i

            self.parents.append(Parentals(self.peeps[chosen_one1], self.peeps[chosen_one2]))
            x = x + 1

    
def get_peep_sex():
    selected_sex = random.randint(0,1)
    if selected_sex == 1:
        peep_sex = "M"
    else:
        peep_sex = "F"
    return peep_sex

def get_peep_name(peep_sex):
    if peep_sex == "M":
        firstname = names.get_first_name(gender='male')
    else:
        firstname = names.get_first_name(gender='female')
    
    lastname = names.get_last_name()
    return {"fname":firstname, "lname":lastname}
