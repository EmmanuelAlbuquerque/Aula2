def BuscaSeq(List, item):
    pos =0
    x= False

    while pos<len(list) and not x:
        if List[pos]== item:
            x= True
        else:
            pos = pos +1
    return x

Lista = [5, 6, 8, 12, 42, 7, 1]
print(BuscaSeq(Lista, 8))
print(BuscaSeq(Lista, 11))
