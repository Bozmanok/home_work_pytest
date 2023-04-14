from fixture.application import Application
from fixture.table_helper import TableHelper
import pytest


@pytest.fixture(scope='session', autouse=True)
def app() -> Application:
    app = Application()
    yield app
    app.destroy()


@pytest.fixture(scope='session')
def data_from_table(app) -> list:
    table = TableHelper(app=app)
    table.open_page_with_table()

    return table.save_data_of_all_rows()
