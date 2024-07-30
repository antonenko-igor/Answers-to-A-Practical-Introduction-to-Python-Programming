L = ["January","February","March","April","May","June","July","August",
    "September","Oktober","November","December"]
d = input("Enter a date in the format mm/dd/yy:  ")
a = d.split("/")
print(L[int(a[0])-1],int(a[1]),",","19" + a[2]) 