# 要求使用元素定位另外一种写法：driver.find_element(By.XXX,value)
# 导包
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("http://localhost/")
# 1.使用xpath的文本形式定位tpshop首页注册超链接，并点击
driver.find_element(By.XPATH, "//div[@class='fl nologin']/a[2]").click()
# 2.使用css属性定位策略定位手机号码输入框，输入手机号码
ele_username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
ele_username.clear()
ele_username.send_keys("13800001234")
# 3.使用css属性包含的方式定位验证码输入框，输入验证码
ele_verify_code = driver.find_element(By.CSS_SELECTOR, "[placeholder*='验证码']")
ele_verify_code.send_keys("8888")
# 4.使用xpath属性与逻辑结合定位方式定位密码输入框，输入设置密码
ele_password = driver.find_element(By.XPATH, "//input[@name='password']")
ele_password.send_keys("123456")
# 5.使用xpath路径定位策略定位确认密码，输入确认密码
ele_password2 = driver.find_element(By.XPATH, "//input[@name='password2']")
ele_password2.send_keys("123456")
# 6.使用超链接定位方式定位同意协议并注册按钮，并点击
ele_click = driver.find_element_by_partial_link_text("同意协议").click()
