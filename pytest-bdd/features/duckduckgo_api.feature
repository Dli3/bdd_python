@service @duckduckgo
Feature: DuckDuckGo Instant Answer API
    As an application developer,
    I want to get instant answers for search terms via a REST API.
    So that my app can get answers anywhere. 

    Scenario Outline: Basic DuckDuckGo API Query
        Given the DuckDuckGo API is queried with "<phrase>" using "json" format
        Then the response status code is "200"
        And the response contains results for "<phrase>"

        Examples: Animals
        | phrase |
        | dog    |
        | duck   |
        | cat    |
        
        Examples: Pokemon
        | phrase     |
        | Pikachu    |
        | Charmander |
        | Charizard  |
