# Locust Basics
Scripting usage and concepts of *locust*.
## Scenario 1
HTTP GET/POST requests sent to a target API from the locust file. Test executed in the Locust CLI.
1. Folder `00_request_example`
2. Scenario parameters:
   ```text
   - Host: http://localhost:8080/api/v3
   - Use Case: POST /order/store
   - Users: 10
   - Spawn-rate: 1 user/sec
   - Ramp-up duration: 10 sec
   - Scenario duration: 20 sec
   ```
3. Command execution:
    ```bash
    $ locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 1 -t 20 --headless
   ```
   *Example in command line with 4 cores:*
  
   ```bash
   $ locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 2 -t 20 --processes 4
   ```
   
   *Example in command line with autoquit to avoid the usage of ctrl+c:*
  
   ```bash
   $ locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 2 -t 20 --processes -1 --autostart --autoquit 3
   ```

## Scenario 2
Locust file that implements a complete load model. The load is distributed between two different user profiles and several use cases in a target API.
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
   ```text
   RATIO PER CLASS
   - 60.0% ThreadGroupForAdmin
      - 14.3% update_pet
      - 28.6% order_store
      - 57.1% return_inventory
   - 40.0% ThreadGroupForUsers
      - 33.3% find_pet
      - 66.7% delete_order
   
   TOTAL RATIO
   - 60.0% ThreadGroupForAdmin
      - 8.6% update_pet
      - 17.1% order_store
      - 34.3% return_inventory
   - 40.0% ThreadGroupForUsers
      - 13.3% find_pet
      - 26.7% delete_order
   ```

3. Command execution:
    ```bash
    $ locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -r 2 -t 20 --processes -1 --headless
    ```
