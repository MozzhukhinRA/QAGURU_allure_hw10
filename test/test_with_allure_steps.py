import allure
from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_search_issue():
    with allure.step('Opening browser'):
        browser.open('https://github.com/home')

    with allure.step('Searching repository'):
        s('.search-input').click()
        s('#query-builder-test').send_keys('QAGURU_allure_hw10')
        s('#query-builder-test').submit()

    with allure.step('Opening QAGURU_allure_hw10 link'):
        s(by.link_text('MozzhukhinRA/QAGURU_allure_hw10')).click()

    with allure.step('Opening issues'):
        s('#issues-tab').should(be.visible).click()
