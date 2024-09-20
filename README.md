# PerfStep

*PerfSTEP* is a Performance Test Tool based on Locust and Behave

## Prerequisites

- Python 3.9 or later
- Locust installation:
    ```bash
    $ pip install locust
    $ locust -V
  
    locust 2.31.5 from /usr/local/lib/python3.12/site-packages/locust (python 3.12.5)
    ```
- Create demo environment
    ```bash
    $ docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:latest
    
    Access swagger in http://localhost:8080/api/v3 
    ```

## PerfStep Course guidelines

- [Locust Basics](00_locust_basics/README.md>).
- [Locust Scripts](01_locust_scripts/README.md>).
- [Behave Basic](02_behave_basic/README.md>).
- [PerfSTEP](03_perfstep_tool/README.md>).

## Bibliography
### Recomended courses
https://academy.qainsights.com/courses/learn-locust
https://github.com/QAInsights/Learn-Locust-Series

### Recommended resources
https://locust.io/
https://docs.locust.io/en/stable/
https://www.blazemeter.com/blog/locust-python
https://cucumber.io/docs/bdd/
https://behave.readthedocs.io/en/latest/
