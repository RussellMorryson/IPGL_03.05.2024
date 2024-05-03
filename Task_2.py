class FIFO_1:
    buffer = []

    def __init__(self): #
        self.buffer = []

    def val_in(self, val: int): # Метод для добалвения нового элемента буфера
        self.buffer.append(val)

    def val_out(self): # Метод для вывода первого элемента буфера
        first = self.buffer[0]
        self.buffer.pop(0)    
        return first
    
    def show(self): # Метод для вывода информации о состоянии буфера
        line: str = ""
        for i in self.buffer:
            line += str(i) + ', '
        print(line[: - 2])


if __name__ == '__main__':
    fbuf = FIFO_1 () # Создание объекта класса
    fbuf.val_in(9) # Добавление элемента в буфер созданного объекта
    fbuf.val_in(5) # 
    fbuf.val_in(6) #
    fbuf.val_in(4) #
    fbuf.show() # Вывод информации о состоянии буфера

    print(fbuf.val_out()) #  Вывод первого элемента буфера
    fbuf.show() # Вывод информации о состоянии буфера