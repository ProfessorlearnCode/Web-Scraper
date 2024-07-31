from bs4 import BeautifulSoup
import pandas as pd

with open("Accessories And Gadgets.html", "r") as file:
    html = BeautifulSoup(file, "html.parser")

product_names = html.find_all('a', class_='product-item__title text--strong link')
sale_prices = html.find_all('span', class_='product-label product-label--on-sale')
regular_prices = html.find_all('span', class_='price price--compare')

product_data = []


for index, name_tag in enumerate(product_names):
    try:
        product_name = name_tag.text.strip()

        try:
            sale_price = sale_prices[index].text.strip()
        except IndexError:
            sale_price = None  # Sale price not available

        try:
            regular_price = regular_prices[index].text.strip()
        except IndexError:
            regular_price = None  # Regular price not available

        product_data.append({
            'Product Name': product_name,
            'Sale Price': sale_price,
            'Regular Price': regular_price
        })
    except Exception as e:
        print(f"Error processing product: {e}")

df = pd.DataFrame(product_data)
df.to_csv('scraped.csv', index=False)

print(f"Data saved to scraped_products.csv")
