print("""The example of the magic square   
       [[8,11,14,1],
       [13,2,7,12],
       [3,16,9, 6],
       [10,5,4,15]]""")

L = eval(input("Enter a 4x4 list to check "))

D1 = []
for i in range(4):
    D1.append(L[i][i])

D2 = []
for i in range(4):
     D2.append(L[3-i][0+i])

if sum(D1) == sum(D2):
     if sum(L[0]) == sum(L[1]) == sum (L[2]) == sum(L[3]):
          V = []
          for i in range(4):
               v = []
               for j in range(4):
                    v.append(L[j][i])
               V.append(v)
          if sum(V[0]) == sum(V[1]) == sum (V[2]) == sum(V[3]):
               print("The magic square.")
          else:
               print("No the magic square!")
     else:
          print("No the magic square!")
else:
     print("No the magic square!") 