
from selenium import webdriver
# if chromedriver is not in your path, you’ll need to add it here
driver = webdriver.Chrome(r'J:\INLO\Selenium\chromedriver.exe')
#driver.get("https://esig-sandbox.ch/team20_3_v2/environnement_dev/index.php")
#button_nav = driver.find_element_by_class_name("navbar-toggler")
#button_nav.click()
#bouton_connect= driver.find_element_by_class_name("nav-link font-weight-bold ")
#bouton_connect.click()
pageUrl = "http://www.seleniumeasy.com/test/basic-first-form-demo.html"
driver.maximize_window()
driver.get(pageUrl)
assert "Selenium Easy Demo - Simple Form to Automate using Selenium" in driver.title
eleUserMessage = driver.find_element_by_id("user-message")
eleUserMessage.clear()
eleUserMessage.send_keys("Test Python")
eleShowMsgBtn=driver.find_element_by_css_selector('#get-input > .btn')
eleShowMsgBtn.click()

eleYourMsg=driver.find_element_by_id("display")
assert "Test Python" in eleYourMsg.text
#driver.close()
