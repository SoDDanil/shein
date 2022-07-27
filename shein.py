import requests
import json

headers = {
    'Host': 'api-service.shein.com',
    'app-from': 'shein',
    'siteuid': 'android',
    'appcountry': 'RU',
    'devtype': 'Android',
    'clientid': '100',
    'accept': 'application/json',
    'device': 'Samsung Android6.0',
    'usercountry': 'RU',
    'applanguage': 'ru',
    'version': '8.3.4',
    'devicelanguage': 'ru',
    'dev-id': 'shein_f38e8066-6dd9-3050-92a9-8cc7307bf68c',
    'device_language': 'ru',
    'apptype': 'shein',
    'localcountry': 'RU',
    'smdeviceid': '202207242333016e35cdf0426b5a7fa77971ec055083d001234cebe7a6ff26',
    'deviceid': 'shein_f38e8066-6dd9-3050-92a9-8cc7307bf68c',
    'appname': 'shein app',
    'appversion': '8.3.4',
    'language': 'ru',
    'currency': 'RUB',
    'token': 'MDEwMDE.eyJiIjo3LCJnIjoxNjU4Njc2NzgwLCJyIjoiVExvUGlLIiwidCI6MX0.41203d0a74392283',
    'network-type': 'WIFI',
    'os-version': '6.0',
    'devicesystemversion': 'Android6.0',
    'appcurrency': 'RUB',
    'user-agent': 'Shein 8.3.4 Android 6.0 Samsung RU ru',
}


all_categories_select_id = [1766,2036,3195,2030,]


def get_url(url,params):
    response = requests.get(url=url,params=params,headers=headers)
    print(response.status_code)
    with open('collect.json', 'w', encoding='Windows-1251') as f:
        json.dump(response.json(),f,indent=4)
    return response

def collect_data(response):
    data = response.json()
    products = data['info']['products']
    with open ('data.txt','a',encoding='utf-8') as f:
        for product in products:
            name_product = product['goods_name']
            price_product = product['retailPrice']['amount']
            id_product = product['goods_id']
            content = name_product+' '+price_product+' ' + id_product+'\n'
            f.write(content)

def main():
    f = open('data.txt','w',encoding='Windows-1251')
    f.close()
    for id in all_categories_select_id:
        print(id)
        url = 'https://api-service.shein.com/category/real_category_goods_list'
        params = {
            'filter': '',
            'tag_ids': '',
            'userpath': 'КАТЕГОРИЯ>ЖЕНСКОЕ>ПЛАТЬЯ>ПОКУПАЙ ПО КАТЕГОРИИ>Новые Платья',
            'filter_good_ids': '',
            'store_code': '',
            'srctype': 'category',
            'cat_id': '',
            'page_name': 'page_select_class',
            'adp': '10664691',
            'sort': '0',
            'page': 1,
            'select_id': id,
            'limit': '20',
        }
        response = get_url(url,params)
        count_product = response.json()['info']['num']
        print(count_product)
        page = 0
        for product in range (0,count_product+1,20):
            page+=1
            params = {
            'filter': '',
            'tag_ids': '',
            'userpath': 'КАТЕГОРИЯ>ЖЕНСКОЕ>РАСПРОДАЖА>РЕКОМЕНДАЦИИ>Смотреть Все',
            'filter_good_ids': '',
            'store_code': '',
            'srctype': 'category',
            'cat_id': '',
            'page_name': 'page_select_class',
            'adp': '2477325',
            'sort': '0',
            'page': page,
            'select_id': id,
            'limit': '20',
        }
            print(f'Страница {page}')
            
            response = get_url(url,params)
            collect_data(response)
        
    
    


if __name__=='__main__':
    main()
