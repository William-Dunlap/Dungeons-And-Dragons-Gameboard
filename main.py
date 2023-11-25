import data
from weapons import Weapons


def main():
    for arr in data.weapons:
        arr[0] = Weapons(arr)


if __name__ == '__main__':
    main()
