from selenium import webdriver
from fixture.table_helper import TableHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.table = TableHelper(self)

    def destroy(self):
        self.wd.quit()
