# PerfSTEP
Performance Test Tool based on Locust and Behave

## How - To

1. Go to `03_perfstep_tool` folder 
2. Source tree organization:

   ```
   .
   ├── _output (directory generated in the test execution included in .gitgnore)
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

4. Execute scenarios:
   1. Requests scenarios:
      ```bash
         $ behave -t "@get,@post"
      ```
   2. Load scenario:
      ```bash
         $ behave -t "@load"
      ```
      **See default config in /behave.ini*

