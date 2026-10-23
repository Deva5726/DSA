a = [2, 4, 4, 5, 1, 3, 6, 8]
visited = []
o=[]
result=[]

for i in range(len(a)):
    # Check if we haven't processed this element yet
    if a[i] not in visited:
        visited.append(a[i])  # Mark it as visited
        count = 0
        
        # Count its occurrences across the whole array
        for j in range(len(a)):
            if a[i] == a[j]:
                count += 1
        o.append(count)
        result.append([a[i],count])
print("count : ")
print(o)
print("original array :")
print(visited)
print("count in Horizontal")
print(result)
print("count in vertical : ")
for pair in result:
    print(pair)

                
        # print(f"Element {a[i]} occurs {count} time(s)")