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
- GET by ID: /api/healthdata/<id>
 
1) Run Python_Requests_Implementation/myreq.py. This will give you options to submit data through the terminal.
- An example of a successful POST request is below.

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/722b09be-84d9-4c2d-b1a1-fb3a65d0deaf)

- An example of a successful GET request is below. 

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/9131b5ac-f262-45d8-996f-d1465e7c7149)

- An example of a successful GET request by ID is below.

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/5a99fdcd-9ab1-4538-a92f-9a6b28b73036)


### Making requests through Web Page: 

1) Go to http://localhost:5000 to view the following options:

<img width="289" alt="image" src="https://github.com/avni-g/CS361_Microservice/assets/61604206/56401738-2a13-4a58-a9e3-86891bb22ef6">

To POST data:

 <img width="388" alt="image" src="https://github.com/avni-g/CS361_Microservice/assets/61604206/f7861e18-95f7-4e5a-b9f0-e208b65cfa20">

TO GET data: 

 <img width="394" alt="image" src="https://github.com/avni-g/CS361_Microservice/assets/61604206/8404b449-c839-43d7-ba05-57d7c4d36c63">

To GET data by ID, update the URL: 

![image](https://github.com/avni-g/CS361_Microservice/assets/61604206/f6730218-4665-4c8b-9d0a-1c488d1d6049)

## Optional future development based on partner feedback 

At this time, the following optional elements of the microservice are not implemented: 
- HTML submission form to GET by ID.
- GET by Patient ID. (Get by ID currently searches for the Record ID). 
