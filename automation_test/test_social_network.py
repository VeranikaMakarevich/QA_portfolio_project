import unittest
import automation_test.helpersSN as h
import requests


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException as WDE
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service



class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        '''we can use Selenium Headless option

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        '''

        self.driver.maximize_window()

    def test_chrome_common(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # API testing from Selenium
        print("California Marketing Url has", requests.get(h.url).status_code, "as status Code")
        code = requests.get(h.url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        h.delay()

        # verify website title
        try:
            assert driver.title == h.cm_title
            print("Title is Correct. Current Title is:", driver.title)
        except WDE:
            print("Title is different. Current Title is:", driver.title)

        # check some elements of header
        wait.until(EC.visibility_of_element_located((By.XPATH, h.X_head)))
        driver.find_element(By.XPATH, h.img_l).is_displayed()
        driver.find_element(By.XPATH, h.nw).is_displayed()

        driver.close()

    def test_chrome_Link1(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L1).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L1)))
        print('The First link is displayed and clickable')

        h.delay()

        # verify which social network is in the first link

        driver.find_element(By.XPATH, h.L1).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("first_link.png")
        print("Title of the first link in social network menu is", driver.title)
        print("Url of the first link in social network menu is", driver.current_url)

        # determine what is the social network

        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ('Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn')

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_chrome_Link2(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L2).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L2)))
        print('The Second link is displayed and clickable')

        h.delay()

        # verify which social network is in the second link

        driver.find_element(By.XPATH, h.L2).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("second_link.png")
        print("Title of the second link in social network menu is", driver.title)
        print("Url of the second link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_chrome_Link3(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L3).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L3)))
        print('The Third link is displayed and clickable')

        h.delay()

        # verify which social network is in the third link

        driver.find_element(By.XPATH, h.L3).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("third_link.png")
        print("Title of the third link in social network menu is", driver.title)
        print("Url of the third link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_chrome_Link4(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L4).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L4)))
        print('The Fourth link is displayed and clickable')

        h.delay()

        # verify which social network is in the fourth link

        driver.find_element(By.XPATH, h.L4).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("fourth_link.png")
        print("Title of the fourth link in social network menu is", driver.title)
        print("Url of the fourth link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_chrome_Link5(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L5).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L5)))
        print('The Fifth link is displayed and clickable')

        h.delay()

        # verify which social network is in the Fifth link

        driver.find_element(By.XPATH, h.L5).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("fifth_link.png")
        print("Title of the fifth link in social network menu is", driver.title)
        print("Url of the fifth link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_chrome_Link6(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L6).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L6)))
        print('The Sixth link is displayed and clickable')

        h.delay()

        # verify which social network is in the Sixth link

        driver.find_element(By.XPATH, h.L6).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("sixth_link.png")
        print("Title of the sixth link in social network menu is", driver.title)
        print("Url of the sixth link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_chrome_Link7(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L7).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L7)))
        print('The Seventh link is displayed and clickable')

        h.delay()

        # verify which social network is in the seventh link

        driver.find_element(By.XPATH, h.L7).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("seventh_link.png")
        print("Title of the seventh link in social network menu is", driver.title)
        print("Url of the seventh link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    # closing the browser
    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        '''we can use Selenium Headless option

        options = webdriver.EdgeOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=options)

        '''

        self.driver.maximize_window()

    def test_edge_common(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # API testing from Selenium
        print("California Marketing Url has", requests.get(h.url).status_code, "as status Code")
        code = requests.get(h.url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        h.delay()

        # verify website title
        try:
            assert driver.title == h.cm_title
            print("Title is Correct. Current Title is:", driver.title)
        except WDE:
            print("Title is different. Current Title is:", driver.title)

        # check some elements of header
        wait.until(EC.visibility_of_element_located((By.XPATH, h.X_head)))
        driver.find_element(By.XPATH, h.img_l).is_displayed()
        driver.find_element(By.XPATH, h.nw).is_displayed()

        driver.close()

    def test_edge_Link1(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L1).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L1)))
        print('The First link is displayed and clickable')

        h.delay()

        # verify which social network is in the first link

        driver.find_element(By.XPATH, h.L1).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("first_link.png")
        print("Title of the first link in social network menu is", driver.title)
        print("Url of the first link in social network menu is", driver.current_url)

        # determine what is the social network

        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ('Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn')

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_edge_Link2(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L2).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L2)))
        print('The Second link is displayed and clickable')

        h.delay()

        # verify which social network is in the second link

        driver.find_element(By.XPATH, h.L2).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("second_link.png")
        print("Title of the second link in social network menu is", driver.title)
        print("Url of the second link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_edge_Link3(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L3).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L3)))
        print('The Third link is displayed and clickable')

        h.delay()

        # verify which social network is in the third link

        driver.find_element(By.XPATH, h.L3).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("third_link.png")
        print("Title of the third link in social network menu is", driver.title)
        print("Url of the third link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_edge_Link4(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L4).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L4)))
        print('The Fourth link is displayed and clickable')

        h.delay()

        # verify which social network is in the fourth link

        driver.find_element(By.XPATH, h.L4).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("fourth_link.png")
        print("Title of the fourth link in social network menu is", driver.title)
        print("Url of the fourth link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_edge_Link5(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L5).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L5)))
        print('The Fifth link is displayed and clickable')

        h.delay()

        # verify which social network is in the Fifth link

        driver.find_element(By.XPATH, h.L5).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("fifth_link.png")
        print("Title of the fifth link in social network menu is", driver.title)
        print("Url of the fifth link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_edge_Link6(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L6).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L6)))
        print('The Sixth link is displayed and clickable')

        h.delay()

        # verify which social network is in the Sixth link

        driver.find_element(By.XPATH, h.L6).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("sixth_link.png")
        print("Title of the sixth link in social network menu is", driver.title)
        print("Url of the sixth link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_edge_Link7(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L7).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L7)))
        print('The Seventh link is displayed and clickable')

        h.delay()

        # verify which social network is in the seventh link

        driver.find_element(By.XPATH, h.L7).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("seventh_link.png")
        print("Title of the seventh link in social network menu is", driver.title)
        print("Url of the seventh link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    # closing the browser
    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        '''we can use Selenium Headless option

        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

        '''

        self.driver.maximize_window()

    def test_firefox_common(self):
        driver = self.driver
        wait = WebDriverWait(driver, 5)

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # API testing from Selenium
        print("California Marketing Url has", requests.get(h.url).status_code, "as status Code")
        code = requests.get(h.url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        h.delay()

        # verify website title
        try:
            assert driver.title == h.cm_title
            print("Title is Correct. Current Title is:", driver.title)
        except WDE:
            print("Title is different. Current Title is:", driver.title)

        # check some elements of header
        wait.until(EC.visibility_of_element_located((By.XPATH, h.X_head)))
        driver.find_element(By.XPATH, h.img_l).is_displayed()
        driver.find_element(By.XPATH, h.nw).is_displayed()

        driver.close()

    def test_firefox_Link1(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L1).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L1)))
        print('The First link is displayed and clickable')

        h.delay()

        # verify which social network is in the first link

        driver.find_element(By.XPATH, h.L1).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("first_link.png")
        print("Title of the first link in social network menu is", driver.title)
        print("Url of the first link in social network menu is", driver.current_url)

        # determine what is the social network

        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ('Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn')

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    def test_firefox_Link7(self):
        driver = self.driver
        wait = WebDriverWait(driver, 4)
        current_window = driver.current_window_handle
        old_windows = driver.window_handles

        # open website "California Marketing" and maximize browser window
        driver.get(h.url)
        driver.maximize_window()

        # check buttons functionality
        driver.find_element(By.XPATH, h.L7).is_displayed()
        wait.until(EC.element_to_be_clickable((By.XPATH, h.L7)))
        print('The Seventh link is displayed and clickable')

        h.delay()

        # verify which social network is in the seventh link

        driver.find_element(By.XPATH, h.L7).click()
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        h.delay()
        driver.get_screenshot_as_file("seventh_link.png")
        print("Title of the seventh link in social network menu is", driver.title)
        print("Url of the seventh link in social network menu is", driver.current_url)

        # determine what is the social network
        def check_SN(text, name_SN):
            return name_SN in text

        text = driver.title
        name_SN = ['Facebook', 'Twitter', 'X', 'YouTube', 'VK', 'LinkedIn']

        if check_SN(text, name_SN[0]):
            print("This link is Facebook")
        elif check_SN(text, name_SN[1]):
            print("This link is Twitter")
        elif check_SN(text, name_SN[2]):
            print("This link is X")
        elif check_SN(text, name_SN[3]):
            print("This link is YouTube")
        elif check_SN(text, name_SN[4]):
            print("This link is VK")
        elif check_SN(text, name_SN[5]):
            print("This link is LinkedIn")
        else:
            print("This link isn't a popular social network. Maybe it's not a social network")

        driver.close()
        driver.switch_to.window(current_window)

    # closing the browser
    def tearDown(self):
        self.driver.quit()
