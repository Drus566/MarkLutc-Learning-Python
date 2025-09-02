D = {}
D['name'] = 'Bob'
D['job'] = 'dev'
D['age'] = 40
print(D)

bob1 = dict(name='Bob', job='dev', age=40)
print(bob1)

bob2 = dict(zip(['name', 'job', 'age'], ['Bob', 'dev', 40]))
print(bob2)