def valorLista():
    for i in range(1,5):
        lista.append(int(input(f'Digite o Valor da sua Prova {i}')))
def Media():
    s=0
    for i in range(len(lista)):
        s = s+ lista[i]
    m= s/ 4
    return m

lista = []
valorLista()
m= Media()
print(m)