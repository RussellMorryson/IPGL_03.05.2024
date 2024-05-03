"""
Пример: 
def isEven(value):
      return value % 2 == 0
"""

def isEven(value: int): # Указание типа принимаемого аргумента
    if int(value) % 2 == 0: # В случае передачи str в функцию конвертация в int
        return True
    return False

# При написании функции важно то, что ожидается от нее.
# В примере выше в ковычках код короче, в примере ниже понятнее, но они выполняют одинаковое действие

if __name__ == '__main__':
    print(isEven(5)); # False
    print(isEven(4)); # True

    c = input() # 9: str
    print(isEven(c)); #error 
    # При вводе буквы алгоритм приведет к критической ошибке