from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=r"C:\chromedriver")
driver.get('https://web.whatsapp.com/')

message='Sab yaad rkha jaega!'
name='Priyanshu Raj'

k=input()

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(name))

user.click()

box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')

while True:
    box.send_keys(message)
    send = driver.find_element_by_xpath(
        '//*[@id="main"]/footer/div[1]/div[3]/button/span')
    send.click()
