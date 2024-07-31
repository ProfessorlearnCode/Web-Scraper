## README.md

# Web Scraping Project

This repository contains two Python scripts for web scraping, each designed to extract product information from a website. The scripts cater to different types of content rendering: static and dynamic JavaScript rendering. The scraped data, including product names, sale prices, and regular prices, is saved into a CSV file for further analysis or use.

## Table of Contents

- [Overview](#overview)
- [Setup and Installation](#setup-and-installation)
  - [Prerequisites](#prerequisites)
  - [Installing Dependencies](#installing-dependencies)
  - [WebDriver Installation](#webdriver-installation)
- [Usage](#usage)
  - [Static Rendering Web Scraper](#static-rendering-web-scraper)
  - [Dynamic JS Rendering Web Scraper](#dynamic-js-rendering-web-scraper)
- [Output](#output)
- [Error Handling & Logging](#error-handling--logging)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Overview

### Static Rendering Web Scraper

This script uses BeautifulSoup to parse a locally stored HTML file (`Accessories And Gadgets.html`). It extracts the product names, sale prices, and regular prices from the HTML content and stores the data in a CSV file.

### Dynamic JS Rendering Web Scraper

The dynamic scraper utilizes Selenium WebDriver to interact with a live website. It is designed to handle JavaScript-rendered content by waiting for elements to load and extracting relevant product information, which is then saved in a CSV file.

## Setup and Installation

### Prerequisites

- Python 3.x
- `pip` (Python package installer)

### Installing Dependencies

For the static web scraper:

```bash
pip install beautifulsoup4 pandas
```

For the dynamic web scraper:

```bash
pip install selenium pandas
```

### WebDriver Installation

The dynamic scraper requires a browser-specific WebDriver. For instance, if using Microsoft Edge, you need the Edge WebDriver. Ensure the WebDriver is available in your system's PATH.

Example for Edge:

```bash
pip install msedge-selenium-tools
```

Ensure the WebDriver executable is compatible with the installed browser version.

## Usage

### Static Rendering Web Scraper

1. Place the HTML file (`Accessories And Gadgets.html`) in the same directory as the script.
2. Run the script to parse the HTML file and save the extracted data to a CSV file.

```bash
python static_scraper.py
```

### Dynamic JS Rendering Web Scraper

1. Ensure the WebDriver is correctly set up and accessible.
2. Update the URL in the script to the desired webpage.
3. Run the script to navigate the webpage, extract product data, and save it to a CSV file.

```bash
python dynamic_scraper.py
```

## Output

Both scripts will generate a CSV file (`scraped_products.csv`) containing the scraped product data with the following columns:

- `Product Name`
- `Sale Price`
- `Regular Price`

## Error Handling & Logging

### Static Rendering Web Scraper

- The script includes try-except blocks to handle cases where specific elements, such as sale prices or regular prices, may not be present.
- Errors during processing are logged to the console for troubleshooting.

### Dynamic JS Rendering Web Scraper

- The script waits for specific elements to load using WebDriverWait, ensuring dynamic content is fully rendered before extraction.
- Errors encountered during scraping are caught and printed to the console, and the browser is closed properly in the `finally` block.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find bugs, please fork the repository and create a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgments

- **BeautifulSoup**: For providing a powerful HTML/XML parsing library.
- **Selenium**: For enabling browser automation and web scraping of dynamically rendered content.
- **Pandas**: For easy data manipulation and storage in CSV format.

---

Feel free to customize this README file as needed to better suit your project's specific details or requirements.
