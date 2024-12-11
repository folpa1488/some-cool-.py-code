def flupper(s):
    r = ""
    for i in range(len(s)):
        o = ord(s[i])
        if o >= ord("a") and o <= ord("z"):  # если текст на английском маленькими буквами
            r += (chr(o - (ord("z") - ord("Z"))))
        # tg @goida_code
        elif o >= ord("а") and o <= ord("я"):
            r += (chr(o - (ord("я") - ord("Я"))))
        else:
            r += s[i]
    return r

#tg @goida_code
print(flupper(input()))
# прога делает весь введенный текст капсом
