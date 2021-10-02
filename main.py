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
    start = int(input("Prima valoare este: "))
    end = int(input("Ultima valoare este: "))
    #  l=get_leap_years(start,end)
    #  print("Anii bisecti sunt: ",l)
    # test_get_leap_years()
    l= get_perfect_squares(start, end)
    print("Patratele perfecte sunt: ",l)
    test_get_perfect_squares()
main()