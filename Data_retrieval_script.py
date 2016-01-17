from selenium import webdriver
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import csv



followers_list = []
login = 'JojoFdvmzzbo'
password = '18403787'


driver = webdriver.Chrome()
driver.maximize_window()


# logging_in function describes the authorization mechanism

def logging_in(login, password):
	
    email_form = driver.find_element_by_xpath("/html//div[@class='front-card']//div[@class='username field']/input[@id='signin-email']")
    email_form.send_keys(login)
    password_form = driver.find_element_by_xpath("/html//div[@class='password flex-table-form']/input[@id='signin-password']")
    password_form.send_keys(password)
    send_button = driver.find_element_by_xpath("/html//button[@class='submit btn primary-btn flex-table-btn js-submit']").click()
    
 
driver.get('https://twitter.com')

logging_in(login, password)

interesting_page_followers_url = ('https://twitter.com/50cent/followers')

driver.get(interesting_page_followers_url)

while len(followers_list) < 300:

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    followers_list = driver.find_elements_by_xpath("/html//a[@class='ProfileNameTruncated-link u-textInheritColor js-nav js-action-profile-name']")
    print(len(followers_list))

follow_buttons = driver.find_elements_by_xpath("//span[@class='button-text follow-text']")
users_links = driver.find_elements_by_xpath("/html//span[@class='u-linkComplex-target']")

driver.find_element_by_xpath("/html//h1[@class='Icon Icon--bird bird-topbar-etched']").click()  # return to top of the page


#for follow in follow_buttons:
#    if follow.text != 'Following':
#        try:
#            follow.click()
#        except (ElementNotVisibleException, WebDriverException) as multiple_exceptions:
#            print('Object was not founded on the page') 

popular_page_name  = (users_links[0].text)

def table_output(followers_list, users_links, popular_page_name):

    print('table printing')
    with open('{}.csv'.format(popular_page_name), 'w', encoding='utf8') as table:
        csvwriter = csv.writer(table, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        
        for item in zip([follower.text for follower in followers_list], [user.text for user in users_links[1:]]):
            csvwriter.writerow(item)

table_output(followers_list, users_links, popular_page_name)    
    


