from scrapping.getsite import get_site
from scrapping.getproducts import get_pages, get_products

def main(): 
    driver = get_site('https://webscraper.io/test-sites/e-commerce/static/computers/laptops')
    max_page = get_pages(driver, "page-link")
    print(get_products(max_page,2, driver))


if __name__ == "__main__": 
    main()
