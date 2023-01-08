from typing import Generator


def names_with_letter(path: str, letter: str) -> Generator:
    with open(path) as file:
        for n in file:
            if n.startswith(letter):
                yield n


if __name__ == '__main__':
    names_gen = names_with_letter('/Users/bat41k/Desktop/TMS_pythonProject/hw/hw_13/unsorted_names.txt', 'A')
    print(next(names_gen), end='')
    print(next(names_gen), end='')

    for name in names_with_letter('/Users/bat41k/Desktop/TMS_pythonProject/hw/hw_13/unsorted_names.txt', 'A'):
        print(name, end='')