import time
time.sleep(120)
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
from plyer import notification


def messenger():
    try:
        url ="https://web.whatsapp.com/send?phone=+91xxxxxxxxxx"
        message_content = "Good morning!"
        path = r"<your chrome driver path>"
        options = webdriver.ChromeOptions()
        options.add_argument("user-data-dir=<Your_browser_user_profile>")
        driver = webdriver.Chrome(executable_path=path, options=options)
        driver.minimize_window()
        driver.get(url)
        time.sleep(20)
        type_it = driver.find_elements_by_class_name('_13NKt')
        time.sleep(20)
        try:
            type_it[1].send_keys(message_content + Keys.ENTER)
        except IndexError as e:
            time.sleep(20) 
            type_it = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
            type_it.send_keys(message_content+ Keys.ENTER)

           
            print(e)
        time.sleep(10)
        driver.quit()
    except Exception as e:
        notification.notify(
            title = "Whatsapp message not sent",
            message = "Error while sending!",
            app_icon = r"<Your icon file>",
            app_name = "Whatsapp Message error",
            toast = True,
              )
        print(e)
        os._exit(0)
# reading from the data
if __name__ == "__main__":
    today = str(datetime.date.today())
    today_2 = f"{today} "
    content = bytes(today_2,'utf-8')
    year_str = str(datetime.datetime.now().year)
    year_edit = bytes(year_str,'utf-8').decode('utf-8')
    date_str = str(datetime.datetime.now().day)
    date_edit = bytes(date_str,'utf-8').decode('utf-8')
    edit = {"1":"01",
            "2":"02",
            "2":"03",
            "4":"04",
            "5":"05",
            "6":"06",
            "7":"07",
            "8":"08",
            "9":"09",}
    print(date_edit)
    try:
        file = open("database.txt", "x")
        messenger()
        file.write(today_2)
        file.close()
    except Exception as e:
        file = open("database.txt", "a+b")
        try:
            try:
                file.seek(-11,2) # seek will not work in negative in text mode, only in byte mode
            except OSError as e:
                print(e)
                messenger()
                file.write(content)
                file.close()
                os._exit(0)
            year = file.read(10).decode('utf-8')
            file.seek(-11,2)
            date = file.read(10).decode('utf-8')
            if year_edit != year[:4]:
                file.close()
                file = open("database.txt", "wb")
                file.close()
                file = open("database.txt", "a+b")
                messenger()
                file.write(content)
                file.close()
            for x in edit.keys():
                if x == date_edit:
                    date_edit = edit.get(x)
                    break
            if date_edit != date[8:14]:
                messenger()
                file.write(content)
                file.close()
                os._exit(0)
        except Exception as e:
            print(e)