from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pandas as pd
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction
import requests

login_caps = {
    # "appium:appPackage": "com.moonvideo.android.resso",
    # "appium:appActivity": "com.anote.android.bach.app.SplashActivity",
    "platformName": "Android",
    "deviceName": "device",
    #"udid": "emulator-5554",
    #"udid": "192.168.8.121:37757",
    "udid": "f0a1be6b",
    "noReset": True
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", login_caps)

time.sleep(2)

driver.execute_script("mobile: deepLink", {'url': 'https://m.resso.com/Zs881H7gr/', 'package': 'com.moonvideo.android.resso'})

time.sleep(2)

el1 = driver.find_element(by=AppiumBy.ID, value="com.moonvideo.android.resso:id/moreIcon")
el1.click()

time.sleep(2)
el2 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView[2]")
el2.click()