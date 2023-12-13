*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}  https://demo.automationtesting.in/Register.html#google_vignette

*** Test Cases ***
Register_Form
	Open Browser    ${url}  chrome
	Sleep    1
	Input Text    xpath://input[@ng-model='FirstName']  John
	Sleep   1
	Input Text    xpath://input[@ng-model='LastName']   Miller
	Sleep    1
	Input Text    xpath://textarea[@ng-model='Adress']     Vaniyambaditheru
	Sleep    1
	Input Text    xpath://input[@ng-model='EmailAdress']    j@yopmail.com
	Sleep    1
	Input Text    xpath://input[@type='tel']    995454554512
	Sleep    1
	Click Element        xpath://input[@value='Male']
	Sleep    1
    Click Element    xpath://input[@id='checkbox1']
    Sleep    1
    Select From List By Index            xpath://div[@id='msdd']
    Sleep   1
    Click Element    xpath://a[@text()='Icelandic']



*** Keywords ***
