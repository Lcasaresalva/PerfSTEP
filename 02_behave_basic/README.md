# BEHAVE Basics
Behave minimum project

1. Lauch testing environment 
   ```bash
      $ docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:latest
   ```

2. Go to `02_behave_basic` folder


3. Install prerequisites

   ```bash
   $ pip install -r requirements.txt
   ```
4. Execute

   ```bash
   $ behave
   ```
   **See default config in /behave.ini*


5. Expected Result:
   ```bash
   ...
   1 feature passed, 0 failed, 0 skipped
   1 scenario passed, 0 failed, 0 skipped
   1 step passed, 0 failed, 0 skipped, 0 undefined
   ...
   
    File: 02_behave_basic/_output/xmlresults/TESTS-hello_world.xml is created 

### Behave Documentation:

https://behave.readthedocs.io/en/latest/