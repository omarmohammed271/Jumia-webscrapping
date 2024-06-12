from requests_html import HTMLSession
import asyncio
import os
import csv

# PYPPETEER_CHROMIUM_REVISION = '1263111'

# os.environ['PYPPETEER_CHROMIUM_REVISION'] = PYPPETEER_CHROMIUM_REVISION



session = HTMLSession()


for x in range(15,50):
    print(f'Page Number {x} ----------------------------')
    req = session.get(f"https://www.jumia.com.eg/all-products/?page={x}#catalog-listing")

    req.html.render(sleep=2)

    products = req.html.xpath('//*[@id="jm"]/main/div[2]/div[3]/section/div[1]',first=True)
    with open('Jumia_all_products.csv','a',newline='',encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name','Price','Details','Rating'])
        for product in products.absolute_links:
            req = session.get(product)
            name_element = req.html.find('h1.-pbxs', first=True)
            if name_element is not None:
                name = name_element.text
            else:
                name = 'N/A'
            
            price_element = req.html.find('span.-prxs', first=True)
            if price_element is not None:
                price = price_element.text
            else:
                price = 'N/A'
            
            detail_element = req.html.find('div.-sc', first=True)
            if detail_element is not None:
                detail = detail_element.text
            else:
                detail = 'N/A'
            
            rating_element = req.html.find('div.-yl5', first=True)
            if rating_element is not None:
                rating = rating_element.text
            else:
                rating = 'N/A'

            writer.writerow([name,price,detail,rating])
            
            # print(f'Name : {name}')
            # print(f'price : {price}')
            # print(f'description : {detail}')
            # print(f'rating : {rating}')
            # print('----------------------------------')
            print(f'Item  Done')
    print('----------------------------------')