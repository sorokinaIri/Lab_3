# TODO Напишите функцию для поиска индекса товара


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
     # TODO Вызовите функцию, что получить индекс товара
    if find_item in items_list:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {items_list.index(find_item)}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
