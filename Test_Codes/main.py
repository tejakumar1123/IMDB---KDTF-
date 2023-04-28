from time import sleep
from test_func.yaml_function import  teja_yaml
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select
import pytest

class Test_kdtf:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()
    
    def test_validlogin(self, boot):   
        yaml_file1 = 'F:\\imdbKDTF\\test_yaml\\loc.yaml'
        yaml_file2 = 'F:\\imdbKDTF\\test_yaml\\data.yaml'
        s = teja_yaml(yaml_file1)
        p = teja_yaml(yaml_file2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(p.yaml_reader()['url'])
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signin']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signinwith']).click()
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['username_locator']).send_keys(p.yaml_reader()['username'])
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['password_locator']).send_keys(p.yaml_reader()['password'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['submitButton_locator']).click()
        assert self.driver.title == 'IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows'
        print("SUCCESS : Logged in with Username {a} & {b}".format(a = s.yaml_reader()['username'],b = s.yaml_reader()['password']))
    
    def test_movieslist(self, boot):   
        yaml_file1 = 'F:\\imdbKDTF\\test_yaml\\loc.yaml'
        yaml_file2 = 'F:\\imdbKDTF\\test_yaml\\data.yaml'
        s = teja_yaml(yaml_file1)
        p = teja_yaml(yaml_file2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(p.yaml_reader()['url'])
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signin']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signinwith']).click()
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['username_locator']).send_keys(p.yaml_reader()['username'])
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['password_locator']).send_keys(p.yaml_reader()['password'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['submitButton_locator']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Menu']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Most_popular_movies']).click()
        
        List1 = self.driver.find_elements(by=By.XPATH, value=s.yaml_reader()['Popular_movies_list'])
        Movie_list = []
        for i in List1:
            Movie_list.append(i.text)
        
        for (i, itemno) in enumerate(Movie_list, 1):
            print(i, itemno)
        
        assert self.driver.title == 'Most Popular Movies - IMDb'
        print("SUCCESS : Listed Most popular movies in IMDb")
    
    def test_seachmenu(self, boot):   
        yaml_file1 = 'F:\\imdbKDTF\\test_yaml\\loc.yaml'
        yaml_file2 = 'F:\\imdbKDTF\\test_yaml\\data.yaml'
        s = teja_yaml(yaml_file1)
        p = teja_yaml(yaml_file2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(p.yaml_reader()['url'])
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signin']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signinwith']).click()
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['username_locator']).send_keys(p.yaml_reader()['username'])
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['password_locator']).send_keys(p.yaml_reader()['password'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['submitButton_locator']).click()
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['Searchmenu']).send_keys(p.yaml_reader()['Searchmenu_data'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['Searchmenu_button']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Movie_moreresults']).click()
        
        List2 = self.driver.find_elements(by=By.XPATH, value=s.yaml_reader()['Movieresults_list'])
        Movie_list = []
        for i in List2:
            Movie_list.append(i.text)
        
        for (i, itemno) in enumerate(Movie_list, 1):
            print(i, itemno)
        
        assert self.driver.title == 'Find - IMDb'
        print("SUCCESS : Listed Search results in IMDb")
    
    def test_createlist(self, boot):   
        yaml_file1 = 'F:\\imdbKDTF\\test_yaml\\loc.yaml'
        yaml_file2 = 'F:\\imdbKDTF\\test_yaml\\data.yaml'
        s = teja_yaml(yaml_file1)
        p = teja_yaml(yaml_file2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(p.yaml_reader()['url'])
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signin']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signinwith']).click()
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['username_locator']).send_keys(p.yaml_reader()['username'])
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['password_locator']).send_keys(p.yaml_reader()['password'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['submitButton_locator']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Profilemenu_button']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['your_lists']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Create_list']).click()
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['name_list']).send_keys(p.yaml_reader()['List_name'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['desc_list']).send_keys(p.yaml_reader()['List_descr'])
        sel = Select(self.driver.find_element(by=By.ID, value=s.yaml_reader()['type_list']))
        sel.select_by_visible_text("People")
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['list_button']).click()
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['add_list']).click()
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['add_list']).send_keys(p.yaml_reader()['It1'])
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['result1']).click()
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['add_list']).send_keys(p.yaml_reader()['It2'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['add_list']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['result1']).click()
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['add_list']).send_keys(p.yaml_reader()['It3'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['add_list']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['result1']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['list_done']).click()
        assert self.driver.title == 'Favorite Actors - IMDb'
        print("SUCCESS : Created New List in IMDb")
    
    def test_signout(self, boot):   
        yaml_file1 = 'F:\\imdbKDTF\\test_yaml\\loc.yaml'
        yaml_file2 = 'F:\\imdbKDTF\\test_yaml\\data.yaml'
        s = teja_yaml(yaml_file1)
        p = teja_yaml(yaml_file2)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(p.yaml_reader()['url'])
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signin']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Signinwith']).click()
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['username_locator']).send_keys(p.yaml_reader()['username'])
        self.driver.find_element(by=By.NAME, value=s.yaml_reader()['password_locator']).send_keys(p.yaml_reader()['password'])
        self.driver.find_element(by=By.ID, value=s.yaml_reader()['submitButton_locator']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['Profilemenu_button']).click()
        self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['signout']).click()
        assert self.driver.find_element(by=By.XPATH, value=s.yaml_reader()['signin_text']).text == 'Sign In'
        print("SUCCESS : Listed Search results in IMDb")
