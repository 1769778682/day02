# 6.打印登陆后页面标题和地址信息

# 导包
import time

from selenium import webdriver

# 打开浏览器
driver = webdriver.Chrome()
# 进入待测网页
driver.get("http://localhost/")
# 1.使用css定位定位tpshop首页登陆超链接，并执行点击
driver.find_element_by_css_selector("[href='/Home/user/login.html']").click()
# 2.使用id定位定位登陆页面用户名输入框，输入用户名
ele_username = driver.find_element_by_id("username")
ele_username.clear()
ele_username.send_keys("13812345678")
# 3.使用name定位定位登陆页面密码输入框，输入密码
ele_password = driver.find_element_by_name("password")
ele_password.send_keys("123456")
# 4.使用class定位定位登陆页面验证码输入框，输入验证码
ele_verify_code = driver.find_element_by_id("verify_code")
ele_verify_code.send_keys(8888)
# 5.使用xpath定位登陆按钮执行点击
ele_button = driver.find_element_by_xpath("//div[@class='login_bnt']/a")
ele_button.click()
time.sleep(2)
# driver.quit()