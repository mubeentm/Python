"named Tuple - It returns a tuple with named entity"

from collections import namedtuple,deque, ChainMap, Counter, OrderedDict,defaultdict
'''
courses = namedtuple('course',['name','tech'])#initializing the named tuple
clist=courses(name='datascience',tech='python')#Assigning the value
print(clist[0])#Accessing the value by index
print(clist.name)#Accessing the value by attribute name
print(getattr(clist,"tech"))#Accesing the value by getattribute method

courselist= ['web development','Angular']
print(courses._make(courselist))#converting the list to named tuple
'''

'Deque - it is the optimised list to perform inserion and deletion easily'
'''
team_list= ["Rohith","Virat","Hardik","Rahul"]
tqueue = deque(team_list)
print(tqueue)
tqueue.append("Rishab")
tqueue.appendleft("Siraj")
print("After append and append left",tqueue)
tqueue.pop()
print(tqueue)
tqueue.popleft()
print(tqueue)
'''

"chainmap - It us a dictionary like class which is able to make a singke view portfolio1.csv"
"""
tmodule_1 = {1:'Angular', 2:'Python'}
tmodule_2 = {3: "React", 4:"cloud computing", 5:"Devops"}
#we cant add two dictionaries
modulelist = ChainMap(tmodule_1,tmodule_2)
print(modulelist)
tmodule_3 = {6:"Fundamentals", 7:"Docker"}
updatedmodulelist=modulelist.new_child(tmodule_3)
print(updatedmodulelist)
print(updatedmodulelist.maps)
print()
print(list(updatedmodulelist.keys()))
print()
print(list(updatedmodulelist.values()))
updatedmodulelist
"""
'''
"Counter - it is a dictionary sub clas which is used to count hashable objects"
#provides no. of occurence of each values
Rohith_Scores = [70,89,170,270,200,100,100,70,50,89,60,50,200]
score_count=Counter(Rohith_Scores)
print(score_count)
print(score_count.keys())
print(score_count.values())
print(score_count.items())
'''
# tempod = OrderedDict()
tempod = defaultdict(int)
tempod[1] = "17.10"
tempod[2] = "20.00"
tempod[3] = "45.00"
print(tempod[4])