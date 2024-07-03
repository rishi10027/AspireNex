from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def scrape_product(url):
    options = Options()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')  # Required for running as root
    options.add_argument('--disable-dev-shm-usage')  # Overcome limited resource problems
    options.add_argument('--disable-gpu')  # Disable GPU hardware acceleration
    options.add_argument('--window-size=1920,1200')  # Set window size to avoid errors
    
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    
    driver.get(url)

    title = extract_title(driver)
    price = extract_price(driver)
    specifications = extract_specifications(driver)

    driver.quit()

    product = {
        'title': title,
        'price': price,
        'specifications': specifications
    }
    return product

def extract_title(driver):
    try:
        title = driver.find_element(By.ID, 'productTitle').text.strip()
    except:
        try:
            title = driver.find_element(By.CLASS_NAME, 'VU-ZEz').text.strip()
        except:
            title = "Title not found"
    return title

def extract_price(driver):
    try:
        price = driver.find_element(By.ID, 'ppdBundlesPriceValueId').text.strip()
    except:
        try:
            price_element = driver.find_element(By.CLASS_NAME, 'CxhGGd')
             # Extract the price text from the element
            price = price_element.text.strip()
        except:
            price = "Price not found"
    return price

def extract_specifications(driver):
    try:
        specifications_section = driver.find_element(By.ID, 'feature-bullets')
        specifications = specifications_section.find_elements(By.CLASS_NAME, 'a-list-item')
        specifications = [spec.text.strip() for spec in specifications]
    except:
        try:
            specifications_section = driver.find_element(By.CLASS_NAME, 'Xbd0Sd')
            specifications = specifications_section.find_elements(By.CLASS_NAME, '_4gvKMe')
            specifications = [spec.text.strip() for spec in specifications]
        except:
            specifications = ["Specifications not found"]
    return specifications
