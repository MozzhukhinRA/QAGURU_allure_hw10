import allure
from allure_commons.types import Severity
from selene import browser, be, by
from selene.support.shared.jquery_style import s
from allure import attachment_type


def test_label_01_passed():
    allure.attach("Test", name="Text", attachment_type=attachment_type.TEXT)
    allure.dynamic.feature('Test Case : Smoke')
    allure.dynamic.story('asser for issues be visible')
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.link('https://github.com/')
    allure.dynamic.tag('UI', 'smoke')

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


#Сценарий заранее задуманный как провальный
# def test_label_02_failed():
#     allure.attach("Test", name="Text", attachment_type=attachment_type.TEXT)
#     allure.dynamic.feature('Test Case : Regress')
#     allure.dynamic.story('asser for issues be visible')
#     allure.dynamic.severity(Severity.MINOR)
#     allure.dynamic.link('https://github.com/')
#     allure.dynamic.tag('UI', 'regress')
#
#     with allure.step('Opening browser'):
#         browser.open('https://github.com/home')
#
#     with allure.step('Searching repository'):
#         s('.search-input').click()
#         s('#query-builder-test').send_keys('QAGURU_allure_hw10')
#         s('#query-builder-test').submit()
#
#     with allure.step('Opening QAGURU_allure_hw10 link'):
#         s(by.link_text('MozzhukhinRA/QAGURU_allure_hw10')).click()
#
#     with allure.step('Opening issues'):
#         s('#issue-tab').should(be.visible).click()
