import base64
import time
from selenium import webdriver

def reply(wd, message, channel):
    chat = wd.find_element_by_xpath('//span[@title="{}"]'.format(channel))
    time.sleep(5)
    chat.click()
    time.sleep(1)
    inputbox = wd.find_element_by_xpath("//div[@contenteditable='true']")
    inputbox.click()
    inputbox.send_keys(message)
    send = wd.find_element_by_xpath("//span[@data-icon='send']")
    send.click()

def fetch_new_messages(wd, last_message, channel):
    chat = wd.find_element_by_xpath('//span[@title="{}"]'.format(channel))
    time.sleep(5)
    chat.click()
    time.sleep(1)
    messages = wd.find_elements_by_css_selector('.message-in, .message-out')
    print(len(messages))

def init():
    wd = webdriver.Remote(command_executor="http://localhost:4444/wd/hub", desired_capabilities=webdriver.DesiredCapabilities.CHROME)
    wd.get('https://web.whatsapp.com')
    time.sleep(10)
    return wd

def prepare_env(wd):
    currb64 = ''
    while True:
        try:
            qr = wd.find_element_by_xpath("//img[contains(@alt, 'Scan me!')]")
            src = qr.get_attribute('src')
            b64 = src[src.find('base64,') + len('base64,'):]
            if b64 != currb64:
                with open('qrcode.png', 'wb') as f:
                    f.write(base64.b64decode(b64))
                currb64 = b64
                print('QRCode loaded. Scan it to proceed.')
                time.sleep(5)
        except Exception as e:
            print("Probably Authenticated")
            time.sleep(5)
            break

if __name__ == '__main__':
    wd = init()
    prepare_env(wd)
    fetch_new_messages(wd, '', 'Warehouse')
