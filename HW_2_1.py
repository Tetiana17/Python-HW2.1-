number = int(input("введи 4-х значне число:"))

thousands = number//1000  # отримую тисячні
hundreds =(number//100) % 10  # отримую соті
tens = (number//10) % 10  # отримую десятки
units = number % 10  # отримую одиниці

# вивожу отримані цифри в колонку
print(thousands)
print(hundreds)
print(tens)
print(units)
