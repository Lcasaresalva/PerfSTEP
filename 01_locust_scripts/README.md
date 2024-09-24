# Locust Basics
Scripting usage and concepts of *locust*.

## Example 1

GET/POST Http requests interface invoked from locustfile and executed in locust CLI.

1. Folder `00_request_example`
2. Scenario parameters:
   ```text
   - Host: http://localhost:8080/api/v3
   - Use Case: POST /order/store
   - Users: 10
   - Spawn-rate: 1 user/sec
   - Ramp-up duration: 10 sec
   - Cores: 4
   - Scenario duration: 20 sec
   ```
3. Command execution:
    ```bash
    $ locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 1 -t 20 --processes 4 --headless
    ```

## Example 2
Thread groups classes to create a well-distributed Load Test Scenario launched from locust CLI.

1. Folder `01_load_example`
2. Scenario parameters:

   ```text
   - Host: http://localhost:8080/api/v3
   - Users: 10
   - Spawn-rate:2 users/sec
   - Ramp-up duration: 5 sec
   - Cores: Autodetect all logical cores (-1)
   - Scenario duration: 20 sec
   ```
   
   ![alt text](../readme_resources/img/01_01_load_scenario.png)

3. Command execution:
    ```bash
    $ locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 2 -t 20 --processes -1 --headless
    ```
