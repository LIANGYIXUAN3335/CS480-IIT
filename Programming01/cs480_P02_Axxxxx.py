import numpy as np
import sys
from copy import deepcopy
ByHand = False # set StartState and GoalState by hands or from sys IO
ValidInput = False # to check inputs
if ByHand: # set StartState and GoalState by hands
    ValidInput = True
    StartState = 'OK'
    NumOfParks = 11
else: #from sys IO
    if len(sys.argv) == 3:
        ValidInput = True
        StartState = sys.argv[1]
        NumOfParksChar = sys.argv[2]
        NumOfParks = int(NumOfParksChar)
if not ValidInput:
    print('Yixuan,Liang, A20490865 solution: ')
    print('ERROR: Not enough or too many input arguments.')
    sys.exit(0)
else:
    # GET THE INFORMATION FROM CSV FILES
    parks = "./parks.csv"
    parks = np.loadtxt(parks, str, delimiter=',')
    driving2 = "./driving2.csv"
    driving2 = np.loadtxt(driving2, str, delimiter=',')
    zones = "./zones.csv"
    zones = np.loadtxt(zones, str, delimiter=',')
    statenum = len(driving2[0])
    # GET THE INFORMATION FROM zones AND STORE IT AS {'NY': 0, 'ND': 1, 'IA': 0,
    state_zones = {}
    for i in range(1,len(zones[0])):
        state_zones[zones[0][i]] = eval(zones[1][i])
    # GET THE INFORMATION FROM DRIVINGS AND STORE IT AS {'RI': [('CT', 87), ('MA', 50)],......
    state_road = {}
    for i in range(1,statenum):
        state = driving2[0][i]
        list = []
        # the domain should be in next zone use ,filtrate the value that not meet this requirement
        for j in range(1,len(driving2[0])):
            if driving2[i][j] !="-1" and driving2[i][j]!="0" and state_zones[driving2[0][j]]==state_zones[driving2[0][i]]+1:
                list.append((driving2[0][j],eval(driving2[i][j])))
        # sort the domain in Alphabetical order
        list.sort(key=lambda x: x[0],reverse=False)
        state_road[state]=list
    state_road1 ={}
    state_road1 =deepcopy(state_road)

    #GET THE INFORMATION FROM PARKS AND STORE IT AS {'NY': 0, 'ND': 1, 'IA': 0,
    state_parks = {}
    for i in range(1,statenum):
        state_parks[parks[0][i]] = eval(parks[1][i])
    initial = StartState
    NO_OF_PARKS = NumOfParks
    assignment =[initial]
def main():
    print('Yixuan,Liang, A20490865 solution: ')
    print('Initial state:', StartState )
    print('Minimum number of parks:' , NumOfParks )
    # GET THE SOLUTION
    ROAD = backtrack_search(assignment)
    if ROAD != "no correct road":
        path_cost =0
        for i in range(len(ROAD)-1):
            for j in state_road[ROAD[i]]:
                if j[0] == ROAD[i+1]:
                    path_cost+= j[1]
        PARKS_VISITED =0
        for k in ROAD:
            PARKS_VISITED+=state_parks[k]
        ROAD1 = " ".join(ROAD)
        print('Solution path: ', ROAD1)
        print('Number of states on a path: ', len(ROAD))
        print('Path cost: ', path_cost)
        print('Number of national parks visited: ', PARKS_VISITED)
    else:
        print('Solution path: FAILURE: NO PATH FOUND')
        print('Number of states on a path: ', 0)
        print('Path cost: ', 0)
        print('Number of national parks visited: ', 0)
def backtrack_search(assignment):
    list =[]# store the state that domain be cleared
    return backtrack(assignment,list)

def ORDER_DOMAIN_VALUES(variable,list):
    while len(list) >= 2:
        key = list[0]
        state_road[key] = state_road1[key]
        list.pop(0)
    return state_road[variable]

def is_complete(assignment):
    if assignment[-1] not in ["WA","OR","NV","CA"] :
        return False
    else:
        park_num = 0
        for i in assignment:
            park_num += state_parks[i]
        if park_num<NO_OF_PARKS:
            return False
        else:
            return True
def backtrack(assignment,list):
    if is_complete(assignment)==True:
        return assignment
    else:
        #if there is no state to go ,then delete the last state and backtrack
        if state_road[assignment[-1]]==[] and len(assignment)>1:
            list.append(assignment[-1])
            state_road[assignment[-2]].pop(0)
            assignment.pop(-1)
            backtrack(assignment,list)
        # if there is no state to go and only inital state left that means no road
        # meeting the requirement
        elif state_road[assignment[-1]]==[] and len(assignment)==1:
            return "no correct road"
        # if the domain of next state is not null ,then traverse the domain
        # until find the correct answer
        else:
            for value in ORDER_DOMAIN_VALUES(assignment[-1],list):
                assignment.append(value[0])
                result = backtrack(assignment,list)
                if result != "failure":
                    return backtrack(assignment,list)
                    break
                else:
                    state_road[assignment[-1]].pop(0)
                    assignment.pop(-1)
                    backtrack(assignment,list)
            return "failure"
main()
