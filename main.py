from funcs import get_data, make_fig


if __name__ == '__main__':
    source, target, value, na, color, labels = get_data(input('Zadej jméno souboru ve formátu xxx.csv : '))
    dia_name = input('Zadej jméno diagramu : ')
    make_fig(labels, source, target, value, color, dia_name)

