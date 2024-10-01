products = []
product = input("Введите товар (0 для завершения): ")
while product != '0':
    count = int(input("Введите количество: "))
    products.append([product, count])
    print('\nДобавлено: ' + '[' + product + ']' + ' в количестве:', count, '\n')
    product = input("Введите товар (0 для завершения): ")
print('\nСписок товаров:\n', products,'\n')

print('-' * 20 + '\n')

shop_name = input("Введите название магазина (0 для завершения): ")
shops_and_prices = []

while shop_name != '0':
    products_prices = []
    for i in products:
        product = i[0]
        price = int(input('Введите цену на товар: [' + product + ']: '))
        products_prices.append([product, price])
    shops_and_prices.append([shop_name, products_prices])
    shop_name = input("Введите название магазина (0 для завершения): ")

print('\n' + '-' * 20 + '\n')

min_summa = []

for i in shops_and_prices:
    summa = 0
    for j in range(len(products)):
        summa += i[1][j][1] * products[j][1]
    print('Общая цена в магазине [' + i[0] +']: ', summa)

    if min_summa == [] or min_summa[1] > summa:
        min_summa = [i[0], summa]

print('\n' + '-' * 20 + '\n')

print("Меньше всего сумма в магазине: [" + min_summa[0] + "] (" + str(min_summa[1]) + ")")
