# TODO  Напишите функцию count_letters
# TODO Напишите функцию calculate_frequency


def count_letters (main_str):
    text = ' '.join(main_str.lower()).split()
    letter_dict ={
    }
    for i in range(0,len(text)):
        if text[i].isalpha() == True:
            if text[i] in letter_dict:
                letter_dict[text[i]] +=1
            else:
                letter_dict[text[i]] = 1
    return letter_dict
def calculate_frequency(letter_dict):
    frequency_dict = {
    }
    count_all = sum(letter_dict.values())
    for letter in "".join(letter_dict):
        frequency_dict[letter] = format(letter_dict[letter] / count_all, '.2f')
    for key, value in frequency_dict.items():
        print("{0}: {1}".format(key,value))
    return

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

calculate_frequency(count_letters(main_str))


# TODO Распечатайте в столбик букву и её частоту в тексте
