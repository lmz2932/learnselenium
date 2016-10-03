from sm import ff, auto_close
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@auto_close
def func():
    try:
        a = WebDriverWait(ff, 3).until(
            EC.presence_of_element_located((By.TAG_NAME, "a")))
        a.click()
    except TimeoutException:
        print "No such element"
