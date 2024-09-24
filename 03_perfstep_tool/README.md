# PerfStep
Performance Test Tool based on Locust and Behave

## How - To

1. Lauch testing environment 
   ```bash
      $ docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:latest
   ```
2. Go to `03_perfstep_tool` folder

3. Install prerequisites

   ```bash
   $ pip install -r requirements.txt
   ```
4. Execute
   ```bash
      $ behave -o _output/output
      ```

   **See default config in /behave.ini*

