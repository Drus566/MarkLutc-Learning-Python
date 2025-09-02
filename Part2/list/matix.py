M = [[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]]
print(M)
col2 = [row[1] for row in M] # Собрать элементы столбце 2 
print(col2)

print([row[1] + 1 for row in M])

print([row[1] for row in M if row[1] % 2 == 0])

diag = [M[i][i] for i in [0, 1, 2]] # Собрать диагональ из матрицы
print(diag)

doubles = [c * 2 for c in 'spam'] # Повторить символы в строке
print(doubles)
