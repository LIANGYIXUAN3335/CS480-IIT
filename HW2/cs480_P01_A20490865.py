import numpy as np
import time
import sys

numberOfArgumentsPassedFromCommandLine = len(sys.argv)
print("Number of arguments passed (including your script name):", numberOfArgumentsPassedFromCommandLine)

# Arguments passed
firstArgument = sys.argv[0]
print("\nScript name:", sys.argv[0])

secondArgument = sys.argv[1]
print("\nINITIAL state:", secondArgument)

thirdArgument = sys.argv[2]
print("\nGOAL state:", thirdArgument)
def main(initial,end):
    global straightline
    straightline = "./straightline.csv"
    straightline = np.loadtxt(straightline, str, delimiter=',')
    driving = "./driving.csv"
    driving = np.loadtxt(driving, str, delimiter=',')
    index = 0
    global edge
    edge = []
    try:
        a,b =initial, end
    except:
        print("ERROR: Not enough or too many input arguments.")
    for i in range(len(straightline[0])):
        if b ==straightline[0][i]:
            index =i
            break
    straightline=straightline[:50,(0,index)]
    for i in range(1,50):
        # print(straightline[i][1])
        straightline[i][1] =int(straightline[i][1])
    print("Initialstate:" +a)
    print("Goalstate:" +b)
    for i in range(1,50):
        for j in range(1,50):
            if int(driving[i][j]) != -1 and int(driving[i][j])!= 0:
                edge.append((driving[0][j],driving[i][0],int(driving[i][j])))
    Greedy_Best_First_Search(a,b)
    A_Search(a,b)

def Greedy_Best_First_Search(start,end):
    starttime1  = time.time()
    path = []
    path.append(start)
    path_cost = []
    already = []
    for i in range(50):
        path1 = []  # path1中存储该节点的连接城市
        distance1 = []  # distance1中存储该节点连接城市的距离
        for a in range(len(edge)):
            if edge[a][0] == path[-1] and edge[a][1] not in already:
                path1.append(edge[a][1])
                distance1.append(edge[a][-1])
        # 贪婪最优搜索
        already.append(start)
        min = 1000
        temp_path = " "
        temp_distance = 0
        # print(distance1)
        for b in range(len(path1)):
            if distance1[b] <int(min):
                min =distance1[b]
                temp_distance = distance1[b]
                temp_path = path1[b]
        path.append(temp_path)
        path_cost.append(temp_distance)
        already.append(temp_path)
        if temp_path == end or temp_path==" ":
            break
    endtime1= time.time()
    Execution_time = (endtime1*float(10^6))-(starttime1*float(10^6))
    if temp_path !=end:
        print("Solution path:FAILURE: NO PATH FOUND")
        print("Number of states on a path :"+str(len(path)))
        print("Path cost: " + str(sum(path_cost)))
        print("Execution time" + str(Execution_time) + " *10^-6 seconds")
    else:
        print("Greedy Best First Search:")
        print("Solution path:"+"-->".join(path))
        print("Number of states on a path: "+str(len(path)))
        print("Path cost: "+ str(sum(path_cost)))
        print("Execution time"+str(Execution_time)+" *10^-6 seconds")

def A_Search(start, end):
    starttime = time.time()
    path = []
    path_cost = []
    path.append(start)
    already = []
    for i in range(20):
        path1 = []  # path1中存储该节点的连接城市
        distance1 = []  # distance1中存储该节点连接城市的距离
        for a in range(len(edge)):
            if edge[a][0] == path[-1]:
                path1.append(edge[a][1])
                distance1.append(edge[a][-1])
        already.append(start)
        # A*搜索
        fxx = 1000
        temp_path = " "
        temp_distance = 0
        for b in range(len(path1)):
            for i in range(50):
                if straightline[i][0]==path1[b]:
                    ST = straightline[i][1]
                    fxx_min=distance1[b]+int(ST)
                    break
            # fxx_min = straightline[edge[a][1]][1] + distance1[b]
            if fxx_min < fxx:
                fxx = fxx_min
                temp_distance = distance1[b]
                temp_path = path1[b]
        path.append(temp_path)
        path_cost.append(temp_distance)
        already.append(temp_path)
        if temp_path == end or temp_path==" ":
            break
    endtime = time.time()
    Execution_time = endtime*float(10^6)-starttime*float(10^6)

    if temp_path !=end:
        print("Solution path:FAILURE: NO PATH FOUND")
        print("Number of states on a path :"+str(len(path)))
        print("Path cost: " + str(sum(path_cost)))
        print("Execution time" + str(Execution_time) + " *10^-6 seconds")
    else:
        print("A_ Search:")
        print("Solution path:"+"-->".join(path))
        print("Number of states on a path: "+str(len(path)))
        print("Path cost: "+ str(sum(path_cost)))
        print("Execution time" + str(Execution_time) + " *10^-6 seconds")
main(sys.argv[1],sys.argv[2])