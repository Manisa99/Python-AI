#Set is created by {}
# It omits the duplicates data.Ex:{1,1,2} = {1,2}
list = [1, 3, 5, 6, 2, 1, 2, 5, 4]

set1 = set(list)

print(set1)

set2 = {4,5,0,2,1,2,4}

set2.remove(5)

set2.add(3)
print(set2)
print(len(set2))