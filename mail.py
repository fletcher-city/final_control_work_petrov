def filter_strings(arr):
    new_arr = []
    for string in arr:
        if len(string) <= 3:
            new_arr.append(string)
    return new_arr

# Примеры данных
input1 = ["Hello", "2", "world", ":-)"]
input2 = ["1234", "1567", "-2", "computer science"]
input3 = ["Russia", "Denmark", "Kazan"]

# Вызов функции для каждого примера
output1 = filter_strings(input1)
output2 = filter_strings(input2)
output3 = filter_strings(input3)

# Вывод результатов
print(output1)
print(output2)
print(output3)