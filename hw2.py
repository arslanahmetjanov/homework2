#1
s = "Программисты — не волшебники, способные вернуть удалённые в прошлом году фотографии, взломать за 5 секунд любой сайт и починить микроволновку. Но именно эти люди создают то пространство, где и появляются мемы про них"
for i in range(len(s)):
    if i % 10 == 0:
        print(s[i])
        

#2
i = input("Вводи число: ")
if i.isdigit() != True:
    print("Ну, попросил же :(")
    while i.isdigit() != True:
        i = input("Не балуйся! Вводи число:")
        
i = int(i)

if i > 20 and i < 40:
    print("YES")
else:
    print("NO")

#3
for i in range(1,11):
    print(i)
    
j = 1
while j != 11:
    print(j)
    j += 1

#4
lst = [3, 0, 1, 3, 0, 4, 3, 3, 4, 5, 6, 6, 1, 3]
c = 0
for i in lst:
    if i == 3:
        c += 1
print("1 -", c)

c = 0
j = 0
while len(lst) > 0:
    if j < len(lst):
        if lst[j] == 3:
            c += 1
        j += 1
    else:
        break
print("2 -",c)

c = lst.count(3)
print("3 -",c)

#5
lst = [3, 7, 16, 3, 0, 45, 3, 5, 66, 6]
print(sum(lst) / len(lst))

#6
for i in range (-20, 21, 3):
    print(i)


j = -20
while j <= 20:
    print(j)
    j += 3

#7
i = int(input("Введи номер месяца: "))

if i >= 3 and i <= 5:
    print("весна")
elif i >= 6 and i <= 8:
    print("лето")
elif i >= 9 and i <= 11:
    print("осень")
elif i >= 1 or i <= 12:
    print("зима")
else:
    print("В году 12 месяцев :)")