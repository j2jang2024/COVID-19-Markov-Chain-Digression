from random import random
from time import sleep

FRIENDS_MEET = 0.4
JUST_MEET = 0.3

SYMPTOM_MASK = 0.99
NO_SYMPTOM_MASK = 0.9
CIVIC_AWARENESS = 0.5

MASK_INF_OUT = 0.3
NO_MASK_INF_OUT = 1

MASK_SUS_IN = 0.5
NO_MASK_SUS_IN = 0.99

class Human:
    def __init__(self, state, city, friends, awareness):
        self.state = state
        self.city = city
        self.friends = friends
        self.awareness = awareness

    def progress(self):
        if self.state == 'e':
            if random()<0.05:
                self.state = 'i'
        if self.state == 'i':
            if random()<0.1:
                self.state = 'r'

def willMeet(h1,h2):
    if h2 in h1.friends:
        if random()<FRIENDS_MEET:
            return True
        return False
    else:
        if random()<JUST_MEET:
            return True
        return False

def willMask(h1):
    if h1.state == 'i':
        if random() < h1.awareness*SYMPTOM_MASK:
            return True
        return False
    else:
        if random() < h1.awareness*NO_SYMPTOM_MASK:
            return True
        return False

def willTransmit(inf_h, sus_h, inf_m, sus_m):
    if inf_m == True:
        if sus_m == True:
            if random() < MASK_INF_OUT*MASK_SUS_IN:
                return True
            return False
        else:
            if random() < MASK_INF_OUT*NO_MASK_SUS_IN:
                return True
            return False
    else:
        if sus_m == True:
            if random() < NO_MASK_INF_OUT*MASK_SUS_IN:
                return True
            return False
        else:
            if random() < NO_MASK_INF_OUT*NO_MASK_SUS_IN:
                return True
            return False

def initialize(n,m):
    humans = []
    for i in range(n):
        humans.append(Human('s','Seoul',[],0.1))
    for j in range(m):
        humans[j].state='e'
    return humans

def meetMatrix(humans):
    mM = []
    row = []
    for i in humans:
        row.append(False)
    for j in humans:
        mM.append(row)

    for i in range(len(humans)):
        for j in range(i):
            mM[i][j] = willMeet(humans[i], humans[j])
    return mM

def oneDay(humans):
    printHumans(humans)
    masks = []
    for human in humans:
        masks.append(willMask(human))

    for i in range(len(humans)):
        for j in range(i):
            if willMeet(humans[i],humans[j]):
                if humans[i].state in ['e','i'] and humans[j].state == 's':
                    if willTransmit(humans[i],humans[j],masks[i],masks[j]):
                        humans[j].state = 'e'
                        # exit()
                elif humans[j].state in ['e','i'] and humans[i].state == 's':
                    if willTransmit(humans[j],humans[i],masks[j],masks[i]):
                        humans[i].state = 'e'
                        # exit()
    for human in humans:
        human.progress()
    return humans    

def printHumans(humans):
    s = 0
    e = 0
    i = 0
    r = 0
    for human in humans:
        if human.state == 's':
            s += 1
        if human.state == 'e':
            e += 1
        if human.state == 'i':
            i += 1
        if human.state == 'r':
            r += 1
    print("Number of Healthy, Susceptible People:       %s"%s)
    print("Number of Exposed, No Symptom People:        %s"%e)
    print("Number of Infective, with Symptom People:    %s"%i)
    print("Number of Removed(Dead or Cured) People:     %s"%r)

# def oneDay():
#     John = Human('e', 'Seoul', [], 0.5)
#     Jane = Human('s', 'Seoul', [John], 0.5)
#     John.friends.append(Jane)

#     john_mask = willMask(John)
#     jane_mask = willMask(Jane)

#     they_met = willMeet(John, Jane)

#     if they_met:
#         if willTransmit(John, Jane, john_mask, jane_mask):
#             Jane.state = 'e'

#     John.progress()
#     Jane.progress()

humans = initialize(50, 5)
day = 0
while True:
    print("———————————————————————")
    print("Day: %s"%day)
    humans = oneDay(humans)
    sleep(0.1)
    day += 1

    death = 0
    for human in humans:
        if human.state in ["r","e","i"]:
            death+=1
    if death ==50:
        exit()