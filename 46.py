'''Задана таблиця назв товарів, що випускаються заводом.
Визначте, чи повторюється в цій таблиці назва першого товару, і, якщо повторюється, видаліть назву першого товару з таблиці. '''
products = ['jeans', 'sweater', 't-shirt', 'jeans', 'dress', 'pants']
if products.count(products[0]) > 1:
    productName = products[0]
    while productName in products:
        products.remove(productName)
print(products)