from math import prod
from scrapping.getsite import get_site
from scrapping.getproducts import get_pages, get_products
from data.connection import Connection

def insertInBd(products, connection):
    for product in products: 
        connection.insert(product.name, product.stars, product.id)

def main(): 
    driver = get_site('https://webscraper.io/test-sites/e-commerce/static/computers/laptops')
    max_page = get_pages(driver, "page-link")
    products = get_products(max_page,2, driver)
    connection = Connection()
    connection.create_db_tables()
    insertInBd(products, connection)
    connection.print_all_data('products')



if __name__ == "__main__": 
    main()
