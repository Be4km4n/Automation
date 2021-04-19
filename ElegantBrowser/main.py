from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Dev/drivers/chromedriver.exe")
driver.get("https://techstepacademy.com/training-ground")

input2_locator = "input[id='ipt2']"
button4_locator = "//button[@id='b4']"

# Assign Elements
input2_elem = driver.find_element_by_css_selector(input2_locator)
btn4_elem = driver.find_element_by_xpath(button4_locator)

# Manipulate elements
input2_elem.send_keys('fabriciomelo')
btn4_elem.click()
