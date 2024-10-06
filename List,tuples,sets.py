c = ['math','cse','geo','com']

print(c[-1])
print(c[0:3])
print(c[2:])
c.append('art')
print(c)
c.insert(0, 'song')
print(c)

c2=['fan','wood']

c.extend(c2)
print(c)

c.remove('math')
print(c)

pooped = c.pop()
print(pooped) 

print(c)
c.pop()
print(c)

c.reverse()
print(c)

c.sort()
print(c)

c3=[1,6,4,2,3,5]

c3.sort()
print(c3)

c3.sort(reverse=True)
print(c3)

c4=[2,1,3]
sorted_list = sorted(c4)
print(sorted_list)

print(c.index('cse'))

print('cse' in c)
print('ABC' in c) 

for index, item in enumerate(c, start =1):
    print(index, item)


c_str = ' - '.join(c)
print(c_str)

sc_courses={'math','science','cse'}
art_courses={'math','science','craft'}
print(sc_courses.intersection(art_courses))
print(sc_courses.difference(art_courses))
print(sc_courses.union(art_courses))