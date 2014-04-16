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

def cc():
    l = [('name', 'OK'), ('age', 100)]
    dict(l)

def dd():
    dict(name='OK', age=100)

def ee():
    dict(**{'name': 'OK', 'age': 100})

print 'aa i[key]'
print timeit(aa)
# 1.03357291222

print 'bb i.update'
print timeit(bb)
# 1.62549996376

print timeit(cc)
print timeit(dd)
print timeit(ee)
