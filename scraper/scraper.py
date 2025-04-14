from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get("https://linktr.ee/jayden")
time.sleep(5)
driver.find_element("xpath", "//*[@id=\"links-container\"]/div[4]/div/div/div[3]").click()  # click on search buttom

thousButt = driver.find_element("xpath", "//*[@id=\"headlessui-dialog-panel-2\"]/div[2]/div/div/div[3]/form/div/div/div/input[1]")
hundsButt = driver.find_element("xpath", "//*[@id=\"headlessui-dialog-panel-2\"]/div[2]/div/div/div[3]/form/div/div/div/input[2]")
tensButt = driver.find_element("xpath", "//*[@id=\"headlessui-dialog-panel-2\"]/div[2]/div/div/div[3]/form/div/div/div/input[3]")
onesButt = driver.find_element("xpath", "//*[@id=\"headlessui-dialog-panel-2\"]/div[2]/div/div/div[3]/form/div/div/div/input[4]")

initial1 = 0
initial2 = 0
initial3 = 0
initial4 = 0

for  thous in range (initial1,10):
    thousButt.click()
    thousButt.clear()
    thousButt.send_keys(thous)

    for hunds in range (initial2, 10):
        hundsButt.click()
        hundsButt.clear()
        hundsButt.send_keys(hunds)
        initial2 = 0

        for tens in range(initial3, 10):
            tensButt.click()
            tensButt.clear()
            tensButt.send_keys(tens)
            initial3 = 0

            for ones in range(initial4, 10):
                onesButt.click()  # click on search buttom
                onesButt.clear()
                onesButt.send_keys(ones)
                confirmButt = driver.find_element("xpath", "//*[@id=\"headlessui-dialog-panel-2\"]/div[2]/div/div/div[2]/form/div/button")
                confirmButt.click()
                print("{} {} {} {}".format(thous, hunds, tens, ones))
                time.sleep(.65)
                initial4 = 0
                

#driver.close()