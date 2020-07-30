from funcs import get_data, make_fig


if __name__ == '__main__':
    source, target, value, nan, color, labels = get_data(input('Zadej jméno souboru ve formátu "xxx.csv": '))
    make_fig(labels, source, target, value, color)

