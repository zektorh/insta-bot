from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import random

from selenium.webdriver.common.proxy import Proxy, ProxyType

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL
prox.http_proxy = "ip_addr:port"
prox.socks_proxy = "ip_addr:port"
prox.socks_version = 5
prox.ssl_proxy = "ip_addr:port"

capabilities = webdriver.DesiredCapabilities.CHROME

driver = webdriver.Chrome()

x = 0
while x < 21 :
    driver.get('https://www.instagram.com/accounts/emailsignup/')

    sleep(10)

    emailOrNumber = driver.find_element(By.NAME, 'emailOrPhone').send_keys('09188687133') #  باید شماره خودتون باشه یا ایمیلتون
    sleep(2)
    FullName = driver.find_element(By.NAME, 'fullName').send_keys('hosseinazimi')
    sleep(1)

    y = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 0, ]

    RandomWord = 'abcdefghijklomnpqrstuvwxyz'

    UserName = driver.find_element(By.NAME, 'username').send_keys(f"none.{random.choice(y)}{random.choice(RandomWord)}{random.choice(y)}")
    sleep(2)
    Password = driver.find_element(By.NAME, 'password').send_keys(f"nonepass.{random.choice(y)}{random.choice(RandomWord)}{random.choice(y)}")

    sleep(15)
    signBTN = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div[5]/div/button').click()

    sleep(7)

    yearselect = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select').click()
    sleep(1)
    year = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[45]').click()
    sleep(4)
    NextBtn = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div[6]/button').click()
    sleep(15)
    inp = int(input('enter the code:  '))

    sleep(15)
    code = driver.find_element(By.NAME, 'confirmationCode').send_keys(inp)
    sleep(20)
    codeBTN = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div/div/div/form/div[2]/button').click()
    sleep(20)
    driver.get('https://www.instagram.com')
    sleep(10)
    x = x + 1


