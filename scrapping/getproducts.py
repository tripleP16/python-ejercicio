from selenium.webdriver.common.by import By
import time
from models.product import Product

# Se obtiene la cantidad total de paginas
def get_pages(driver, class_name):
    pagination = driver.find_elements(By.CLASS_NAME, class_name)
    max_page = 0
    for page in pagination: 
        try:
            aux = int(page.get_attribute("innerHTML"))
            if aux > max_page :
                max_page = aux
        except: 
            continue
    return max_page

# Funcion que permite cambiar de pagina
def next_button(page, driver):
    site = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page={}".format(page)
    driver.get(site)
    time.sleep(1)
    


# Funcion que obtiene la lista de productos a guardar
def get_products(
    max_page,
    min_stars, 
    driver):
    products = []
    for i in range(1,max_page + 1):
        row = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/div")
        products_to_check = row.find_elements(By.CSS_SELECTOR, ".col-lg-4")
        for product in products_to_check:
            rating = product.find_element(By.CLASS_NAME, "ratings")
            stars = rating.find_elements(By.TAG_NAME, "span")
            total_stars = len(stars)
            if(total_stars >= min_stars):
                title_element = product.find_element(By.CLASS_NAME, "title")
                name = title_element.get_attribute("innerHTML")
                id = title_element.get_attribute("href").split("/")[-1]
                product_to_send = Product(id,name,stars)
                products.append(product_to_send)
        next_button(i, driver)
    return products
    
    

