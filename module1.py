'''
type_of_accounts=("savings","current","credit","fixed","credit")
print(type_of_accounts.count("credit"))
print(type_of_accounts[::-1])
print(len(type_of_accounts))
print(type_of_accounts.index("current"))
print(type_of_accounts[1:3])
sorted_tuple=tuple(sorted(type_of_accounts))
print(sorted_tuple[::-1])
'''

c_teams=["india","pakistan","australia","srilanka","england"]
'''
print(c_teams.sort(),c_teams)
c_teams.append("bangladesh")
print(c_teams)
c_teams.insert(2,"nepal")
print(c_teams)
c_teams.extend(["westindies","usa"])
print(c_teams)
print(c_teams.pop())
print(c_teams)
# remove()-to remove the element from the list
'''
world_cups=[2,1,6,1,1]
index=1
for team,cup in zip(c_teams,world_cups):
    print("Team - ",index,team,"won" , cup, "world_cups")
    index+=1
fruits=['apple','oranges','grapes']
fruit=":".join(fruits)
print(fruit)
# world_cups.

example={1:2}
print(example[1])

print(example.get(1))