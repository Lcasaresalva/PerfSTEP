# BEHAVE Basics
Behave minimum project

1. Go to `02_behave_basic` folder 

2. Source tree organization:

   ```
   .
   ├── _output (directory generated in the test execution)
   └── features
        ├── steps (steps and libraries used in the scearios)
        ├── *.feature (Files with the scenarios)
        ├── behave.ini (behave configuration file)
        └── requirements.txt (python requirements)
   ```
3. Install prerequisites:

   ```bash
   $ pip install -r requirements.txt
   ```
   Recommendation: install Python requirements into a virtual environment.


4. Execute:

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
   ``` 
   Note: output file defined in *behave.ini* file

### Behave Documentation:

- https://behave.readthedocs.io/en/latest/