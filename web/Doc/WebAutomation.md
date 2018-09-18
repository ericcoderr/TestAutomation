<center><H1> WMAT Web Automation definition </H1>v0.1</center>
## 目录
语言Python3.5  ,服务端和客户端Linux,只做Chrome浏览器的自动化测试

* [环境准备](#env_pre)
    * [自动化测试环境](#auto_env)
    * [OMS环境](#OMS_env)
    * [持续集成环境](#jenkins_env)
* [Test Case编写](#Test_Case)
    * [工程目录说明](#project_directory)
    * [Firefox slenium插件导出Test Case修改说明](#selenium_ide)
    * [编写TestCase事项](#edit_testcase)

## 正文
### <a name="env_pre"></a>环境准备
* <a name="auto_env"></a>自动化测试环境

        1.录脚本环境：Firefox_52.0.2.6291,并通过Firefox插件管理安装selenium IDE插件。这步工作因为内网环境没办法安装selenium，所以只能在外网录制，在内网修改，QA也可以直接在内网写脚本

        2.在Linux Selenium server:
            a. 安装PHANTOMJS:http://phantomjs.org/download.html，下载解压，并把phantomjs-2.1.1-linux-x86_64/bin目录配置到Path下，也可以把phantomjs-2.1.1-linux-x86_64/bin/phantomjs 放到/usr/sbin/下面(此处需要有权限访问)。
            <mark>Download phantomjs-2.1.1-linux-x86_64.tar.bz2 (22.3 MB) and extract the content.
			Note: For this static build, the binary is self-contained. There is no requirement to install Qt, WebKit, or any other libraries. It however still relies on Fontconfig (the package fontconfig or libfontconfig, depending on the distribution). The system must have GLIBCXX_3.4.9 and GLIBC_2.7
			</mark>
            b.下载selenium-server-standalone-3.3.1.jar ， 启动 java -jar /home/root1/Downloads/selenium-server-standalone-3.3.1.jar
            c. 从SVN下载框架代码，主要包含两个目录wmart_web 和TestCase目录。
            e. 运行bootstrap : e.g : E:\TestAutomation\web\wmart_web\src>python bootstrap.py --config e:/config.ini
        3.QA内网开发环境搭建
            a.从svn 下载 自动化测试框架代码，包含bin和wmart_web目录，两个必须放在同一级。
            b.安装chrome浏览器
            c.安装python2.7.5
            d.运行wm_web目录下的bootstrap.py，如果是在IDE里运行，可以加启动参数 --config template/config.ini ,template 是项目名称，不用修改bootstrap.py
        <mark>
                1.安装python selenium 插件，pip install -U selenium  [此文件已提交到框架里面不需要在安装]
                2.数据库访问，需要安装pymssql ,已集成到框架里，在wm_web目录下，此处要注意机器的python是32位还是64位的，公司默认安装32位的，所以可以直接使用。如果是64位，请把wm_web\64\下的文件的替换掉wm_web下的。
                3.数据库密码存放，参考db.python,先调用base64_encode()加密，然后在setUp里解密，已达到密码明文不落地。
        </mark>


* <a name="oms_env"></a>OMS环境
开发环境：oms dj外网开发环境，QA 环境：oms dj 内网QA 环境
* <a name="jenkins_env"></a>持续集成环境


###<a name="Test_Case"></a>Test Case编写
* <a name="project_directory"></a>工程目录说明
####web
    Doc
    Temp
    TestCase  TestCase Demo 目录
    wm_web 框架代码目录
    bin 二进制文件，chromedriver.cmd
    report
    download
    在部署环境时Temp和Doc目录不需要，其他目录必须保持跟以上目录一致，QA写的Case必须放到TestCase目录下，并且根据项目区分，下面必须有本项目的config.ini

* <a name="selenium_ide"></a>Firefox slenium插件导出Test Case修改说明

* <a name="edit_testcase"></a>编写TestCase事项
    参考web\TestCase\template\login.py

        1.可以基于Firefox Selenium IDE 插件录制脚本，脚本需要修改 用bootstrap的setUp覆写导出脚本里setUp方法，QA 写的TestCase不需要写setUp。

        2.TestCase根目录以及子目录下面必须要加空的__init__.py文件，只限于要执行的TestCase目录,注意TestCase目录只是一个示例，此目录是用来管理TestCase的目录，可以自定义，一般建议项目名加版本号 ,这个地方如果不同环境跑不同case,只需要按目录区分就行，在不同环境运行时指定相应的目录就行。e.g: OMS/V1.0/。

        3.运行 bootstrap 时需要加参数  bootstrap 后面必须要指定config_path相对路径 ，这个config.ini 文件里的内容参考template的config.ini，文件名或目录可以根据环境区分，路径也可以自己定义。 e.g --config template/config.ini


        如果在IDE里运行，可以指定启动参数 --config ,也可以通过命令行参数  python --config ./config.ini

            bootstrap后面的可选参数，命令行参数会覆盖config.ini的参数。

            --server-env ： 如果server模式 ，这个 参数 --server-env server
            --case-path： case目录,这个地方必须是相对目录，并且根目录必须是TestCase
            --case-pattern：运行case的正则表达式 e.g test*
            --desc-sys： 目标系统，用来生成报表目录的 e.g : oms
            --remote-host: server模式 host
            --desc-host:目标系统host

            e.g: template 项目的运行bat脚本
            python ../../wm_web/src/bootstrap.py --config template/config.ini


-------------------------------------------以下非框架相关---------------
　　一些Chrome的地址栏命令（这些命令会不停的变动，所有不一定都是好用的）
　　在Chrome的浏览器地址栏中输入以下命令，就会返回相应的结果。这些命令包括查看内存状态，浏览器状态，网络状态，DNS服务器状态，插件缓存等等。
　　about:version - 显示当前版本
　　about:memory - 显示本机浏览器内存使用状况
　　about:plugins - 显示已安装插件
　　about:histograms - 显示历史记录
　　about:dns - 显示DNS状态
　　about:cache - 显示缓存页面
　　about:gpu -是否有硬件加速
　　about:flags -开启一些插件 //使用后弹出这么些东西：“请小心，这些实验可能有风险”，不知会不会搞乱俺的配置啊！
　　chrome://extensions/ - 查看已经安装的扩展
　　其他的一些关于Chrome的实用参数及简要的中文说明（使用方法同上，当然也可以在shell中使用）
　　–user-data-dir=”[PATH]” 指定用户文件夹User Data路径，可以把书签这样的用户数据保存在系统分区以外的分区。
　　–disk-cache-dir=”[PATH]“ 指定缓存Cache路径
　　–disk-cache-size= 指定Cache大小，单位Byte
　　–first run 重置到初始状态，第一次运行
　　–incognito 隐身模式启动
　　–disable-javascript 禁用Javascript
　　--omnibox-popup-count="num" 将地址栏弹出的提示菜单数量改为num个。我都改为15个了。
　　--user-agent="xxxxxxxx" 修改HTTP请求头部的Agent字符串，可以通过about:version页面查看修改效果
　　--disable-plugins 禁止加载所有插件，可以增加速度。可以通过about:plugins页面查看效果
　　--disable-javascript 禁用JavaScript，如果觉得速度慢在加上这个
　　--disable-java 禁用java
　　--start-maximized 启动就最大化
　　--no-sandbox 取消沙盒模式
　　--single-process 单进程运行
　　--process-per-tab 每个标签使用单独进程
　　--process-per-site 每个站点使用单独进程
　　--in-process-plugins 插件不启用单独进程
　　--disable-popup-blocking 禁用弹出拦截
　　--disable-plugins 禁用插件
　　--disable-images 禁用图像
　　--incognito 启动进入隐身模式
　　--enable-udd-profiles 启用账户切换菜单
　　--proxy-pac-url 使用pac代理 [via 1/2]
　　--lang=zh-CN 设置语言为简体中文
　　--disk-cache-dir 自定义缓存目录
　　--disk-cache-size 自定义缓存最大值（单位byte）
　　--media-cache-size 自定义多媒体缓存最大值（单位byte）
　　--bookmark-menu 在工具 栏增加一个书签按钮
　　--enable-sync 启用书签同步


selenium ide命令
操作类型——Action
浏览器操作
open(https://www.sogou.com/)  打开url。
goBack()  无参数，后退。
refresh()  无参数，刷新。
windowFocus()  无参数，激活选中的浏览器窗口。
windowMaximize()  无参数，使浏览器窗口最大化。
close() 无参数，关闭。
type("locator","value") 在input表达输入值。  
typeKeys("locator","value")  模拟键盘敲击，输入字符。
click("locator")  单击，最后后面使用waitForPageToLoad（）命令。
clickAt("locator","coordstring") 单击，需要提供想的坐标。
doubleClick("locator")  双击。
doubleClickAt("locator","coordstring") 双击。
select("locator")  在下拉框中选择选项。
selectWindow("windowID") 选取窗口，如果参数为null，则选择旧弹窗
selectPopUp（"windowID"）  无参数，表示选择弹出窗口；参数可以是新窗口的名字、标题。。
check("locator")  勾选复选框或单选框。
uncheck("locator")  取消勾选。
focus("locator")  定位焦点。
setTimeout（"timeout/ms"）等待超时时间。
setSpeed("time/ms")  测试执行速度。
pause（""time/ms" )  暂停时间。
break（）无参数，暂停当前测试，除非手动继续。
captureEntirePageScreenshot("filename")  截图并保存为PNG文件。需要指明路径和文件后缀。
highlight（"locator"）将元素背景色改为黄色。
echo（"massage"）  打印静态信息。
echo ${a}   打印动态变量的值。
　　存储类型——Accessor  检查应用程序的状态，并将结果存入变量。 其中locate为定位元素。如name=wd
store（"值"，“variableName”）将值存入变量。  打印出该值，echo ${变量}　　　　
storeTitle（"title"）将当前网页标题存入变量title。   echo ${title}　　　　
storeLocation（"url"）将网页URL存入变量。  echo ${url}　　　　
storeValue（"locate"，"variableName"）将input元素存入变量。echo ${变量}　　　　
storeEditable（"locate","variableName"）将input元素的可编辑状态存入变量。可编辑返回true。echo ${变量}　　　　
storeText（"locate","variableName"）将元素的文本值存入变量。echo ${变量}　　　　
storeChecked（"locate","variableName"）将选框的勾选状态存入变量。已勾选返回true。echo ${变量}　　　　
storeSelectedIndex（"locate","variableName"）将下列列表中index存入变量。echo ${变量}　　　　
storeSelectedLable("locate","variableName")　　　　
storeSelectedValue("locate","variableName")　　　　
storeSelectedOptions("locate","variableName")
storeTable("locate","variableName")　　　　
storeAttibute("locate","variableName")　　　　
storeTextPresent("locate","variableName")　　　　
storeElementPresent("locate","variableName")将元素存在页面中是否存入变量。　　　　
storeVisible("locate","variableName")将元素的可见性存入变量。　　　　
storeSpeed("variableName") 将执行速度存入变量。　　
断言类型——Assertion 验证某个命题是否为真。网页标题、URL、input元素值、
assertTitle("预期值")验证网页的标题是否等于预期值。
assertNoTitle("预期值")验证网页的标题是否不等于预期值。
verifyTitle("预期值")         同assertTitle功能一样
verifyNotTitle("预期值")   同assertNotTitle功能一样
waitForTitle("预期值")      等待当前网页标题并进行验证是否等于预期值
waitForNotTitle("预期值")等待当前网页标题并进行验证是否不等于预期值
assertLacation("url")        验证网页的URl是否等于预期值
assertNotLocation（"url"）验证网页的URl是否不等于预期值
verifyLocation("url")
verifyNotLocation("url")
waitForLocation("url")
waitForNotLocation("url")
assertValue("locate","预期值")验证input元素的值是否等于预期值
assertNotValue("locate","预期值")
verifyValue("locate","预期值")
verifyNotValue("locate","预期值")
waitForValue("locate","预期值")
waitForNotValue("locate","预期值")
assertEditable()
assertText("locate","预期值")验证某个元素的文本值是否等于预期值。
assertNotText("locate","预期值")
verifyText("locate","预期值")
verifyNotText("locate","预期值")
waiForText("locate","预期值")
waitForNotText("locate","预期值")
assertChecked()

