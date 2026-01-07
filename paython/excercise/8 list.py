lit=['The Easy Learn',32,12.4,False,"The Esay Learn"]
lit1=[1,2,3,4,5]

#print complete list
print(lit)

#print first element of the list
print(lit[0])

#print element string from 1st till 3rd
print(lit[0:3])

#print element string from 2nd element 
print(lit[1:])

#print lit two times
print(lit*2)

#print concatenated lists
print(lit+lit1)

lit.append(0)
print(lit)

lit1.extend([1,2,3])
print(lit1)

lit.insert(2,"hi")
print(lit)

lit.remove("hi")
lit.remove(12.4)
print(lit)

print(lit.pop(2))

lit1.clear()
print(lit1)

print(lit.index(" The Easy Learn"))

print(lit.count("The Easy Learn"))
 