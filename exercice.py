#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
def convert_to_absolute(number: float) -> float:
    number= (number**2)**(1/2)
    return number

def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    prenom = []
    for i in prefixes:
        prenom.append(i+'ack')
    return prenom


def prime_integer_summation() -> int:
    num = 2
    somme = 0
    n = 0
    while n <= 100:
        for i in range(2, num):
            if i == num:
                n+=1
                somme += num
                num += 1
                break
            if i == num-1:
                n += 1
                somme += num
                num += 1
                break
            if num % i != 0:
                continue
            if num % i == 0 and i!=1:
                num += 1
                break




    return somme


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
