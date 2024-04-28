import tkinter as tk
from node import Node
from stack import Stack

def split_stack(data):
    operands = Stack()
    operators = Stack()
    
    num = ''
    for char in data:
        if char.isdigit():
            num += char
        else:
            if num:
                operands.push(num)
                num = ''
            while operators.size > 0 and prior(char) < prior(operators.top.data):
                op1 = operands.pop()
                op2 = operands.pop()
                op3 = operators.pop()
                result = operation(op2, op1, op3)
                operands.push(result)
            operators.push(char)
    
    if num:
        operands.push(num)
    
    while operators.size > 0:
        op1 = operands.pop()
        op2 = operands.pop()
        op3 = operators.pop()
        result = operation(op2, op1, op3)
        operands.push(result)
        
    return operands.pop()

def operation(op1, op2, op3):
    if op3 == "+":
        result = int(op1) + int(op2)
        return result
    elif op3 == "-":
        result = int(op1) - int(op2)
        return result
    elif op3 == "*":
        result = int(op1) * int(op2)
        return result
    elif op3 == "/":
        try:
            assert int(op2) != 0
            result = int(op1) / int(op2)
        except AssertionError:
            return "Divisão por 0 não é permitida"
        else:
            return result

def prior(operator):
    if operator == "+" or operator == "-":
        return 1

    elif operator == "*" or operator == "/":
        return 2
    else: 
        return 0

def add_to_expression(char):
    entry.insert(tk.END, char)

def remove_last():
    entry.delete(len(entry.get()) - 1)
    
def evaluate_expression():
    expression = entry.get()
    result = split_stack(expression)
    result_label.config(text="Resultado: " + str(result))

# Interface gráfica usando Tkinter
root = tk.Tk()
root.title("Calculadora de Stack")

frame_entry = tk.Frame(root)
frame_entry.pack(padx=10, pady=10)

entry = tk.Entry(frame_entry, width=30)
entry.pack(side=tk.LEFT)

frame_buttons = tk.Frame(root)
frame_buttons.pack(padx=10, pady=10)

button_row1 = ["7", "8", "9", "+"]
button_row2 = ["4", "5", "6", "-"]
button_row3 = ["1", "2", "3", "*"]
button_row4 = ["0", "/", "<-", "="]

array_line = {
    "1": button_row1,
    "2": button_row2,
    "3": button_row3,
    "4": button_row4
}

def line_buttons(frame_buttons, array_line):
    for row_index, button_row in enumerate(array_line.values()):
        for col_index, button_text in enumerate(button_row):
            if button_text == "=":  
                button = tk.Button(frame_buttons, text=button_text, width=5, command=evaluate_expression)
            elif button_text == "<-": 
                button = tk.Button(frame_buttons, text=button_text, width=5, command=remove_last)
            else:
                button = tk.Button(frame_buttons, text=button_text, width=5, command=lambda char=button_text: add_to_expression(char))
            button.grid(row=row_index, column=col_index)

line_buttons(frame_buttons, array_line)

result_label = tk.Label(root, text="Resultado: ")
result_label.pack()

root.mainloop()
