from timeit import timeit

def aa():
    l = [{'name': 'toomore', 'age': 29}, {'name': 'lylon', 'age': 28}]

    for i in l:
        i['name'] = 'OK'
        i['age'] = 100

def bb():
    l = [{'name': 'toomore'}, {'name': 'lylon'}]

    for i in l:
        i.update({'name': 'OK', 'age': 100})

print 'aa i[key]'
print timeit(aa)

print 'bb i.update'
print timeit(bb)
