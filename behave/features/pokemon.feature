Feature: Pokemon API

    As a user, 
    I want to make a GET request via a REST API,
    and obtain certain data for a specified pokemon. 

    Scenario: Test example
    Given Small talk
    When Hi
    Then Bye

    Scenario Outline: Verify GET request
    Given I have a RESTful API "<endpoint>" 
    When I make a GET request for "<pokemon>" data
    Then the response should be "<status_result>"

    Examples: Pokemon
    | endpoint                          | pokemon       | status_result |
    | https://pokeapi.co/api/v2/pokemon/| charizard     | 200           | 
    | https://pokeapi.co/api/v2/pokemon/| dragonite     | 200           |
    | https://pokeapi.co/api/v2/pokemon/| DoesNotExist  | 404           |


