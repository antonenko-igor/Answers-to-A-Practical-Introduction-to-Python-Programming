LST = ['01265','12171', '23257', '34548', '45970', '56236', 
      '67324', '78084', '89872', '99414']

for i in range(10000,99000):
    flag = 0
    for c in range(10):     
        count = 0
        for r in range(5):                       
            if LST[c][r:r+1] == str(i)[r:r+1]:
                count = count + 1                              
        if count != 1:
            flag = 1
            break
    if flag == 0:
        print('The number is ', i)
"""
The idea is:
01265  12171  13257
30274  30274  30274 and so on.
-----  -----  -----
  х       х     х
  2       7     2
"""  