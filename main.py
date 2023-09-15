import os

# Указываем путь к папке с файлами
print('\n===== Программа для удаления строк из дериктории с папками и файлами в них =====')

way = input('\nВведите путь к папке (Мой путь - C:\\Users\\golde\\OneDrive\\Рабочий стол\\employees): ')
folder_path = fr"{way}"
# ТЕСТИРОВАЛ С ЭТИМ - C:\Users\golde\OneDrive\Рабочий стол\employees

filename_in_folders = input('\nВведите названия одного похожего файла в ваших папках (index.html): ')
# ТАКОЙ ФАЙЛ БЫЛ ВО ВСЕХ ПАПКАХ - index.html

first_line = int(input('\nС какой строки удалить (у меня было с 11)? '))
end_line = int(input('\nДо какой строки удалить (до 29)? '))

try:
    # Проходимся по всем папкам внутри указанной папки
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            # Если файл называется index.html
            if filename == f'{filename_in_folders}':
                # Составляем полный путь к файлу
                file_path = os.path.join(dirpath, filename)
                # Открываем файл на чтение и запись
                with open(file_path, 'r', encoding='cp1251') as file_read:
                    # Читаем все строки файла в список
                    lines = file_read.readlines()
                # Удаляем строки с 12 по 29
                # del lines[11:29]
                del lines[first_line:end_line]  # Но сейчас на выбор есть возможность.
                # Открываем файл на запись
                with open(file_path, 'w', encoding='cp1251') as file_write:
                    # Записываем все оставшиеся строки в файл
                    for line in lines:
                        file_write.write(line)
except Exception:
    pass
