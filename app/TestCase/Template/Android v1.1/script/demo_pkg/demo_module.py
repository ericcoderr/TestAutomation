'''
自定义函数，函数名没有限制
必须要有一个入参，接收由框架构造的环境
接收的参数由如下工具可以扩展使用：
control:控件定位器，可以使用封装好的方法获取页面控件
action：可以使用封装好的方法执行操作
driver：当前连接的设备，最基础的工具，必须通过这个获取设备
当自定义函数用于expectation的操作时，必须返回bool值
由于自定义函数中的入参case，是一个unittest，可以直接在函数中做校验操作如：case.assertTrue(a==b)
'''
class DemoClass:
    def run_action(self,case):
        elementstr = '//android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.ScrollView[1]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.EditText[1]'
        this_element = case.control.find_element(elementstr)
        case.action.disptach_action(this_element, 'type', '18026587555')

    def check(self,case):
        return True
