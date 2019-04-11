# Slowniki
aliens = {'kolor': 'zielony', 'punkty': '5'}
print(aliens['kolor'])
print(aliens['punkty'])
aliens['name'] = 'Mateusz'
del aliens['kolor']

favorite_lang = {
    'Janek': 'python',
    'Janina': 'c',
    'Stas': 'Nie lubi zadnego'
}

for key, value in favorite_lang.items():  # key == name, value == languages
    print("\nKlucz : " + key.title())
    print("Wartosc : " + value)
myFriends = ['Stas', 'Janina']

for name, value in favorite_lang.items():
    if name in myFriends:
        print("Witaj, " + name.title() + "! Widze, ze Twoim ulubionym jezykiem programowania jest " + value)
    else:
        print("Wartosc : " + name + ", jezyk : " + value)
# if name not in array, .values():, .set() = unikatowe rzeczy

for name in sorted(favorite_lang):
    print(name.title() + ", dziekuje!")

al = {'color': 'grey', 'pt': '3'}
al1 = {'color': 'green', 'pt': '5'}
al2 = {'color': 'blue', 'pt': '7'}

alienAll = [al, al1, al2]
for alien in alienAll:
    print(alien)

klucz = {
    'color': {
        'janek': 'blue',
        'maria': 'grey'
    },}

for user, color in klucz.items():
    print("Uzytkownik" + user)
    fcolor = color['janek']
    fcolor2 = color['maria']

    print("Janek " + fcolor)
    print("Maria " + fcolor2)
