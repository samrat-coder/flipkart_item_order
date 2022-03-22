Feature: Mobile_order
    Scenario: Mobile_order
        Given User create driver
        And   User open url
        When  User enter mobile number '9123990228' and password 'samrat@1234'
        And   User search item 'mobiles'
        And   User short price '10000'
        And   User select brand name 'realme'
        And   User select first item
        And   switch to window
        And   User select buy now
        And   User select delevery
        And   User select continue
        And   User select credit card
        And   User enter credit card number '4929179761505439'
        And   User enter month '09'
        And   User enter year '23'
        And   User enter cvv '130'
        And   User select pay amount
        Then  User close driver




