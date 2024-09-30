@no_driver
Feature: Execute tasks on resources
         Inject load on some Resources-related APIS with a number of users

  @load
  Scenario: Full Load Scenario
    Given 10 users accessed with the proper profile every 5 seconds
    And the scenario should take "10" seconds
    And I configure the following tasks with weights
      | task                 | weight |
      | ThreadGroupForUsers  | 4      |
      | ThreadGroupForAdmins | 6      |
    When I execute the load scenario
    Then I check performance results according to
      | nfr   | criteria |
      | 95%   | 50       |
      | avgRT | 40       |
      | ratio | 0.05     |
