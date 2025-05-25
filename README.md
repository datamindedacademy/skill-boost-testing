# Skill Boost Testing
## Getting started

You can simply click the button below to start the exercise environment within
GitHub Codespaces.
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/datamindedacademy/skill-boost-testing)

## Exercises

- Exercise 1: Simple unit testing. Take a look at the code in `/skill_boost_testing/galgje/galgje.py` and write unit tests for the functions in this file.
- Exercise 2: Practice mocking with mocks, stubs and fakes with a service making use of a database. 
- Exercise 3: We are going to create a small test application to process customer orders. We want to take an order object and fill it with a warehouse object. An order is very simple. It only has a String product and an int quantity. A warehouse keeps an inventory of different products.
When we ask our order to fill itself with a warehouse object, then There are 2 possible responses. If there are enough products in the warehouse for our order, then our order will be filled with these products. If there are not enough products available in the warehouse, then the order will not be filled and nothing will happen to the warehouse.
The code and initial tests are already written. Write the following extensions and test them:
  - In the above we used a real warehouse object in our unit tests. We even used state verification on our warehouse object to see if the state is what we expect. In this exercise we only want to test an order and we want to fake the behavior of a warehouse. We want to test if the fill method works correctly and therefore see if the property isFilled is set to true when we can successfully remove products from the warehouse. Rewrite the 2 existing tests using a mock warehouse object.
  - Whenever an order fails, and there is therefore too little stock in the warehouse, we want to send out an email. The problem is that during testing we do not want to send real emails to customers. So instead we create a fake, a test double of our email system, one that we can check and manipulate. Create an interface Mailservice with one method called `send`, this method returns nothing and has a String message as a parameter. Then create a fake mail service that implements this interface. Make sure that you keep track of the emails that have been sent in this class.
Next, test whether an email is sent when an order has failed. You will see that we use state verification here to see if the email has been sent. This is of course a very simple test. We only test that a message has been sent. We have not tested whether it was sent to the right person or with the right content, but it is sufficient to illustrate how it works.
  - We can also use mocking to test this functionality! In this case, we do not use our FakeMailService class. Rewrite the same test using mocking. In both cases, we use test doubles instead of the real email service. The difference is that the fake uses state verification, while the mock uses behavior verification. In order to use a fake, we had to add some extra methods to work with it. For example, we had to be able to query how many emails have been sent. However, mock objects always use behavior verification.