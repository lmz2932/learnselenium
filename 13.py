from sm import ff, auto_close
from selenium.common.exceptions import NoSuchElementException


@auto_close
def func():
    ff.implicitly_wait(3)
    try:
        a = ff.find_element_by_partial_link_text('g')
        a.click()
    except NoSuchElementException:
        print "Page load fail or no such element"
