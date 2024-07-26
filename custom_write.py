def custom_write(file_name, strings):
    nomber_str = 0
    result = {}
    with open(file_name, 'w',  encoding='UTF-8') as f:
        for i in strings:
            f_tell = f.tell()
            f.write(i)
            f.write('\n')
            nomber_str +=1
            result[(nomber_str, f_tell)]= i
    return result
            #print((nomber_str, f_tell), i)


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)


