f = open('data.txt', 'w')
f.write('Hello\n')
f.write('world\n')
f.close()

f = open('text.txt')
text = f.read()
print(text)
print(text.split())

for line in open('text.txt'): print(line)