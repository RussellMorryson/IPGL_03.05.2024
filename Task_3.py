# Данный метод фактически занимается рекурсивным поиском и сортировкой элементов
def quickSort(myList): # Методя быстрой сортироки 
    if len(myList) < 1: # При условии того что список пуст, вернуть пустой список
        return myList
    else:
        pivot = myList[0]
        lesser = quickSort([x for x in myList[1:] if x < pivot]) # Рекурсивный поиск наименьшего елемента
        greater = quickSort([x for x in myList[1:] if x >= pivot]) # Рекурсивный поиск наибольшего элемента
        return lesser + [pivot] + greater # Возврат структуры сортировки
        
if __name__ == '__main__':
    l1 = [1, 5, 65, 41, 102, 2, 38, 96]
    print(quickSort(l1))
