translit = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",
    "б": "b", "ю": "ju", "ё": "jo"
}

file = open('./data/cyrillic.txt', encoding='utf8')
text = file.readline()

транслит = ""

for line in text:
    for symb in line:
        is_up = symb.isupper()
        s = translit.get(symb.lower(), symb)
        
        if is_up:
            s = s.capitalize()
            
        транслит += s
file.close()

result = open('./data/transliteartion.txt', 'w', encoding='utf8')
result.write(транслит)
result.close()