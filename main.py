from typing import List


def show_menu():
    print('1. Citire lista. ')
    print('2. Afisare numere prime. ')
    print('3. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sunt divizibile cu 10.')
    print('4. Iesire. ')


def read_list() -> List[int]:
    list_int = []
    list_str = input('Introduceti numere separate prin spatiu: ')
    list_str_split = list_str.split(' ')
    for lista in list_str_split:
        list_int.append(int(lista))
    return list_int


def is_prime(n: int) -> bool:
    '''
    Determina daca un numar dat n este prim.
    :param n: Numarul dat.
    :return: True daca numarul n este prim, False in caz contrar.
    '''
    if n < 2:
        return False
    for i in range(2, n - 1):
        if n % i == 0:
            return False
    return True


def test_is_prime():
    assert is_prime(-5) == False
    assert is_prime(1) == False
    assert is_prime(5) == True
    assert is_prime(12) == False
    assert is_prime(29) == True


def get_list_primes(lst: List[int]) -> List[int]:
    '''
    Determina numerele prime dintr-o lista data.
    :param lst: Lista data.
    :return: Numerele prime din lista.
    '''
    lista_prime = []
    for i in lst:
        if is_prime(i):
            lista_prime.append(int(i))
    return lista_prime


def test_get_list_primes():
    assert get_list_primes([]) == []
    assert get_list_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7]
    assert get_list_primes([12, 14, 25, 29, 19, 13, 4, 13]) == [29, 19, 13, 13]


def get_all_div_by_10(lst: List[int]) -> bool:
    '''
    Determina daca elementele dintr-o lista sunt divizibile cu 10 sau nu.
    :param lst: O lista data.
    :return: True daca toate elementele din lista sunt divizibile cu 10, False in caz contrar.
    '''
    for i in lst:
        if i % 10 != 0:
            return False
    return True


def test_get_all_div_by_10():
    assert get_all_div_by_10([1, 2, 3, 4]) == False
    assert get_all_div_by_10([10, 200, 2340, 2340, 150]) == True
    assert get_all_div_by_10([10, 20, 30, 5]) == False
    assert get_all_div_by_10([10, 15, 20, 25, 30, 35]) == False


def get_longert_subarray_div_by_10(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lunga subsecventa de numere divizibile cu 10.
    :param lst: O lista data.
    :return: Cea mai lunga subsecventa de numere divizibile cu 10.
    '''
    subsecventa_max = []
    for st in range(len(lst)):
        for dr in range(st, len(lst)):
            if get_all_div_by_10(lst[st:dr + 1]) and len(subsecventa_max) < len(lst[st:dr + 1]):
                subsecventa_max = lst[st:dr + 1]
    return subsecventa_max


def test_get_longert_subarray_div_by_10():
    assert get_longert_subarray_div_by_10([]) == []
    assert get_longert_subarray_div_by_10([110, 12, 120, 230, 340, 35, 4660, 35]) == [120, 230, 340]
    assert get_longert_subarray_div_by_10([10, 20, 30, 40, 11, 23, 34, 24, 40, 30]) == [10, 20, 30, 40]
    assert get_longert_subarray_div_by_10([10, 20, 34, 30, 4503530, 350, 64, 50, 360, 4650]) == [30, 4503530, 350]

    def main():

        lista = []

    while True:
        show_menu()
        optiune = input('Alegeti optiunea: ')
        if optiune == '1':
            lista = read_list()
        elif optiune == '2':
            print(f'Numerele prime din lista {lista} sunt: {get_list_primes(lista)}')
        elif optiune == '3':
            print(
                f'Cea mai lunga subsecvente de numere divizibile cu 10 din lista {lista} sunt: {get_longert_subarray_div_by_10(lista)}.')
        elif optiune == '4':
            break
        else:
            print('Optiune invalida, incercati din nou! ')


if __name__ == '__main__':
    test_is_prime()
    test_get_list_primes()
    test_get_all_div_by_10()
    test_get_longert_subarray_div_by_10()
    main()
