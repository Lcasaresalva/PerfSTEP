@no_driver
Feature: Execute request on resources # ../00_request_host.feature:2

  @get
  Scenario Outline: Resources Tasks Execution -- @1.1               # ../00_request_host.feature:13
    Given 10 users accessed with the proper profile every 5 seconds # None
    And the scenario should take "60" seconds                       # None
    When I execute the "GET" to "/user/logout" endpoint             # None

  Scenario Outline: Resources Tasks Execution -- @1.1               # ../00_request_host.feature:24
    Given 10 users accessed with the proper profile every 5 seconds # None
    And the scenario should take "60" seconds                       # None
    And I use the admin user                                        # None
    When I execute the "GET" to "/pet/1" endpoint                   # None

  Scenario Outline: Resources Tasks Execution -- @1.1               # ../00_request_host.feature:54
    Given 10 users accessed with the proper profile every 5 seconds # None
    And the scenario should take "60" seconds                       # None
    And the request body is                                         # None
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
    When I execute the "POST" to "/pet" endpoint                    # None

@no_driver @perf
Feature: Execute tasks on resources # ../01_load_test.feature:2

  @end
  Scenario Outline: Resources Tasks Execution -- @1.1               # ../01_load_test.feature:22
    Given 10 users accessed with the proper profile every 5 seconds # None
    And the scenario should take "60" seconds                       # None
    And I configure the following tasks with weights                # None
      | task                 | weight |
      | ThreadGroupForUsers  | 4      |
      | ThreadGroupForAdmins | 6      |
    When I execute the endurance scenario                           # None
    Then I check performance results according to                   # None
      | nfr   | criteria |
      | 95%   | 100      |
      | avgRT | 150      |
      | ratio | 0.05     |

