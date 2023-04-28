from test_func.yaml_function import teja_yaml
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager

import pytest

class Test_kdtf:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    def test_validlogin(self, boot):   
        yaml_file = 'F:\\imdbKDTF\\teja.yaml'
        s = teja_yaml(yaml_file)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(s.yaml_reader()['url'])
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signin']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signinwith']).click()
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['username_locator']).send_keys(s.yaml_reader()['username'])
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['password_locator']).send_keys(s.yaml_reader()['password'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['submitButton_locator']).click()
        assert self.driver.title == 'IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows'
        print("SUCCESS : Logged in with Username {a} & {b}".format(a = s.yaml_reader()['username'],b = s.yaml_reader()['password']))
