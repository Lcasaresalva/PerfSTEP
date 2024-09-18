# PerfStep
Performance Test Tool based on Locust and Behave

# Create demo environment
docker run  --name swaggerapi-petstore3 -d -p 8080:8080 swaggerapi/petstore3:latest

Access swagger in http://localhost:8080/api/v3 

# Example 1

    1.-  Folder 00_example_httpuser
  
  ## Test scenario description:
  
  <img width="983" alt="image" src="https://github.com/user-attachments/assets/7490d64c-5cfb-41a4-bf83-36d193aa1d82">

  ## Execution 1

    Create locustfile.py
    locust -f locustfile.py –u 1 –r 1 –t 10 
    Open browser  http://0.0.0.0:8089
    
    Example Host: http://localhost:8080/api/v3 
    
    Running in headless mode (see output)
    locust --headless -u 1 -r 1 -H http://localhost:8080/api/v3 

# Example 2

  2.- Folder 01_example_user

  ## Test scenario description:

  <img width="932" alt="image" src="https://github.com/user-attachments/assets/01505e5e-27ba-46d8-abf3-c6c7bdd54ce2">

  ## Execution 2

  locust -f locustfile.py –u 4 –t 10 --headless


# Bibliography
## Recomended courses
https://academy.qainsights.com/courses/learn-locust
https://github.com/QAInsights/Learn-Locust-Series

## Recommended resources
https://locust.io/
https://docs.locust.io/en/stable/
https://www.blazemeter.com/blog/locust-python
