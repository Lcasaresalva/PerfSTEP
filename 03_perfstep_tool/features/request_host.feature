@no_driver
Feature: Execute request on resources
#  Background: We want to inject load on some Resources-related APIS with a number of users

  @req
  Scenario Outline: Resources Tasks Execution
    Given <users> users accessed with the proper profile every <spawn_rate> seconds
    And the scenario should take "<test_time>" seconds
    When I execute the "GET" to "/user/logout" endpoint

    Examples:
      | users | spawn_rate | test_time |
      |    10 |         5  | 60        |