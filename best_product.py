import requests
import json
from bs4 import BeautifulSoup
import app


import sys
sys.path.insert(0,'bs4.zip')

#Imitate the Mozilla browser.
# user_agent = {'User-agent': 'Mozilla/5.0'}
user_agent = {'User-agent': 'Chrome/99.0.4844.84'}



def compare_prices(laughs_url,glomark__url):

    # laughs_product_dict = {
    #     1: 'maliban-lemon-puff-200g-pkt.html',
    #     2: 'categories/beverages/coca-cola-2l-pet.html',
    #     3: 'panda-baby-cologne-mother-s-love-100ml-126861.html',
    #     4: 'coca-cola-zero-sugar-free-2l-129838.html'
        
    # }   


    # product_url = laughs_product_dict[1]
    

    #laughs_product_url = f'{laughs_base_url}{product_url}'
    html = requests.get(laughs_url).content
    laughs_markup = f''' {html} '''
    soup = BeautifulSoup(laughs_markup, 'html.parser')
    # print(soup.prettify())


    product_name = soup.find('div', {'class': 'product-name'})
    product_name_laughs = product_name.find('h1').text

    price_laughs = soup.find('span', {'class': 'regular-price'})
    #print(price_laughs.find('span').text)

    price_laughs = float(price_laughs.find('span').text[3:])


# - - - - - - 

    # glomark_product_dict = {
    #     1: 'maliban-biscuit-lemon-puff-200g/p/15318',
    #     2: 'flora-facial-tissues-160s/p/10470',
    #     3: 'whole-grain-oats-bread/p/13684',
    #     4: 'flora-facial-tissues-200s-2-ply/p/13509',
    #     5: 'star-gold-white-sugar-1kg/p/36066'
    # }

    # product_url = glomark_product_dict[1]

    #glomark_product_url = f'{glomark_base_url}{product_url}'
    html = requests.get(glomark__url).content
    glomark_markup = f''' {html} '''
    soup = BeautifulSoup(glomark_markup, 'html.parser')


    product_name = soup.find('div', {'class': 'product-title'})
    product_name_glomark = product_name.find('h1').text


    res = requests.get(glomark__url)
    soup = BeautifulSoup(res.content, 'html.parser')
    script = soup.find('script', type='application/ld+json').text.strip()
    #print(script)

    data = json.loads(script)
    price_glomark = data['offers'][0]['price']
    # print(price_glomark)
    price_glomark = float(price_glomark)  

      
    laughs_statement = f'Laughs  {product_name_laughs} Rs.: {price_laughs}'
    glomark_statement = f'Glomark {product_name_glomark} Rs.: {price_glomark}'
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)


    final_statement = ''

    if(price_laughs>price_glomark):
        #print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
        #return 'Glomark is cheaper Rs.:',price_laughs - price_glomark
        final_statement = f'Select the Glomark product, it is cheaper Rs. {price_laughs - price_glomark}'
    elif(price_laughs<price_glomark):
        #print('Laughs is cheaper Rs.:',price_glomark - price_laughs) 
        #return 'Laughs is cheaper Rs.:',price_glomark - price_laughs 
        final_statement = f'Select the Laughs product, it is cheaper Rs. {price_glomark - price_laughs}'   
    else:
        #print('Price is the same')
        # return 'Price is the same'
        final_statement = f'Same Price'

    

    return laughs_statement, glomark_statement, final_statement

    



# laughs_base_url = 'https://www.laugfssuper.com/index.php/'
# glomark_base_url = 'https://glomark.lk/'
# print(compare_prices(laughs_base_url, glomark_base_url))


























#laughs_base_url = 'https://www.laugfssuper.com/index.php/'

# product_url = 'maliban-lemon-puff-200g-pkt.html'
# product_url = 'panda-baby-cologne-mother-s-love-100ml-126861.html'
# product_url = 'flora-facial-tissues-2-x-160-box-548116.html'

# laughs_product_url = f'{laughs_base_url}{product_url}'
# html = requests.get(laughs_product_url).content
# laughs_markup = f''' {html} '''
# soup = BeautifulSoup(laughs_markup, 'html.parser')
# # print(soup.prettify())

# product_name = soup.find('div', {'class': 'product-name'})
# print(product_name.contents)

# product_price = soup.find('span', {'class': 'regular-price'})
# #print(product_price.find('span').text)

# product_price = float(product_price.find('span').text[3:])
# print(product_price)


# # - - -

# glomark_base_url = 'https://glomark.lk/'
# product_url = 'maliban-biscuit-lemon-puff-200g/p/15318'
# #product_url = 'whole-grain-oats-bread/p/13684'

# glomark_product_url = f'{glomark_base_url}{product_url}'
# html = requests.get(glomark_product_url).content
# glomark_markup = f''' {html} '''
# soup = BeautifulSoup(glomark_markup, 'html.parser')


# glomark_product_name = soup.find('div', {'class': 'product-title'})
# print(glomark_product_name.find('h1').text)


# res = requests.get(glomark_product_url)
# soup = BeautifulSoup(res.content, 'html.parser')
# script = soup.find('script', type='application/ld+json').text.strip()
# # print(script)

# data = json.loads(script)
# price = data['offers'][0]['price']
# print(price)
