from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    base_url = 'https://www.abebooks.com/servlet/SearchEntry?cm_sp=TopNav-_-Advs-_-Advs'
    search_keyword = "Russel and Norvig"

    # Provide the path of chromedriver present on your system.
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",
                              options=options)

    # Send a get request to the url
    driver.get(base_url)
    driver.implicitly_wait(10)
    # search_box = driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']")
    search_box = driver.find_element_by_id('keyword')
    # driver.find_element(By.XPATH, './/input[@class="gnav-searchbox-input"]')
    driver.implicitly_wait(5)
    # search_button = driver.find_element_by_xpath("//input[@id='nav-search-submit-button']")
    search_button = driver.find_element(By.ID, 'search-button')
    driver.implicitly_wait(5)
    search_box.send_keys(search_keyword)
    driver.implicitly_wait(5)
    search_button.submit()
    driver.implicitly_wait(5)

    product_asin = []
    product_name = []
    product_price = []
    product_ratings = []
    product_ratings_num = []
    product_link = []
    authors = []

    items = wait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[contains(@class, "cf result-item")]')))

    for item in items:
        name = item.find_element(By.XPATH, './/span[@data-cy="listing-title"]').text
        author = item.find_elements(By.XPATH, './/p[@class="author"]/strong').text
        currency, price = item.find_elements(By.XPATH, '//p[@class="item-price"]').text.split(' ')
        # ratings_box = item.find_elements(By.XPATH, './/div[@class="a-row a-size-small"]/span')
        # data_asin = item.get_attribute("data-asin")
        # whole_price = item.find_elements(By.XPATH, './/span[@class="a-price-whole"]')
        # fraction_price = item.find_elements(By.XPATH, './/span[@class="a-price-fraction"]')
        # link = item.find_element(By.XPATH, './/a[@class="a-link-normal a-text-normal"]').get_attribute("href")

        product_name.append(name)
        authors.append(author)
        product_price.append(price)
        # product_asin.append(data_asin)

        # if whole_price and fraction_price:
        #     price = '.'.join([whole_price[0].text, fraction_price[0].text])
        # else:
        #     price = 0
        # product_price.append(price)
        #
        # if ratings_box:
        #     ratings = ratings_box[0].get_attribute('aria-label')
        #     ratings_num = ratings_box[1].get_attribute('aria-label')
        # else:
        #     ratings, ratings_num = 0, 0
        #
        # product_ratings.append(ratings)
        # product_ratings_num.append(str(ratings_num))
        # product_link.append(link)

    driver.quit()

    print(product_name)
    # print(product_asin)
    print(authors)
    print(product_price)
    # print(product_ratings)
    # print(product_ratings_num)
    # print(product_link)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
