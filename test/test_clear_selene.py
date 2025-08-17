from selene import browser, be, by
from selene.support.shared.jquery_style import s


def test_search_issue():
    browser.open('https://github.com/home')
    s('.search-input').click()
    s('#query-builder-test').send_keys('QAGURU_allure_hw10')
    s('#query-builder-test').submit()

    s(by.link_text('MozzhukhinRA/QAGURU_allure_hw10')).click()
    s('#issues-tab').should(be.visible).click()
