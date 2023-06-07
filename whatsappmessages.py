from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import schedule
import time

#Replace with the path to your Chrome driver executable
driver_path = '/path/to/chromedriver'

#Replace with the name of the contact/group you want to send the message to
target = "babe"

#Edit message to be sent
message = "Good morning."

def send_whatsapp_message():
    #Open Chrome
    driver = webdriver.Chrome(driver_path)
    driver.get('https://web.whatsapp.com')

    input('Press Enter after scanning QR code and logging in to WhatsApp Web...')

    search_input = driver.find_element_by_xpath('//div[contains(@class, "copyable-text")]')
    search_input.click()
    search_input.send_keys(target)
    search_input.send_keys(Keys.ENTER)

    time.sleep(3)

    message_input = driver.find_element_by_xpath('//div[@class="_3uMse"][@contenteditable="true"]')
    message_input.click()
    message_input.send_keys(message)
    message_input.send_keys(Keys.ENTER)

    time.sleep(2)

    driver.quit()

#Schedule the task to run every day at the specified time
schedule.every().day.at("06:00").do(send_whatsapp_message)

#continuously execute the scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)
