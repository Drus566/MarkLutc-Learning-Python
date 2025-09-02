M = [[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]

print({sum(row) for row in M}) # создать множество сумм элементов в строках
# {24, 6, 15}

print({i : sum(M[i]) for i in range(3)}) # создать словарь сумм элементов в строках 
# {0: 6, 1: 15, 2: 24}

print([ord(x) for x in 'spaam']) # Список числовых значений символов

print({ord(x) for x in 'spaam'}) # Множество с удаленными дубликатами

print({x: ord(x) for x in 'spaam'}) # Словарь с уникальными ключами

print((ord(x) for x in 'spaam')) # генератор значений
