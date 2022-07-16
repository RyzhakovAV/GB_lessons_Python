original_text = input("Введите строку: ")
find_text = input("Введите строку: ")

def find_in_str (orl_text: str, f_text: str):
    counter = 0
    for index in range(0, len(orl_text) - len(f_text)+1):
        if f_text in orl_text[index:index+len(f_text)]: counter+=1
    return counter

print(f"Текст {find_text} встречается в тексте {find_in_str(original_text, find_text)} раз")
