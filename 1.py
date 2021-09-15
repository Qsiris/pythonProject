# 2. Имеется файл с текстом на русском языке.
# Дать варианты переноса всех слов.
# Перенос возможен по следующим правилам:
# 1) переносятся либо остаются в конце строки не менее двух символов;
# 2) невозможен перенос перед буквами 'ь' и 'ъ';
# 3) слово должно иметь не менее двух слогов;
# 4) в оставшейся и переносимой частях слова должны быть гласные буквы.

def input_from_file(filename):
    # открытие файла и чтение из него
    f = open("1.txt", "r")
    text_source = f.read()
    f.close()
    return text_source


def clean_input(text_source):
    # создание алфавита для удаления лишнего из введенных данных
    d = [".", ",", ";", ":", "?", "!", "-"]
    # удаление лишних знаков из слов
    for i in range(len(d)):
        text_source = text_source.replace(d[i], "")

    # удаление лишних пробелов
    text_source = text_source.replace("  ", " ")
    # разделение ввода по пробелам между словами
    text_source = text_source.split(" ")
    return text_source


def make_list_of_unique_words(text_source):
    output = []
    for x in text_source:
        if x not in output:
            output.append(x)
    return output


def show_variants_of_warp(text_source):
    d = ['а', 'у', 'о', 'и', 'э', 'ы',
         'ю', 'е', 'ё', 'А', 'У', 'О',
         'И', 'Э', 'Ы', 'Ю', 'Е', 'Ё']
    for i in range(len(text_source)):
        # проверка наличия трех букв в слове
        if len(text_source[i]) < 3 and text_source.count(d[i]) < 2:
            for i in range(len(text_source)):
                j = 0
                while j <= len(text_source[i]):
                    if text_source[j, j + 2].count('ъ') == 1 and text_source[j, j + 2].count('ь') == 1:
                        j += 2
                    for i in range(len(d)):
                        if 0 < text_source[j, j + 2].count(d[i]) < 2:
                            print(f'{text_source[j, j + 2]} - {text_source[len(text_source[i], -1)]}')
                            j += 2
        else:
            print(f'Слово {text_source[i]} не имеет вариантов переноса!')


def main():
    text_source = input_from_file('1.txt')
    text_source = clean_input(text_source)
    text_source = make_list_of_unique_words(text_source)
    show_variants_of_warp(text_source)


main()
