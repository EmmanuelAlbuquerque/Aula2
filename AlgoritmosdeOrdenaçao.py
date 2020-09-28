#BubbleSort 

def bubbleSort(list):
    for passnum in range(len(list)-1,0,-1):
        for i in range(passnum):
            if list[i]>list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp


lista = [54,26,93,17,77,31,44,55,20]
bubbleSort(lista)
print(lista)


#MergeSort

def mergeSort(list):
    print("Divisão ",list)
    if len(list)>1:
        meio = len(list)//2
        esqmet = list[:meio]
        dirmet = list[meio:]

        mergeSort(esqmet)
        mergeSort(dirmet)

        i=0
        j=0
        k=0
        while i < len(esqmet) and j < len(dirmet):
            if esqmet[i] < dirmet[j]:
                list[k]=esqmet[i]
                i=i+1
            else:
                list[k]=dirmet[j]
                j=j+1
            k=k+1

        while i < len(esqmet):
            list[k]=esqmet[i]
            i=i+1
            k=k+1

        while j < len(dirmet):
            list[k]=dirmet[j]
            j=j+1
            k=k+1
    print("Merging ",list)

lista = [54,26,93,17,77,31,44,55,20]
mergeSort(lista)
print(lista)



#QuickSort

def quickSort(list):
   quickSortHelper(list,0,len(list)-1)

def quickSortHelper(list,first,last):
   if first<last:

       splitpoint = partition(list,first,last)

       quickSortHelper(list,first,splitpoint-1)
       quickSortHelper(list,splitpoint+1,last)


def partition(list,first,last):
   pivo = list[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and list[leftmark] <= pivo:
           leftmark = leftmark + 1

       while list[rightmark] >= pivo and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = list[leftmark]
           list[leftmark] = list[rightmark]
           list[rightmark] = temp

   temp = list[first]
   list[first] = list[rightmark]
   list[rightmark] = temp


   return rightmark

lista = [54,26,93,17,77,31,44,55,20]
quickSort(lista)
print(lista)
