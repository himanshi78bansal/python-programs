starting = int(input("Table from : "))
ending = int(input("Table to : "))
for row in range(1,11):
    for col in range(starting,ending+1):
        print(row*col
              ,end="\t")
    print("\n")


