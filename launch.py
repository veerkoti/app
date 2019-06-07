import subprocess
import time
from appium import webdriver

class install_and_launch:
    def __init__(self):
        self.driver = None
        self.url = 'http://localhost:4723/wd/hub'
        self.dc = {
            #'browserName':'Chrome',
            'automationName':'UiAutomator2',
            'platformName':'Android',
            'deviceName':'e8250781',
            'platformVersion':'9'
        }
    def install_and_launch(self,app):
        self.dc['app']=app
        server = subprocess.Popen(["D:/Downloads/Appium/appium_server/node.exe","D:/Downloads/Appium/appium_server/appium/build/lib/main.js"])
        time.sleep(5)
        self.driver = webdriver.Remote(self.url,self.dc)

launch_obj = install_and_launch()
launch_obj.install_and_launch('D:/Downloads/Appium/appium_server/appium/node_modules/appium-uiautomator2-server/app/src/androidTestE2eTest/java/io/appium/uiautomator2/unittest/resource/ApiDemos-debug.apk')
text_objects = launch_obj.driver.find_elements_by_class_name('android.widget.TextView')
# textbox_objects = launch_obj.driver.find_elements_by_class_name('android.widget.EditText')
print('text_objects',text_objects)
# print('textbox_objects',textbox_objects)