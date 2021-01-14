# WebUI自动化框架V1.0        开发者：信息安全部-scot

## 项目说明
- 本框架是基于关键字驱动结合Excel数据驱动设计的一套UI自动化框架，适用于FSWeb商城前台和后台ERP系统等，  
在Excel用例中特别添加了断言结果颜色标记，让测试结果一目了然！

## 环境部署
- 可通过git clone url直接拉取项目文件
- 可直接使用项目文件中的venv虚拟环境，若虚拟环境无法使用，可尝试新增虚拟环境
- 验证环境是否配置成功：选择项目根路径下的run.py运行，观察是否可以运行，控制台是否有日志导出，查看logs  
下是否生成最新的日志文件

## 项目结构说明
- Chromeoptions =======> google浏览器设置
- Driver_execute =======> Excel文件读取方法
- FSkeys =======> 关键字类
- Logs =======> 日志类及.log存放位置
- Report =======> 测试报告方法及存放位置
- Testcase =======> DATA测试用例文件存放位置
- run.py =======> 测试用例执行器，填写对应用例集路径即可执行
- README.md =======> 项目说明文档

## Excel字段说明
- 编号：为用例操作编号自增
- 事件：为关键字方法，关键字方法说明  
-- open：访问url  
-- close：关闭当前标签页，当只有一个页面是关闭浏览器  
-- quit：退出浏览器  
-- locator：定位  
-- input：输入  
-- click：点击事件  
-- suspend：悬浮操作（鼠标悬浮）  
-- assert_text：文本断言校验  
-- wait：强制等待  
-- assert_wait：显示等待（也可当做断言校验）  
-- switch_close：关闭当前标签页，切换句柄  
-- switch_to：不关闭标签页，切换句柄  
-- switch_old：切换回上一次标签页句柄  
-- assert_att：基于元素属性断言校验  
- 定位方法：元素定位方法id、name、xpath、link text、partial link text、css selector、class name、tag name  
- 元素路径：根据定位方法匹配，可通过copy xpath
- 输入内容：第一行为初始化的浏览器，其他为input或wait参数
- 描述：操作描述
- 预期结果：当需要断言时，添加对照文本或属性
- 实际结果：断言完毕后，程序自动填写Pass或False

## V1.1版本优化
- Report模块增加邮件发送HTMLTestRunner测试报告等
- 更多后续...POM设计模式、多线程等方向
