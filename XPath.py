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
# 绝对路径
# driver.find_element_by_xpath("/html/body/div/fieldset/form/p[1]/input").send_keys("admin")
# 相对路径
driver.find_element_by_xpath("//form/p[1]/input").send_keys("admin")
# 利用元素属性
driver.find_element_by_xpath("//input[@placeholder='请输入密码']").send_keys("123456")
# 属性与逻辑结合
driver.find_element_by_xpath("//*[@name='telA' and @class='telA']").send_keys("13812345678")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='pa']/input").clear()
# 层级与属性结合
driver.find_element_by_xpath("//*[@id='pa']/input").send_keys("lel_kk")
# 扩展
# --使用属性包含的形式定位用户名输入框，并输入：admin，暂停两秒
driver.find_element_by_xpath("//*[contains(@placeholder, '号码')]").clear()
driver.find_element_by_xpath("//*[contains(@placeholder, '号码')]").send_keys("13812312312")
# --
# 3秒后关闭浏览器窗口
time.sleep(3)
driver.quit()