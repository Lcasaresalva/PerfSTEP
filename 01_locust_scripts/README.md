# PerfStep
Performance Test Tool based on Locust and Behave

# Create demo environment
docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:latest

Access swagger in http://localhost:8080/api/v3 

# Execution

1.-  Folder 00_example_httpuser
locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -t 20 --processes 4 --autostart --autoquit 3

Running in headless mode (see output)
locust -f runTest.py --host http://localhost:8080/api/v3 -u 10 -t 20 --processes 4 --autostart --autoquit 3

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