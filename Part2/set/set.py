X = set('spam')
Y = {'h','a','m'}

print(X, Y)
print(X & Y)
print(X | Y)
print(X - Y)
print(X > Y)

print({n ** 2 for n in [1,2,3,4]}) # включения множеств

print(list(set([1,2,1,3,1]))) # фильтрация дубликатов
print(set('spam') - set('ham')) # нахождение разностей
print(set('spam') == set('asmp')) # нейтральная к порядку проверка символов

print('p' in set('spam'))
print('p' in set('spam'), 'p' in 'spam', 'ham' in ['eggs', 'spam', 'ham'])