def FindLiars(N:int, answerMatrix:list):
    answer_dict = {}
    index = 0
    # using the response given by each student as key, and collect indicies into a list as value
    for answer in answerMatrix:
        if answer in answer_dict:
            answer_dict[answer].append(index)
        else:
            answer_dict[answer] = [index]
        index+=1
    
    truthTeller = [False] * (N+1) 
    # if truthTeller[i]=True, then it means it is possilbe to have i truth teller based
    # the answer matrix
    truthTeller[0]=True #always assume we have 0 truth teller in the beginning

    for key in answer_dict:
        #suppose we have a key TLTLT, since it has 3 T, and T occuers at index 0,2,4
        #if the corresponding value for key TLTLT is list [0,2,4] then we can claim it is possilbe
        #that there exist 3 truth teller, because student 0,2,4 are claiming they are truth teller and
        #indeed they are telling truth since their claim mathchs.

        #However, if the list in the value does not match the index T occurs in the key, then it must be
        #the case that this statement "there are 3 truth teller and they are student 0,2,4" is false

        #Moreover, their are 0 truth teller if and only if the key that a row does not contain any T (eg "LLLLL")
        #does not occur in the dictionary

        #This is just a brief justification of the approach, a formal proof can be done using induction
        truth_index = [] #the expected truth teller index based on key
        t=0
        all_L = True
        for char in key:
            if char == 'T':
                truth_index.append(t)
                all_L=False
            t+=1
        if (all_L): #if there is a key with no T in it, then we cannot have 0 truth teller
            truthTeller[0] = False
        elif (len(truth_index) == len(answer_dict[key])): #if their length does not match, then we cannot claim this key as truth
            all_match = True
            l = len(truth_index)
            for i in range(0,l):
                if truth_index[i]!=answer_dict[key][i]:
                    all_match = False
                    break
            if (all_match):
                truthTeller[l]=True # it is possilbe to have l truth teller since this key can be a truth

    min_truth = -1
    max_truth = -1
    for i in range(0, N+1):
        if (min_truth==-1) and (truthTeller[i]):
            min_truth=i
        if (truthTeller[i]):
            max_truth=i
    
    if(min_truth==-1):#there are no any number of truth teller, then this is a paradox
        print("is paradoxical")
    else:
        print("contains atleast "+ str((N-max_truth))+ " and atmost "+ str((N-min_truth))+ " liars")

classroom_num = int(input())
classrooms = []
for i in range(0,classroom_num):
    size = int(input())
    answer_matrix = []
    for j in range(0,size):
        response = input()
        answer_matrix.append(response)
    classroom = [size, answer_matrix]
    classrooms.append(classroom)
for i in range(0, classroom_num):
    print("Class Room#"+str(i+1),end=" ")
    FindLiars(classrooms[i][0],classrooms[i][1])


