arr = [10 , 20 , 30 , 40 , 50 ]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print(f"smallest ={smallest}")