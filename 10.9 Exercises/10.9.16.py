num = eval(input("Enter a decimal height in feet:  "))
d_num = int(num)
f_num = num - d_num
print(d_num,"feet",",", "{:.2f}".format(f_num*12),"inches"  ) 