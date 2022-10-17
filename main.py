from scrapping.getsite import get_site

def main(): 
    driver = get_site('https://webscraper.io/test-sites/e-commerce/static/computers/laptops')
    driver.close()

if __name__ == "__main__": 
    main()
