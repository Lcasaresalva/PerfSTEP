@no_driver
Feature: Execute tasks on resources
         Inject load on some Resources-related APIS with a number of users

  @load
  Scenario Outline: Resources Tasks Execution
    Given <users> users accessed with the proper profile every <spawn_rate> seconds
    And the scenario should take "<test_time>" seconds
    And I configure the following tasks with weights
      | task                 | weight |
      | ThreadGroupForUsers  | 4      |
      | ThreadGroupForAdmins | 6      |
    When I execute the load scenario
    Then I check performance results according to
      | nfr   | criteria |
      | 95%   | 100      |
      | avgRT | 150      |
      | ratio | 0.05     |

    Examples:
      | users | spawn_rate | test_time |
      | 10    | 5          | 10        |