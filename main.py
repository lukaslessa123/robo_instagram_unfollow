from logging import exception
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class InstaUnfollow:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()
        

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        sleep(3)
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        sleep(3)
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        sleep(3)
        password_element.send_keys(Keys.RETURN)
        sleep(5)
        
        self.enter = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').send_keys(Keys.ENTER)
        sleep(3)

        self.enter = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').send_keys(Keys.ENTER)
        sleep(5)


    def Unfallow(self):

        self.driver.get("https://www.instagram.com/flipwashfortaleza/following/")
        sleep(5)

        self.unfollow = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
            .click()
        sleep(5)
                  
        try:
                for i in range(50):
                    
                    self.driver.find_element_by_xpath('//button[text()="Seguindo"]')\
                        .click()
                    print("Etapa unfollow 1")
                    sleep(1)
                    
                    self.driver.find_element_by_xpath('//button[text()="Deixar de seguir"]')\
                        .click()
                    print("Etapa unfollow 2")
                    sleep(5)
        except Exception as e:
            sleep(5)
                
        



                
                
        #except:
        #    pass

swellmkt = InstaUnfollow("flipwashfortaleza", "sucesso020920")
swellmkt.login()
swellmkt.Unfallow()