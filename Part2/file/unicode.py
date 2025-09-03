S = 'sp\xc4m'
print(S)
print(S[2])

file = open('unidata.txt', 'w', encoding='utf-8') # Записать/ закодировать текст UTF-8
file.write(S)
file.close()

text = open('unidata.txt', encoding='utf-8').read() # Прочитать декодировать текст UTF-8
print(text)
print(len(text))

raw = open('unidata.txt', 'rb').read() # читать закодированные байты
print(raw)
print(len(raw))

print(text.encode('utf-8')) # вручную кодировать в байты
print(raw.decode('utf-8')) # вручную декодировать в строк

# Если переводить текст в другие кодировки, то конечно байты будут отличаться 
print(text.encode('latin-1')) 
print(text.encode('utf-16'))
print(len(text.encode('latin-1')),len(text.encode('utf-16')))
print(b'\xff\xfes\x00p\x00\xc4\x00m\x00'.decode('utf-16')) # Но декодируется в ту же самую строку:w
