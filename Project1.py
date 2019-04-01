print("Hello World!")
x = 10;
print(type(x));

y = "Hi!"
y = y + " dude! Welcome to my first Python file!"
print(y)

z = input() #wejscie uztyownika
z = int(x) #konwersja z stringa na inta
print(z)

print(y[1])  #Druga liczba
print(y[0:3]) #Wypisze caly wyraz
print(y[:]) #Wypisze cale zdanie
arrays = [1, 1, 1, 2, 2, 3, 3, 3, 3]
AktualnaDominanta = arrays[0]
LiczbaAD = 0
Nowa = 0
LiczbaNowej = 0
for array in arrays:
    if array == AktualnaDominanta:
        LiczbaAD+=1
    else:
        Nowa = array
        while Nowa == array
            LiczbaNowej+=1
            array+=1
    if LiczbaAD > LiczbaNowej:
        LiczbaNowej = 0
    elif LiczbaAD == LiczbaNowej:
        print("Nie ma w tej tablicy dominanty!")
    else :
        AktualnaDominanta = Nowa
        LiczbaAD = Nowa
        Nowa = 0

if LiczbaAD > LiczbaNowej:
    print(AktualnaDominanta)
else :
    print(Nowa)