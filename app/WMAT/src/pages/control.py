from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from src.helper.wait_util import Waiter
from appium.webdriver.common.mobileby import MobileBy
from src.driver import MyDriver


class Control(object):
    def __init__(self, case):
        self.wait = Waiter.getInstance()
        self.driver = case.driver
        # add new method to the `find_by_*` pantheon
        By.IOS_UIAUTOMATION = MobileBy.IOS_UIAUTOMATION
        By.ANDROID_UIAUTOMATOR = MobileBy.ANDROID_UIAUTOMATOR
        By.ACCESSIBILITY_ID = MobileBy.ACCESSIBILITY_ID


    '''
    regular match by input text, ios name or classname contatis '.'
    '''
    def find_element(self, locator,ios_name):
        _type = self.dispatch_locator_text(locator,ios_name)
        return self.find_element_by_located(_type, locator)

    def validate(self, locator):
        if not locator:
            return False


    def dispatch_locator_text(self, locator,ios_name):
        if locator.find('//') > -1:
            return By.XPATH
        elif locator.find('.') > -1 and not MyDriver.is_ios(self.driver):
            return By.CLASS_NAME
        else:
            if MyDriver.is_ios(self.driver):
                if ios_name:
                    return MobileBy.ACCESSIBILITY_ID
                else:
                    return By.CLASS_NAME
            else:
                return By.ID


    def find_element_by_located(self,_type,locator):
        try:
            return self.wait(self.driver, EC.presence_of_element_located((_type, locator)))
        except AttributeError:
            print("未能找到 %s 元素" % (locator))
        else:
            return self.wait(self.driver, EC.presence_of_element_located((_type, locator)))

    def find_elements_by_located(self,_type,locator):
        try:
            return self.wait(self.driver, EC.presence_of_all_elements_located((_type, locator)))
        except AttributeError:
            print("未能找到 %s 元素" % (locator))
        else:
            return self.wait(self.driver, EC.presence_of_all_elements_located((_type, locator)))


    def find_elements(self, locator):
        _type = By.CLASS_NAME
        return self.find_elements_by_located(_type, locator)




    AND_TEXT = 'text'
    IOS_TEXT ='label'
    AND_CLASS_TEXT_VIEW = 'android.widget.TextView'
    IOS_CLASS_TEXT_VIEW = 'UIAStaticText'
