# [对象定位](http://www.selenium.org.cn/1562.html)

通过id、name、class name、link text、partial link text、tag  name、xpath、css selector一系列方法可以获得对象定位。

```html
<input type="text" class="s_ipt" name="wd" id="kw" maxlength="100" autocomplete="off">
```

这是百度的搜索栏的html

```python
#coding=utf-8
from selenium import webdriver
import time

browser = webdriver.Firefox()


browser.get("http://www.baidu.com")
time.sleep(2)
#通过id方式定位
browser.find_element_by_id("kw").send_keys("selenium")
#通过name方式定位
browser.find_element_by_name("wd").send_keys("selenium")
#通过tag name方式定位
browser.find_element_by_tag_name("input").send_keys("selenium")
#通过class name 方式定
browser.find_element_by_class_name("s_ipt").send_keys("selenium")
#通过CSS方式定位
browser.find_element_by_css_selector("#kw").send_keys("selenium")
#通过xphan方式定位
browser.find_element_by_xpath("//input[@id='kw']").send_keys("selenium")

browser.find_element_by_id("su").click()
time.sleep(3)
browser.quit()
```

再来看下面一组控件属性：

```html
<th width="95"></th><th width="">文件名</th><th class="c1">创建时间</th><th class="c1">状态</th><th class="c1">文件大小</th><th class="c1">时长</th>
```

需要用到xpath或css selector方法

## CSS定位

> CSS(Cascading Style Sheets)是一种语言，它被用来描述HTML和[XML](https://zh.wikipedia.org/wiki/XML)文档的表现。CSS使用选择器来为页面元素绑定属性。这些选择器可以被selenium用作另外的定位策略。

