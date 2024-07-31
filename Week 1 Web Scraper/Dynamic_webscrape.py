from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def extract_product_details(product_string):
    parts = product_string.split('\n')
    
    store_name = parts[0] if len(parts) > 0 else 'N/A'
    product_name = parts[1] if len(parts) > 1 else 'N/A'
    sale_price = parts[3].split(' ', 1)[1] if len(parts) > 3 else 'N/A'
    regular_price = parts[5] if len(parts) > 5 else 'N/A'

    return {
        'store_name': store_name,
        'product_name': product_name,
        'sale_price': sale_price,
        'regular_price': regular_price
    }

# Set up the web driver (using Edge in this case, can be swapped with other browsers)
driver = webdriver.Edge()

# URL of the website to scrape
url = "https://saamaan.pk/collections/accessories-and-gadgets"
driver.get(url)

try:
    products = []
    extracted_data = []

    # Wait for the elements to load and find them
    elements = driver.find_elements(By.CLASS_NAME, "product-item__info")
    element_wait = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-item__info"))
    )

    for elem in elements:
        products.append(elem.text)

    for product in products:
        product_extract = extract_product_details(product)
        extracted_data.append(product_extract)

    print(extracted_data)

    df = pd.DataFrame(extracted_data)
    df.to_csv('scraped_products.csv', index=False)
    print("Data saved to scraped_products.csv")

except Exception as e:
    print(f"An error occurred: {e}")
    
finally:
    driver.quit()
    driver.close()
