# 导包
import time
from selenium import webdriver

# 创建浏览器驱动对象
driver = webdriver.Chrome()
# 打开待测地址
driver.get("file:///C:/Users/sandysong"
           "/Desktop/pagetest/%E6%B3%A8%E5%86%8CA.html")
time.sleep(2)
# 业务操作
# 使用css定位方式中id选择器使用
driver.find_element_by_css_selector("#userA").send_keys("admin")
# 使用css定位方式中属性选择器使用
driver.find_element_by_css_selector("[placeholder='请输入电话号码']").send_keys("123456")
# 使用css定位方式中class选择器定位
driver.find_element_by_css_selector(".telA").send_keys("13812345678")
# 使用css定位方式中的元素选择器
driver.find_element_by_css_selector("button").click()
# 3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()