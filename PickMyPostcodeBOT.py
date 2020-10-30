from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://pickmypostcode.com")
sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/nav/ul/li[5]/button[2]").click()
sleep(2)
driver.find_element_by_xpath('//*[@id="confirm-ticket"]').send_keys("Enter Postcode Here")
driver.find_element_by_xpath('//*[@id="confirm-email"]').send_keys("Enter Email Here")
driver.find_element_by_xpath('//button[@type="submit"]').click()
sleep(5)
driver.get("https://pickmypostcode.com/video")
sleep(5)
driver.get("https://pickmypostcode.com/survey-draw/")
sleep(5)
driver.get("https://pickmypostcode.com/your-bonus/")
driver.close()