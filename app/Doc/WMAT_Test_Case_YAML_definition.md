
<center><H1> WMAT Test Case YML definition </H1>v0.9</center>

## 目录

* [Page Step](#page_step)  
  * [element](#element)
  * [action](#action)
  * [data](#data)
  * [expectation](#expectation)
* [Scenario](#scenario)
* [Test Case](#test_case)
* [扩展－自定义函数](#customization)
* [WebView/Html 支持](#webview_support)
* [单个Test Case的中间数据结构](#internal_data_structure)
* [Test Case的组织结构及命名规范](#naming_convention)

# 正文

基于UI的操作基本都由3个要素构成：元素，操作和结果校验，他们都封装在Page Step里。Pages Step 是最基础的单元，定义了控件和操作。操作可以接受输入参数，这样就把控件定义和数据分开了。我们的整个test case的组织都是基于Page，每个Page一个文件。

Scenario 就是“自动化用例”文档中的每个测试点（Item）。是Page Steps 组成的逻辑操作块。可以给Page Step 传参数。

Test case 是Scenario的组合, 可以在Test case里指定输入的参数值。

## <a name="page_step"></a>Page Step

Page Steps 以 UI 页面为单位，定义了一个页面上的所有单元操作。它就相当于最底层的一个函数。下面的例子是一个在“我的账户”页面上，进入登录页面的这个动作的Page Step：
​	
example: /pages/tabbar/MyAccount.yml
​	
```
enter_login_page:
	element: tablecellMyAccountLogin
   	action: click
   	expectation: 
		- ’登录‘
   		- ’注册‘
   	desc: 进入登录页面
```
Note: expectation中的字符只能用单引号
​		
example: `/pages/tabbar/Login.yml`
​		
```
input_username:
	element: txtfieldUserName
	action: type
	data: 'Eric'
	desc: 输入用户名
			
input_password:
 	element: $password_element
  	action: type
 	data: $password
	
click_login_button:
	element: btnLogin
	action: click
	expectation: $mobilephone
	   	
search:
	action: ${search}
	data: $keyword
```

### Step

一个Step可以由 element/action/data/expectation/desc 5个元素构成。其中，只有action是必须的，其他三个元素都可选。

#### <a name="element"></a>element

element 用来定位一个控件。它可以自动识别后面跟的参数类型从而调用相应的定位方法，主要包括 id，xpath和class name。比如：

* `element: btnLogin`  此时可判断出参数为id，自动调用 `find_element_by_id` 方法定位  
* `element: //UIANavigationBar[1]/UIAButton[2]` 此时可判断出参数为xpath，可自动调用`find_element_by_xpath` 方法  
* `element: android.widget.LinearLayout` 此时可判断出参数为class name，自动调用`find_element_by_class_name 方法`
* `element: $product_element` element 元素可以设置为变量，在编写test case时才传入实际的值
* <mark>pending：是否要考虑加一个参数，比如返回控件集合再加一个索引。主要指在by_classname的时候。也可以自己封装实现 xx.xxxx.xxxx[2] 这样的语法</mark>


#### <a name="action"></a>Action

Action目前支持以下类型：

* `click` 点击。此时action不带参数
* `type` 输入字符，此时action需要带参数Data。Data域的说明见下。
* `tap` 轻击屏幕上的某个坐标，需要输入坐标值x, y。如：

```
  action: tap
  data: 35, 45
```

​      坐标也支持百分比的方式，如： 

```
  action: tap
  data: 40%, 52%
```

* `swipe` 从屏幕上坐标x1, y1 滑动到 x2, y2:

```
  action: swipe
  data: x1, y1, x2, y2
```

* `flick` 与`swipe`类似，只是flick为快速滑动：

```
  action: flick
  data: x1, y1, x2, y2
```


* `wait` 等待一段时间，单位为秒。默认为10秒，可在配置文件中修改此默认值。

```
  action: wait
  data: 10
```

* `typeEnter` 在输入框中输入值后按回车，在iOS 搜索时比较有用

```
  action: typeEnter
  data: 饼干
```
* action 也可以支持自定义函数以适应特殊业务需求(比如“清空购物车”这一系列动作)，此处为扩展点，如：
  `action: ${package.module.Class.function}`

  <mark>post a example</mark>

  此时clear_cart 这个函数应该定义在同目录下同名的.py 文件中（需要继承某个父类）。
  扩展的函数也可以调用公用函数，如：
  `action: ${wmat.util.CartUtil.clear_cart}`

  关于自定义函数扩展详见 [扩展－自定义函数](#customization)

#### <a name="data"></a>Data

* data 是与action相配合的输入参数。大多数情况下data都可采用$DATA 来表示一个变量，用于在  scenario 和 test case 中输入。

  #### <a name="expectation"></a>Expectation

  Expectation 用于校验执行结果是否正确。

* 最简单的用法是直接判断一个字符串是否出现在UI上，如：
  `expectation: 该商品已售完！`  
  此时 WMAT 将会遍历UI上所有的 UIAStaticText （iOS）或者 <mark>(Android)</mark> 控件，只要有一个字符串相等即返回true

* expection 也可以指定去哪种控件类型里去搜寻，如：
  `expectation: 孙小美 | type=UIATextField`  
  此时 WMAT 将会遍历 UI 上所有的 UIATextField 去搜索该字符串，找到一个即返回 true。所以第一种用法也等价于 `expectation: 该商品已售完！ | type=UIAStaticText`

* 也可以指定定位一个控件来做严格的判断，如：
  `expectation: 孙小美 | element=//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]/UIATextField[1]`  
  同样，此时控件的定位方式与 `element` 元素的定位方式一样，也可支持3种类型的定位

* 支持模糊匹配模式，用`matching`属性表示。当 `matching=contains` 时，即为“包含”匹配模式。比如UI 上的文本为:  
```
 双11特大优惠，缤纷好礼送不停！
 小伙伴们快快加入~
```

此时以下校验将通过：

```
  expetation: 特大优惠，缤纷好礼 | matching=contains 
```

  缺省情况下为精确匹配模式，即校验值和实际值必须完全相等。

* 对element 指定属性的校验

比如某个element 具有属性 label, clickable，我们想校验它的clickable值是 true：

`expectation: true | element=element_id, attribute=clickable`

* expectation 支持用脚本表达式，此处作为扩展点，如：
  		`expectation: ${package.module.Class.function} `

  此处的function必须返回一个boolean值。

* expectation 可以支持多个检查点，此时需要用列表来表示：

```
expectation:
	- $value1 | element=element1
	- $value2 | element=element2
	- $value3 | element=element3
```

* 仅校验元素存在

有时候我们仅仅需要校验一个元素是否存在。此时采用关键字 $$IF_EXIST 即可，如果该元素未找到则该 case 失败。

```
expectation: $$IF_EXIST | element=//UIAApplication[1]/UIAWindow[1]/UIAScrollView[1]
```

* Toast 支持（Android only）

WMAT 支持 Android Toast 消息的校验，用法很简单，指定 `matching=toast` 即可。但是唯一要注意的地方是toast方式的expectation 不能单独出现，必须和action放在一起，如下：

```
click login button:
        element: login_btn_signin
        action: click
        step_desc: '下一步'
        expectation: 用户名或密码错误 | matching=toast
```

#### Desc

就是该Step的说明描述，可以不写。
 	   			
## <a name="scenario"></a>Scenario: 

Scenarios 是由 Page Steps 组合成的一个略复杂的业务操作序列. 就是“自动化用例”文档中的每个测试点（Item）。Scenario 里可以给 Page Step 指定输入参数。 
​	
example: `/scenarios/registerAndLogin/LoginScenarios.yml`

```
＃ 从‘我的帐户’页执行登录动作
login：	
	－ tabbar.MyAccount | enter_login_page
	－ tabbar.Login | input_username | $username
	－ tabbar.Login | input_password | $password
	－ tabbar.Login | login | $mobilephone
```

<mark>考虑在Scenarios里的数据也可以变量化，以便于将来批量导入测试数据和重复执行。</mark>
​	
​			
## <a name="test_case"></a>Test Case

Test cases 由 scenarios 组成完成实际的测试流程。可在这里指定输入参数。
​	
example: `/testcases/registerAndLogin/LoginTestCases.yml`

```
# 用帐户 eric 登录 －－ 成功 
testl_ogin_with_eric_account: 
    - registerAndLogin.LoginScenarios | login | username='eric', password='xxxxx', mobilephone='18634322411'
    - myAccount.AccountScenarios | logout

# 用qq号登录
test_login_by_qq: 
    - registerAndLogin.LoginScenarios | login_with_qq_number | qqnumber='273847162'
    - myAccount.AccountScenarios | logout

# 用微信号登录后还可以用qq登录
test_login_by_wechat_then_qq: 
    - registerAndLogin.LoginScenarios | login_with_wechat_number | wechatuser='michael'
    - registerAndLogin.LoginScenarios | login_with_qq_number | qqnumber='273847162', CAPS_DESC="'app': 'C:/Users/ehuan12/android/android.apk'"
    - myAccount.AccountScenarios | logout
```

## <a name="customization"></a>扩展－自定义函数

自定义函数建议放在与 pages 并列的 script 目录下，如：TestCase/GHS/Android_v1.5.5/script/demo_module.py

```
class DemoCustomClass:
    def run_action(self,case):
    	self.driver.find_element_by_xpath('//UIATabBar[1]/UIAButton[5]').click()
    	self.driver.find_element_by_xpath('//UIASearchBar[1]').send_keys('Sz')
    	cart = self.driver.find_element_by_xpath('//UIAButton[1]').get_attribute('name')
    	case.assertEqual(cart, CART_UI[1], '购物车显示异常')
    
    def check(self, case):
    	self.driver.find_element_by_accessibility_id('深圳市').click()
    	value=self.driver.find_element_by_xpath('//UIATableCell[1]/UIAStaticText[2]').get_attribute('name')
    	if value == '该手机号已存在'
    		return True
    	return False
```

对自定义函数，类和函数名没有限制，可以自由引用其他的库和调用自己写的其他函数。该函数的第一个入口参数 self 接收由框架构造的环境配置和上下文。  

* self.driver：当前连接的设备，最基础的工具，必须通过这个获取设备
* 当自定义函数用于expectation的操作时，必须返回 boolean 值
* 第二个入口参数case是一个unittest，可以直接在函数中做校验操作如：case.assertTrue(a==b), 该校验结果将被框架捕获并出现在报表中

函数定义好之后，可以直接在 page step 中引用：

```
input_username:
        element: txtUsername
        action: type
        data: 18026587555
        desc: 'input user name'

call_custom_function:
        action: ${demo_pkg.demo_module.DemoCustomClass.run_action}
        desc: '清空购物车'
```
以下的使用就和普通的 page step 完全一样了。

## <a name="webview_support"></a>WebView/Html 支持

在APP中有时会嵌入WebView，里面其实是一个html 页面，此时就成为一个混合应用（Hybrid）。

WMAT 支持 WebView 中 html 的校验。

首先 WMAT 中定义了两个特殊的 action，用于切换 native_app driver 和 webview driver：

```
switch_to_webview:
	action: switch_to_webview

switch_to_native:
	action: switch_to_native
```

在 webview 中的page step 操作是一样的，但是此时定义的Page Step必须加上一个后缀 _WEBVIEW 以示区分：

```
click_elec_card_WEBVIEW:
	element: //a[contains(text(), ’购买礼品卡’)
	action: click
	expection: $some_text
```
在组合到一个scenario 中的时候，必须记得换回native driver：

```
buy_elec_card:
	- common.Util | switch_to_webview
	- card.PresentCard | click_elec_card_WEBVIEW
	- ... # 其他操作
	- common.Util | switch_to_native
```

## <a name="internal_data_structure"></a>单个Test Case的中间JSON数据结构

```
[
  	{
  		"testcase_name": "login with eric's user",
  		"package_name": "registerAndLogin.Login",
     	"scenarios_suites": [
    		{
      			"scenarios_name": "wmat.scenarios.RegisterAndLogin.Register_MobileVerification_FirstDigit_Positive",
      			"page_steps": [
        		{"page": "tabbar.MyAccount", "element": "tablecellMyAccountLogin", "action": "click", "expectation": ["’登录‘ & ’注册‘"], "desc": "进入登录页"},
        		{"page": "tabbar.Login", "element": "txtfieldUserName", "action": "click", "data": "1861234123", "expectation": "", "desc": "输入用户名"},
        		{"page": "tabbar.Login", "element": "sectxtfieldPassword", "action": "type", "data": "’stoneman‘ || ’18611578049‘", "expectation": "", "desc": "登录"},
        		{"page": "tabbar.Login", "element": "btnLogin", "action": "click", "data": 12345678, "expectation": "btnLogin", "desc": "input Password"},
        		{"page": "tabbar.Login", "element": "txtfieldUserName", "action": "type", "data": "1861234123", "expectation": nil, "desc": "输入用户名", "runtimes": "10"},
        		{"page": "tabbar.Login", "": "btnClose", "action": "click", "expectation": "[${tabbar.Login.funcName}]", "desc": "close coupon popup window(optional)"}
        	},
    		{
      			"scenarios_name": "${wmat.scenarios.myCustomClass.method}",
    		}
  		]
  	}
]
```

## <a name="naming_convention"></a>Test Case的package组织结构及命名规则

### Page：

以 pages 开头，依据 QA 提供的8类70个页面，按类别分，如：

账号类页面在 account 包

* 登录页： account.Login  
  它对应 qa/pages/account/Login.yml 文件

* 忘记密码页：account.ForgotPassword
  它对应 qa/pages/account/ForgotPassword.yml 文件

订单类页面在 order 包

* 订单列表页：order.OrderList
  它对应 qa/pages/order/OrderList.yml 文件

### Scenario:

以 scenarios 开头，依据 QA 提供的测试用例文件的分类，如：

* 注册登录类：scenarios.RegisterAndLogin  
  其中定义了一系列属于注册登录的场景，它对应 qa/scenarios/RegisterAndLogin.yml

### Test Case:

以 testcases 开头，具体case名称视具体情况定，如：

* wmat.testcases.Coupon
  可能包含了所有优惠活动相关的case，位于 qa/testcase/Coupon.yml







```

```

```

```

```

```