def fatorial(numero, show=False):
    fat=1
    for contador in range(numero, 0, -1):
        if show:
            print(contador, end='')
            if contador > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat*=contador
    return fat


print(fatorial(5, show=True))
