# PerfStep
Performance Test Tool based on Locust and Behave

# Create demo environment
docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:latest

Access swagger in http://localhost:8080/api/v3 

# Execution

1.-  Folder 00_example_httpuser
Test description:
<img width="1033" alt="image" src="https://github.com/user-attachments/assets/95ae5367-f66f-43d3-837c-4f1484450b6e">


Create locustfile.py
locust
Open browser  http://0.0.0.0:8089
Example Host: http://localhost:8080/api/v3 

Running in headless mode (see output)
locust --headless -u 1 -r 1 -H http://localhost:8080/api/v3 

2.- Folder 01_example_user
locust --headless

# Bibliography
## Recomended courses
https://academy.qainsights.com/courses/learn-locust
https://github.com/QAInsights/Learn-Locust-Series

## Recommended resources
https://locust.io/
https://docs.locust.io/en/stable/
https://www.blazemeter.com/blog/locust-python
