print("Hello World!")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x.append(10)
print(x)
x.insert(0, 0)
print(x)
y = [5, 1, 2, 4, 6, 2, 5 ,7, 10]
print(y)
y.sort()
print(y)

z = ['Mateusz', 'Karol', 'Wojtek', 'Mikolaj', 'Pawel', 'Marcin']
for names in z:
    print(names)

for i in range(0, 50, 2):
    print(i)

fruits = ['apple', 'applepen', 'banana', 'pear']
for i, fruit in enumerate(fruits):
    if i == 3:
        break
    print(i)
    print(fruit)

x = "czesc {} {}".format("siema", "elo")
print(x)
#print("Sprawdzam {}".format(i))
Cwiczenie = ('Mateusz', 'Admin', 'Wojtek', 'Marcin')
for cwiczenie in Cwiczenie:
    if cwiczenie == 'Admin':
        print("Witaj, " + cwiczenie + '! Czy chcesz przejrzec ostatni raport?')
    else:
        print('Witaj,' + cwiczenie+ '! Dziekujemy, ze ponownie sie zalogowales!')