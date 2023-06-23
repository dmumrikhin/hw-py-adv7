'''
Используя стек из задания 1 необходимо решить задачу на проверку сбалансированности 
скобок. Сбалансированность скобок означает, что каждый открывающий символ имеет 
соответствующий ему закрывающий, и пары скобок правильно вложены друг в друга.
'''

class Stack:

    def __init__(self, stack = ''):
        self.stack = stack

    def isEmpty(self): # Проверка, пустой ли стек
        if len(self.stack) > 0:
            return False
        else:
            return True
        
    def push(self, elem: str): # Добавляет элемент в стек
        self.stack += elem

    def pop(self) -> str: # Удаляет последний элемент, возвтращает его
        last_char = self.stack[-1]
        self.stack = self.stack[:-1]
        return last_char
    
    def peek(self) -> str: # Возвтращает последний элемент стека
        try:
            last_char = self.stack[-1]
            return last_char
        except:
            pass
    
    def size(self) -> str: # Возвращает длину стека
        return len(self.stack)



def check_the_row(row):

    temp_stack = Stack('')
    bracket_pair_list = [['(',')'], ['[', ']'], ['{', '}']]

    for item in row:
        if [temp_stack.peek(), item] in bracket_pair_list:
            temp_stack.pop()
        else:
            temp_stack.push(item)
    
    if temp_stack.isEmpty():
        print('Сбалансированно')
    else:
        print('Несбалансированно')

if __name__ == '__main__':

    row = '()'
    check_the_row(row)



