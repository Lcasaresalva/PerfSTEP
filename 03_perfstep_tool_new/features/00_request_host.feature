@no_driver
Feature: Execute request on resources
#  Background: We want to inject load on some Resources-related APIS with a number of users

  @get
  Scenario Outline: Resources Tasks Execution
    Given <users> users accessed with the proper profile every <spawn_rate> seconds
    And the scenario should take "<test_time>" seconds
    When I execute the "GET" to "/user/logout" endpoint

    Examples:
      | users | spawn_rate | test_time |
      |    10 |         5  | 10        |


  Scenario Outline: Resources Tasks Execution
    Given <users> users accessed with the proper profile every <spawn_rate> seconds
    And the scenario should take "<test_time>" seconds
    And I use the admin user
    When I execute the "GET" to "/pet/1" endpoint

    Examples:
      | users | spawn_rate | test_time |
      |    10 |         5  | 10        |

  @post
  Scenario Outline: Resources Tasks Execution
    Given <users> users accessed with the proper profile every <spawn_rate> seconds
    And the scenario should take "<test_time>" seconds
    And the request body is
    """
      {
        "id": 10,
        "name": "doggie",
        "category": {
          "id": 1,
          "name": "Dogs"
        },
        "photoUrls": [
           "string"
        ],
        "tags": [
          {
            "id": 0,
            "name": "string"
          }
        ],
        "status": "available"
      }
    """
    When I execute the "POST" to "/pet" endpoint

    Examples:
      | users | spawn_rate | test_time |
      |    10 |         5  | 10        |