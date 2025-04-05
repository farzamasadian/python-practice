distance=input()
distance=distance.split() 
n=0
distance=[int(i) for i in distance]
distance.sort()
print(distance[len(distance)-1]-distance[0])
