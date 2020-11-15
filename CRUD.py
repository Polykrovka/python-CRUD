import json

try:
    save = open('save.json', 'x')
except FileExistsError:
    print(end='')
save = open('save.json', 'r')
f = save.read()
save.close()
if f == '':
    files = dict()
else:
    f = json.loads(f)
    files = f

def create():
    file = input('Введите желаемое имя файла: ')
    while file in files:
        file = input('Файл "'+ file + '" уже сущевствует, введите другое имя или команду "back" что бы вернуться или команду "list", что бы посмотреть список всех файлов: ')
        if file == 'back':
            break
        elif file == 'list':
            list()
            create()
            break
    else:
        files[file] = input('Введите данные: ')
def read():
    file = input('Введите имя файла: ')
    while file not in files:
        file = input('Нет файла с именем "'+ file + '", введите другое имя или команду "back" что бы вернуться или команду "list", что бы посмотреть список всех файлов: ')
        if file == 'back':
            break
        elif file == 'list':
            list()
            read()
            break
    else:
        print(files[file])
def delite():
    file = input('Введите имя файла: ')
    while file not in files:
        file = input('Нет файла с именем "'+ file + '", введите другое имя или команду "back" что бы вернуться или команду "list", что бы посмотреть список всех файлов: ')
        if file == 'back':
            break
        elif file == 'list':
            list()
            delite()
            break
    else:
        del files[file]
        print('Файл "'+ file +'" удалён.')
def update():
    file = input('Введите имя файла: ')
    while file not in files:
        file = input('Нет файла с именем "'+ file + '", введите другое имя или команду "back" ,что бы вернуться или команду "list", что бы посмотреть список всех файлов: ')
        if file == 'back':
            break
        elif file == 'list':
            list()
            update()
            break
    else:
        files[file] = input('Введите новые данные: ')
def list():
    for file in files:
        print(file, end=' ')
    print('')


x = 0
print('Введите "help" что бы увидеть список доступных команд')
while x != 'exit':
    x = input('Введите команду: ')
    if x == 'create':
        create()
    elif x == 'read':
        read()
    elif x == 'delite' or x == 'del':
        delite()
    elif x == 'update':
        update()
    elif x == 'list':
        list()
    elif x == 'help':
        print('Доступные команды:', '\ncreate - создать новый файл', '\nread - прочитать(открыть) файл', '\ndel или delite - удалить файл', \
              '\nupdate - перезаписать файл', '\nlist - вывести список файлов', '\nexit - завершить программу')
    elif x == 'exit':
        break
    else:
        print('Неизвестная команда: ', x)
y = json.dumps(files, ensure_ascii=False)
save = open('save.json', 'w+')
save.write(y)
save.close()
