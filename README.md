# CS361_Microservice
 
## Setting up the server

If you are planning to set up the server locally, complete the following steps:

1) Open the directory locally. 

2) Ensure you have Python installed using the terminal: 

`python --version`

3) Run the pip install to install dependencies: 
`pip3 install pipenv`
`pipenv install`

4) Activate the virtual environment.

`pipenv shell`

5) Run app.py, which starts the server and contains routing for the POST and GET requests.  

`python app.py`

6) Confirm the server is live by checking the URL: http://localhost:5000

## Making requests through Python Requests Implementation: 

### Endpoints:
- POST: /api/healthdata/post
- GET: /api/healthdata
- GET by ID: /api/healthdata/[id] (exclude brackets) 
 
1) Run Python_Requests_Implementation/myreq.py. This will give you options to submit data through the terminal.
- An example of a successful POST request is below.

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/722b09be-84d9-4c2d-b1a1-fb3a65d0deaf)

- An example of a successful GET request is below. 

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/9131b5ac-f262-45d8-996f-d1465e7c7149)

- An example of a successful GET request by ID is below.

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/5a99fdcd-9ab1-4538-a92f-9a6b28b73036)


### Making requests through Web Page: 

1) Go to http://localhost:5000 to view the following options:

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/d6054bc4-675c-4f55-8621-313f02d0a46f)

An example of how to POST data:

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/bc5f5ac1-d4f3-4c26-aff1-2c0db7094091)

An example of how to GET data by Patient ID:

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/3fb6bfc7-6197-44d9-a219-71fc90364d8c)

An example of how to GET all data:

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/2aa18a45-e5b1-437a-b8ac-ca3bd017ebb8)



### UML Sequence Diagram

![Microservice UML Sequence](https://github.com/avni-g/CS361_Microservice/assets/61604206/3f67624a-40ab-460f-85ff-85ecf2b0a663)


