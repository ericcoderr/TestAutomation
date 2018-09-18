
from src.helper.wait_util import Waiter
from time import sleep
from src.common.constant import Field
from src.helper.script_helper import Script
import re
from src.driver import MyDriver

class Actions(object):

    def disptach_action(self,element,action,data):
        if action == Field.ACTION_TYPE:
            self.send_keys(data, element)
        elif action == Field.ACTION_CLICK:
            self.click(element)
        elif action == Field.ACTION_TYPEENTER:
            self.send_keys(data+"\n",element)
        elif action == Field.ACTION_TAP:
            self.tap(data)
        elif action == Field.ACTION_SWIPE:
            self.swipe(data)
        elif action == Field.ACTION_FLICK:
            self.flick(data)
        elif action == Field.ACTION_WAIT:
            self.wait(data)
        elif action == Field.ACTION_SWITCH_TO_NATIVE:
            self.switch_to_native()
        elif action == Field.ACTION_SWITCH_TO_WEBVIEW:
            self.switch_to_webview()
        elif re.match('^\${.*}$', action, flags=0):
            self.run_script(re.sub(r'^\${(.*)}$', r'\1', action))
        elif action == Field.ACTION_SWITCH_TO_APP:
            self.switch_to_app(data)
        elif action == Field.ACTION_BACKGROUND_APP:
            self.background_app(data)
        elif action == Field.ACTION_CURRENT_ACTIVITY:
            self.get_current_activity()
        elif action == Field.ACTION_TYPE_EXT:
            self.type_ext(data,element)

    def switch_to_native(self):
        self.driver.switch_to.context('NATIVE')

    def switch_to_webview(self):
        self.driver.switch_to.context('WEBVIEW')


    def __init__(self,case):
        self.waiter = Waiter.getInstance()
        self.driver = case.driver
        self.case = case
        self.x = self.driver.get_window_size()['width']
        self.y = self.driver.get_window_size()['height']

    def run_script(self, script):
        mtd = Script.get_attr(script)
        mtd(self.case)

    def send_keys(self,text,element):
        # self.waiter.wait(self.driver, element).send_keys(text)
        element.clear()
        element.send_keys(text)

    def click(self, element):
        element.click()

    def tap(self, data):
        postions=[self.exchange_percent(data)]
        self.waiter.implicitly_wait(self.driver)
        self.driver.tap(postions)

    def swipe(self, data):
        postions = self.exchange_percent(data)
        self.waiter.implicitly_wait(self.driver)
        if MyDriver.is_ios(self.driver):
            if len(postions) == 5:
                self.driver.swipe(postions[0], postions[1], postions[2]-postions[0], postions[3]-postions[1],postions[4])
            else:
                self.driver.swipe(postions[0], postions[1], postions[2]-postions[0], postions[3]-postions[1],5000)
        else:
            if len(postions) ==5:
                self.driver.swipe(postions[0],postions[1],postions[2],postions[3],postions[4])
            else:
                self.driver.swipe(postions[0],postions[1],postions[2],postions[3],5000)

    def flick(self, data):
        postions = self.exchange_percent(data)
        self.waiter.implicitly_wait(self.driver)
        if MyDriver.is_ios(self.driver):
            self.driver.flick(postions[0], postions[1], postions[2]-postions[0], postions[3]-postions[1])
        else:
            self.driver.flick(postions[0],postions[1],postions[2],postions[3])

    def wait(self, data):
        if type(data)==int:
            sleep(data)
            return
        if str.isdigit(data):
            sleep(int(data))
            return


    def exchange_percent(self,data):
        new_p = []
        postions = data.split(',')
        for index in range(len(postions)):
            if '%' in postions[index]:
                if index % 2 == 0:
                    new_p.append(int(postions[index][:-1])/ 100 * self.x)
                else:
                    new_p.append(int(postions[index][:-1])/ 100 * self.y)
            else:
                new_p.append(postions[index])
        return new_p

    def switch_to_app(self,data):
        '''
        Not support dynmic param
        '''
        apps=data.split(',')
        package=apps[0]
        activity=apps[1]
        self.driver.start_activity(package, activity)

    def background_app(self,data):
        '''
        Unit second
        '''
        self.driver.background_app(data)

    def get_current_activity(self):
        self.driver.current_activity

    def type_ext(self,data,element):
        actual=''
        i=0
        while True:
            element.clear()
            data_arr=list(data)
            j=0
            for key_code in data_arr:
                self.press_key_code(int(key_code)+7)
                text=element.get_attribute('text')
                #如果当前长度超过预期的值说明多输入了一个数字，需要回删一个字符  
                if len(str.replace(text,' ','')) > j+1:
                    print('长度输入超过预期，需要回删一个字符')
                    self.press_key_code(67)

                if  j==len(data_arr)/2:
                    element.click()
                    self.press_key_code(123)
                j+=1

            actual=str.replace(element.get_attribute('text'),' ','')
            print('第'+str(i)+'次尝试,期望值:'+str(data)+',实际值:'+str(actual))
            i+=1
            if actual!= data:
                element.clear()

            if actual==data or i >10:
                break
        pass

    def press_key_code(self,key_code):
        self.driver.keyevent(key_code)
        sleep(1)

