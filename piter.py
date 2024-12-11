s = input()
odd = 0
even = 0
for i in range(len(s)):
    if i % 2 == 0:
        even += int(s[i])
    else:
        odd += int(s[i])
#tg @goida_code
if even == odd:
    print("Счастливое по-питерски")
else:
    print("Повезет позже")
#tg @goida_code