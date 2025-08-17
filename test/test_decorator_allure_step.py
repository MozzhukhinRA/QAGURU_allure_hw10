import allure
from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_start():
    open_browser()
    search_repository('MozzhukhinRA/QAGURU_allure_hw10')
    transition_repository('MozzhukhinRA/QAGURU_allure_hw10')
    open_issue()


@allure.step('Browser opening')
def open_browser():
    browser.open('https://github.com/home')


@allure.step('Search repository {repo}')
def search_repository(repo):
    s('.search-input').click()
    s('#query-builder-test').send_keys(repo)
    s('#query-builder-test').submit()


@allure.step('Opening {repo}')
def transition_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Opening issues')
def open_issue():
    s('#issues-tab').should(be.visible).click()