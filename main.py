import math
def get_leap_years(start: int, end: int):
    '''
    Determinam anii bisecti intr-un interval inchis dat
    :param start: prima valoare din interval
    :param end: ultima valoare din interval
    :return: lista tuturor anilor bisecti
    '''
    li = []
    if start % 4 == 0:
        first = start
    elif (start+1) % 4 == 0:
        first = start+1
    elif (start+2) % 4 == 0:
        first = start+2
    elif (start + 3) % 4 == 0:
        first = start + 3
    while first <= end :
        li.append(first)
        first += 4
    return li


def get_perfect_squares(start: int, end: int):
    '''
    Returneaza o lista cu toate patratele perfecte dintr-un interval inchis
    :param start: prima valoare din interval
    :param end: ultima valoare din interval
    :return: Lista
    '''
    li = []
    for i in range (start, end+1):
        if math.sqrt(i) == int(math.sqrt(i)):
            li.append(i)
    return li

def is_palindrome(n: int):
    '''
    Returneaza 1 daca numarul este palindrom, 0 in caz contrar
    :param n:parametru de verificare
    :return: true sau false
    '''
    ogl = 0
    x = n
    while x > 0:
        ogl = ogl*10 + x % 10
        x = x // 10
    if n == ogl:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(151) is True
    assert is_palindrome(12) is False
    assert is_palindrome(913) is False
    assert is_palindrome(1331) is True
def test_get_leap_years():
    assert get_leap_years(2013, 2014) == []
    assert get_leap_years(2013, 2016) == [2016]
    assert get_leap_years(2012, 2016) == [2012, 2016]
    assert get_leap_years(2017, 2030) == [2020, 2024, 2028]
    assert get_leap_years(2008, 2016) == [2008, 2012, 2016]

def test_get_perfect_squares():
    assert get_perfect_squares(2, 3) == []
    assert get_perfect_squares(15, 17) == [16]
    assert get_perfect_squares(1, 100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert get_perfect_squares(5, 70) == [9, 16, 25, 36, 49, 64]
def main():
    print("1.Numarul este palindrom")
    print("2.Anii bisecti dintre doua numere")
    print("3.Toate numerele patrate perfecte dintr-un interval inchis")
    print("4.Exit")
    x = int(input("Alegeti exercitiul"))
    while x!=0:
        if x == 1:
            n = int(input("Numarul este: "))
            print(is_palindrome(n))
        elif x == 2:
            start = int(input("Prima valoare este: "))
            end = int(input("Ultima valoare este: "))
            l=get_leap_years(start,end)
            print("Anii bisecti sunt: ",l)
        elif x == 3:
            start = int(input("Prima valoare este: "))
            end = int(input("Ultima valoare este: "))
            l = get_perfect_squares(start, end)
            print("Patratele perfecte sunt: ",l)
        elif x == 4:
            x = 0
        elif x>4 :
            print("Acest exercitiu nu exista")
        print("1.Numarul este palindrom")
        print("2.Anii bisecti dintre doua numere")
        print("3.Toate numerele patrate perfecte dintr-un interval inchis")
        print("4.Exit")
        x = int(input("Alegeti exercitiul"))
    test_get_leap_years()
    test_get_perfect_squares()
    test_is_palindrome()

main()