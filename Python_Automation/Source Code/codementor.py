import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login_user(driver):
    driver.get("https://cart.beverlyhillsmd.com/login")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "log-in-button")))

    elem = driver.find_element(By.ID, 'username-input')
    elem.send_keys(os.environ.get('USERNAME'))
    elem = driver.find_element(By.ID, 'password-input')
    elem.send_keys(os.environ.get('PASSWORD'))
    elem = driver.find_element(By.CLASS_NAME, "log-in-button")
    elem.click()


def add_product(driver):
    driver.get("https://cart.beverlyhillsmd.com/cart?product1=a0N3w000012soESEAY")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="Checkout"]')))

    elem = driver.find_element(By.XPATH, '//button[text()="Checkout"]')
    elem.click()


def main():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920x1080")

    driver = webdriver.Chrome(options=chrome_options)

    login_user(driver)
    add_product(driver)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="SUBMIT ORDER"]')))
    time.sleep(3)

    # Country
    elem = driver.find_element(By.XPATH, "//shipping-address-form/div/form/div[3]/dropdown-input/div/div/div/div/span/select")
    # ActionChains(self.driver).move_to_element(element).click().perform()
    elem.click()
    elem.send_keys("Ca")
    elem.send_keys(Keys.RETURN)

    # State
    elem = driver.find_element(By.XPATH, "//shipping-address-form/div/form/div[5]/dropdown-input/div/div/div/div/span/select")
    elem.click()
    elem.send_keys("On")
    elem.send_keys(Keys.RETURN)

    # Credit card
    elem = driver.find_element(By.XPATH, '//*[@id="cardType"]/div/div/div/div/span/select')
    elem.click()
    elem.send_keys("Vi")
    elem.send_keys(Keys.RETURN)

    elem = driver.find_element(By.XPATH, '//*[@id="paymentInfoForm"]/div/form/div[5]/text-input/div/div/div/div/span/input')
    elem.send_keys("4111111111111111")

    elem = driver.find_element(By.XPATH, '//*[@id="paymentInfoForm"]/div/form/div[6]/text-input/div/div/div/div/span/input')
    elem.send_keys("J S")
    
    elem = driver.find_element(By.XPATH, '//*[@id="paymentInfoForm"]/div/form/div[7]/div[1]/text-input/div/div/div/div/span/input')
    elem.send_keys("111")
    
    elem = driver.find_element(By.XPATH, '//*[@id="paymentInfoForm"]/div/form/div[7]/div[3]/text-input/div/div/div/div/span/input')
    elem.send_keys("10/24")

    elem = driver.find_element(By.XPATH, '//button[text()="SUBMIT ORDER"]')
    print(elem.is_enabled())

    time.sleep(500)
    driver.close()


if __name__ == "__main__":
    main()