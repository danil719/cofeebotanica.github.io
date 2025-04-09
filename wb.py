import pandas as pd
import requests

base_params = {
    'ab_vector_qi_from': 'extend',
    'appType': '1',
    'curr': 'rub',
    'dest': '-1257786',
    'lang': 'ru',
    'query': 'экстендер вакуумный',
    'resultset': 'catalog',
    'sort': 'popular',
    'spp': '30',
    'suppressSpellcheck': 'false'
}

data_list = []

for page in range(1, 11):
    params = base_params.copy()
    params['page'] = str(page)

    try:
        response = requests.get('https://search.wb.ru/exactmatch/ru/common/v9/search', params=params)
        response.raise_for_status()
        data = response.json()

        products = data.get('data', {}).get('products', [])
        for product in products:
            price = None
            sizes = product.get('sizes', [])
            if sizes:
                price = sizes[0].get('price', {}).get('product', 0) / 100  # Переводим в рубли

            data_list.append({
                'Название': product.get('name', 'Нет названия'),
                'ID': product.get('id', 'Нет ID'),
                'Бренд': product.get('brand', 'Нет бренда'),
                'Цена (руб)': price
            })

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе страницы {page}: {e}")

# Создаем DataFrame и сохраняем в Excel
df = pd.DataFrame(data_list)
df.to_excel('wildberries_products.xlsx', index=False, engine='openpyxl')

print("Данные сохранены в wildberries_products.xlsx!")