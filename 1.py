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
         'ю', 'я', 'ё', 'e', 'А', 'У',
         'О', 'И', 'Э', 'Ы',
         'Ю', 'Я', 'Ё', 'E']
    for i in range(len(text_source)):
        # проверка наличия трех букв в слове
        if len(text_source[i]) >= 3:
            counter = 0
            for j in range(len(d)):
                counter += text_source[i].count(d[j])
                # проверка наличия двух слогов в слове
            if counter >= 2:
                print(f"Для слова '{text_source[i]}':")
                k = 0
                while k < len(text_source[i]) - 2:
                    temp = text_source[i]
                    if temp[k + 2:].count('ь') or temp[k + 2:].count('ъ'):
                        k += 1
                    # если перенос 1 символа то говорим что нету вариантов и выход из цикла
                    elif len(temp[k + 2:]) == 1:
                        print(f"Для слова '{text_source[i]}' нет варианта переносов!")
                        break
                    # если после переноса не останется хотябы одной гласное буквы пропуск
                    else:
                        print(f"{temp[0: k + 2]}-{temp[k + 2:]}")
                        k += 2
            else:
                print(f"Для слова '{text_source[i]}' нет вариантов переносов!")


def main():
    text_source = input_from_file('1.txt')
    text_source = clean_input(text_source)
    text_source = make_list_of_unique_words(text_source)
    show_variants_of_warp(text_source)


main()
