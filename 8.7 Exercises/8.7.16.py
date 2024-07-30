n = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]

L = [(n[i+1]-n[i]) for i in range(len(n)-1)]
print(L)
print("The maximum gap size - ",max(L) )
print("The percentage of gaps that have size 2: ",(L.count(2)/len(L))*100) 