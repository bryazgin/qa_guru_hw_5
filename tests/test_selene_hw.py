from selene import browser, be, have, by
import os.path


def test_complete_form():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').should(be.blank).type('Sergey')
    browser.element('#lastName').should(be.blank).type('Bryazgin')
    browser.element('#userEmail').should(be.blank).type('test_selene@gmail.com')
    browser.all('.custom-control').element_by(have.exact_text('Male')).click()
    browser.element('#userNumber').should(be.blank).type('8999112233')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element(by.text('July')).click()
    browser.element('.react-datepicker__year-select').click().element(by.text('1995')).click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.all('.custom-control-label').element_by(have.exact_text('Sports')).click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('image/image.jpg'))
    browser.element('#currentAddress').should(be.blank).type('pr. Lenina, dom 28, kv. 128')
    browser.element('#state').click().element(by.text('Haryana')).click()
    browser.element('#city').click().element(by.text('Karnal')).click()
    browser.element('#submit').click()

    browser.element('.modal-header').should(have.exact_text('Thanks for submitting the form'))
    browser.element('.table-responsive').all('td:nth-of-type(2)').should(have.texts(
        'Sergey Bryazgin',
        'test_selene@gmail.com',
        'Male',
        '8999112233',
        '10 July,1995',
        'Computer Science',
        'Sports',
        'image.jpg',
        'pr. Lenina, dom 28, kv. 128',
        'Haryana Karnal'
    ))


