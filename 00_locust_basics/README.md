# Locust Basics
Basic usage and concepts of *locust*.

## Example 1
HTTPs request into *locustfile.py* and executed from locust UI.

1. Folder `00_example_httpuser`
2. Scenario parameters:
    ```text
   - Host: http://localhost:8080/api/v3
   - Use Case: /order/store
   - Users: 1
   - Spawn-rate: 1 users/sec
   - Time duration: 10 sec
   ```
3. Command execution:
   1. By default:
       ```bash
       $ locust –u 1 –r 1 –t 10
    
       Access Locust in http://0.0.0.0:8089
       ```
   2. Specifying file:
       ```bash
       $ locust -f locustfile.py –u 1 –r 1 –t 10
    
       Access Locust in http://0.0.0.0:8089
       ```
    3. Headless execution:
       ```bash
       $ locust -f locustfile.py –u 1 –r 1 –t 10 --headless
       ```


## Example 2
Performance load scenario in locustfile.py through locust CLI.

1. Folder `01_example_user`
2. Scenario parameters:
    ```text
   - Use Case: 
      - 50% MyFirstTest
      - 50% MySecondTest
   - Users: 4
   - spawn-rate = 2 users/s
   - Time duration: 10 sec
   ```
3. Command execution:
   ```bash
   locust -f locustfile.py –u 4 -r 2 –t 10 --headless
   ```


