import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

with open("login.txt", "r+") as file:
    content = file.readlines()

username = content[0].split("=")[1][1:-2]
password = content[1].split("=")[1][1:-2]
path = content[2].split("=")[1][1:-1] + "\chromedriver.exe"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automaition"])
driver = webdriver.Chrome(path, chrome_options = chrome_options)
driver.get("https://entrar.in/login/login")

actions = ActionChains(driver)

#Login section
try:
    username_feild = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
except:
    print("probably the website is down")

username_feild.send_keys(username)

password_feild = driver.find_element_by_name("password")
password_feild.send_keys(password)

capchta = driver.find_element_by_class_name("label-input100")
print(capchta.text)
capchta_result = int(capchta.text[0]) + int(capchta.text[4])

capchta_feild = driver.find_element_by_name("captcha")
capchta_feild.send_keys(capchta_result)
capchta_feild.send_keys(Keys.RETURN)
print("Signed in")

#online classroom section
driver.implicitly_wait(5)
driver.get("https://entrar.in/classroom_creation_crm_new/s_display")
print("reached")

try:
    join_class = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//tbody[1]/tr[6]/td[5]/a"))  
    )
except:
    print("Class is not yet enabled")

#join class section
driver.get(join_class.get_attribute("href"))
print("joined")