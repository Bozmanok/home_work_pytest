from model.table import Table
from selenium.webdriver.common.by import By


class TableHelper:
    def __init__(self, app):
        self.app = app

    def open_page_with_table(self):
        wd = self.app.wd
        wd.get("https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites")

    def get_count_rows_of_table(self):
        wd = self.app.wd
        rows = wd.find_elements(By.XPATH, '/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr')

        return len(rows)

    def get_values_of_frontend(self, i):
        wd = self.app.wd
        frontends = []
        x_path = f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[{i}]/td[3]'
        rows = wd.find_elements(By.XPATH, f'{x_path}/a')
        for j in range(1, len(rows) + 1):
            frontends.append(wd.find_element(By.XPATH, f'{x_path}/a[{j}]').text)

        return frontends

    def get_values_of_backend(self, i):
        wd = self.app.wd
        backends = []
        x_path = f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[{i}]/td[4]'
        rows = wd.find_elements(By.XPATH, f'{x_path}/a')
        for j in range(1, len(rows) + 1):
            backends.append(wd.find_element(By.XPATH, f'{x_path}/a[{j}]').text)

        return backends

    def get_values_of_database(self, i):
        wd = self.app.wd
        databases = []
        x_path = f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[{i}]/td[5]'
        rows = wd.find_elements(By.XPATH, f'{x_path}/a')
        for j in range(1, len(rows) + 1):
            databases.append(wd.find_element(By.XPATH, f'{x_path}/a[{j}]').text)

        return databases

    def save_data_from_row_of_table(self, i):
        wd = self.app.wd
        x_path = f'/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/table[1]/tbody/tr[{i}]'
        websites = wd.find_element(By.XPATH, f'{x_path}/td[1]/a').text
        popularity_text = wd.find_element(By.XPATH, f'{x_path}/td[2]').text
        if '[' in popularity_text:
            popularity_text = popularity_text.split('[')[0]
        popularity = int(''.join([x for x in popularity_text if x.isdigit()]))
        frontend = self.get_values_of_frontend(i)
        backend = self.get_values_of_backend(i)
        database = self.get_values_of_database(i)
        notes = wd.find_element(By.XPATH, f'{x_path}/td[6]').text

        return Table(
            websites=websites,
            popularity=popularity,
            frontend=frontend,
            backend=backend,
            database=database,
            notes=notes,
        )

    def save_data_of_all_rows(self):
        data_from_table = []
        count_rows = self.get_count_rows_of_table()
        for i in range(1, count_rows + 1):
            data_from_table.append(self.save_data_from_row_of_table(i))

        return data_from_table
