# Logging


* 代码里的日志统一使用 Python 的 Logging 模块，不能用 print 
* 出错使用logging.error, 无论是出错还是fail，都需要进行屏幕截图。
* 出错时需要log出当前的test case，scenario，page 和step
* 在测试用例执行过程中，需要log：
	* 每一个Test Case进入和完成，调用的参数等
	* 每一个Scenario 进入和完成，调用的参数等
	* 每一个Page Step 进入和完成，输入的参数等 

# Report

HTMLTestRunner: [https://pypi.python.org/pypi/HTMLTestRunner](https://pypi.python.org/pypi/HTMLTestRunner)

* 对中文的支持
* 移植到3.x
* 研究TestResult对象是否还能输入更多的内容，然后考虑定制report
	* report里显示scenario，pages信息，特别是出错log中
	* 错误信息加入屏幕截图
	* 按照模块分类，拆分文件，而不是所有结果放一个文件，否则将来太大

# 编码规范

参照标准的 python 编码规范
[http://www.cnblogs.com/morya/archive/2011/09/20/2182883.html](http://www.cnblogs.com/morya/archive/2011/09/20/2182883.html)  

* indent: 4个空格
* 每行最大长度：90个字符
* 注释：
	* 单行注释：

	`x = x+1  # Compensate for border`

	* 文档化注释： 
	
	```
	"""	Return a foobang
	Optional plotz says to frobnicate the bizbaz first.
       """
	```          
* 类名：ClassName
* 函数名：func_name
* 变量：product_price
* 全局变量：DEFAULT_TITLE = 'Unit Test Report'

