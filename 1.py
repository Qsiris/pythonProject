# 2. Имеется файл с текстом на русском языке.
# Дать варианты переноса всех слов.
# Перенос возможен по следующим правилам:
# 1) переносятся либо остаются в конце строки не менее двух символов;   +
# 2) невозможен перенос перед буквами 'ь' и 'ъ';                        +
# 3) слово должно иметь не менее двух слогов;                           +
# 4) в оставшейся и переносимой частях слова должны быть гласные буквы.


def input_from_file(filename):
    # открытие файла и чтение из него
    f = open(filename, "r")
    text_source = f.read()
    f.close()
    return text_source


def clean_input(text_source):
    # создание алфавита для удаления лишнего из введенных данных
    d = [".", ",", ";", ":", "?", "!", "-", "(", ")", "...", '"', "«", "»", "-", "—"]
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


def check_len_two(word1, word2):
    return len(word1) >= 2 and len(word2) >= 2


def check_hard_and_soft_sign(word):
    d = ['ь', 'ъ', 'Ъ', 'Ь']
    for i in range(len(d)):
        if word.count(d[i]) >= 1:
            return True
    return False


def check_two_syllables(word):
    count = 0
    vowel_list = ['А', 'Е', 'Ё', 'И', 'О', 'У', 'Ы', 'Э', 'Ю', 'Я',
                  'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

    for i in range(len(word)):
        for j in range(len(vowel_list)):
            if word[i].count(vowel_list[j]) >= 1:
                count += 1

    if count >= 2:
        return True
    else:
        return False


def show_variants_of_warp(text_source):
    checked = False
    count = 1
    for i in range(len(text_source)):
        temp = text_source[i]
        print(f"Для слова {temp}:")
        for k in range(len(temp) - 2) :
            checked = check_len_two(temp[0: k + 2], temp[k + 2: len(temp)])
            checked = check_two_syllables(temp)
            checked = check_two_syllables(temp)
            if checked:
                print(f"{temp[0: k + 2]}-{temp[k + 2: len(temp)]}")
                k += 2
            else:
                k += 1
            count += 1
        count = 1


def main():
    text_source = input_from_file('1.txt')
    text_source = clean_input(text_source)
    make_list_of_unique_words(text_source)
    show_variants_of_warp(text_source)


main()
