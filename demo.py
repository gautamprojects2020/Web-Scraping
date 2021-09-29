import time
from openpyxl import Workbook
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Chrome Browser Will Open
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
# Amazon Site Will Open
driver.get("https://www.amazon.in/")
time.sleep(5)
# Will Search For Samsung Phones
driver.find_element(
    By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("samsung phones")
driver.find_element(By.XPATH, "//input[@value='Go']").click()
driver.find_element(By.XPATH, "//span[text()='Samsung']").click()
# We Will Collect Names and Price of phonr in list
phonenames = driver.find_elements(
    By.XPATH, "// span[contains(@class,' a-color-base a-text-normal')]")
prices = driver.find_elements(
    By.XPATH, "// span[contains(@class,'a-price-whole')]")
# Will Store Data in respective Empty List
Phone_Names = []
Price_List = []
for phone in phonenames:

    Phone_Names.append(phone.text)

for price in prices:
    Price_List.append(price.text)

# Here We join two list in tuple through zip function

final_list = zip(Phone_Names, Price_List)

# Here We Save the Data in Excel

wb = Workbook()
wb['Sheet'].title = 'Samsung Price_Data'
sh1 = wb.active
sh1.append(['Samsung_Model_Name', 'Price'])

for x in list(final_list):
    sh1.append(x)
wb.save("Final1.xlsx")
# Here We will close our Chrome Browser
driver.quit()
