from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait #ilgili driverı bekleten yapı
from selenium.webdriver.support import expected_conditions as ec #beklenen koşullar
from selenium.webdriver.common.action_chains import ActionChains 

class Test_Sauce_Odev5:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.saucedemo.com")
        self.driver.maximize_window()
    
    
    def test_invalid_login(self):
        wdw = WebDriverWait(self.driver,5)
        usernameInput = wdw.until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = wdw.until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("1")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        errorMessage = self.driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")
    
    
    def urun_ekle(self):
        wdw = WebDriverWait(self.driver,5)
        usernameInput = wdw.until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = wdw.until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        addToCart = wdw.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']")))
        addToCart.click()
        shoppingCartLink = wdw.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='shopping_cart_container']/a")))
        shoppingCartLink.click()
        product = wdw.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='item_4_title_link']")))
        mesagge = product.text
        print(f"Sepetteki urun adı: {mesagge}")
        continueShopping = wdw.until(ec.visibility_of_element_located((By.XPATH,"//*[@id='continue-shopping']")))
        continueShopping.click()
        remove = wdw.until(ec.visibility_of_element_located((By.XPATH,"//*//*[@id='remove-sauce-labs-backpack']")))
        remove.click()  
        sleep(5)      
        

    def urun_inceleme(self):
        wdw = WebDriverWait(self.driver,5)
        usernameInput = wdw.until(ec.visibility_of_element_located((By.ID,"user-name")))
        usernameInput.send_keys("standard_user")
        passwordInput = wdw.until(ec.visibility_of_element_located((By.ID,"password")))
        passwordInput.send_keys("secret_sauce")
        loginButton = self.driver.find_element(By.ID,"login-button")
        loginButton.click()
        self.driver.execute_script("window.scrollTo(0,500)")
        itemName= self.driver.find_element(By.XPATH, "//*[@id='item_2_title_link']/div")
        itemNameText =itemName.text
        itemName.click()
        productTitle = self.driver.find_element(By.XPATH,"//*[@id='inventory_item_container']/div/div/div[2]/div[1]")
        productText = productTitle.text
        backButton = self.driver.find_element(By.XPATH,"//*[@id='back-to-products']")
        backButton.click()
        sleep(5)

        
testClass = Test_Sauce_Odev5()
#testClass.urun_ekle()
#testClass.urun_inceleme()
testClass.test_invalid_login()
