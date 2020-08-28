from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r"C:\chromedriver")
driver.get('https://web.whatsapp.com/')

message='haha'
name='Yasser'
path=r'C:\Users\yusuf\Downloads\minion.jpg'

k=input()

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))
user.click()

for i in range(1000):
    attach = driver.find_element_by_xpath(
        '//div[@title="Attach"]')
    attach.click()

    image = driver.find_element_by_xpath(r'//*[@id="main"]/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input')
    image.send_keys(path)

    sleep(3)

    send_btn = driver.find_element_by_xpath(
        r'//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
    send_btn.click()

