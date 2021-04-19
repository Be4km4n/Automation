from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Dev/drivers/chromedriver.exe")

driver.get("https://techstepacademy.com/trial-of-the-stones")

# Assign Elements
inputStone = driver.find_element_by_css_selector("input[id='r1Input']")
buttonStone = driver.find_element_by_css_selector("button#r1Btn")
h4Stone = driver.find_element_by_xpath("//div[@id='passwordBanner']/h4")

inputPswd = driver.find_element_by_css_selector("Input#r2Input")
buttonSecrets = driver.find_element_by_css_selector("button#r2Butn")

# The Two Merchants
merchant = driver.find_element_by_xpath("//div/span/../p")
inputMerchant = driver.find_element_by_css_selector("input#r3Input")

# Manipulating elements
inputStone.send_keys('rock')
buttonStone.click()
inputPswd.send_keys(h4Stone.text)
buttonSecrets.click()

inputMerchant.send_keys(merchant.text)


