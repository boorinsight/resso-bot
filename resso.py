from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

login_caps = {
    "appium:appPackage": "com.moonvideo.android.resso",
    "appium:appActivity": "com.anote.android.bach.app.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    #"udid": "emulator-5554",
    #"udid": "192.168.8.121:37757",
    "udid": "J9AXGF00S840NWB",
    "noReset": False
}

boot_caps = {
    "platformName": "Android",
    "deviceName": "device",
    #"udid": "emulator-5554",
    #"udid": "192.168.8.121:37757",
    "udid": "J9AXGF00S840NWB",
    "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", login_caps)

driver.implicitly_wait(5)
#time.sleep(5)

try:
    el0 = driver.find_element(by=AppiumBy.ID, value="com.moonvideo.android.resso:id/ivClose")
    el0.click()
except:
    pass

driver.implicitly_wait(10)
#time.sleep(2)
el2 = driver.find_element(by=AppiumBy.ID, value="com.moonvideo.android.resso:id/googleText")
el2.click()

driver.implicitly_wait(10)
#time.sleep(3)
el3 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView[2]")

#driver.implicitly_wait(10)
time.sleep(5)
try:
    if el3.text == "genshinio3099k@nzcho.my.id":
        el3.click()
    else:
        pass
except:
    pass

try:
    #driver.implicitly_wait(10)
    time.sleep(3)
    driver.swipe(540, 1142, 540, 998, 400)

    #driver.implicitly_wait(10)
    time.sleep(3)
    el4 = driver.find_element(by=AppiumBy.ID, value="com.moonvideo.android.resso:id/userAgeGateBtn")
    el4.click()
except:
    pass
driver.close_app()

print("opening the songlist")
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", boot_caps)
driver.execute_script("mobile: deepLink", {'url': 'https://m.resso.com/Zs881H7gr/', 'package': 'com.moonvideo.android.resso'})

driver.implicitly_wait(13)
#time.sleep(10)

try:
    el5 = driver.find_element(by=AppiumBy.ID, value="com.moonvideo.android.resso:id/ifvVipRefinedCloseBtn")
    el5.click()
except:
    pass

#time.sleep(4)
song_title = pd.read_csv("https://docs.google.com/spreadsheets/d/e/2PACX-1vQnmNV7VV6BvQIV7nT1eJOHCPn3N6B279um4K6160d2i5OsDvmvkrKFfSkzFq-lipf542403H0t8IqK/pub?gid=0&single=true&output=csv")
driver.implicitly_wait(10)
for i in song_title["title"]:
    el6 = driver.find_element(by=AppiumBy.XPATH, value=f"//android.widget.TextView[@text='{i}']")
    el6.click()
    time.sleep(5)
    # try:
    #     el8 = driver.find_element(by=AppiumBy.XPATH, value="//android.view.View[@content-desc=\"Install\"]/android.widget.TextView")
    #     el8.click()
    #     time.sleep(3)
    #     el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.TextView[@text='More info']")
    #     el9.click()
    # except:
    #     pass
    # driver.swipe(540, 1277, 540, 1150, 400)
    # time.sleep(5)
    # driver.back()
time.sleep(10)
driver.close_app()