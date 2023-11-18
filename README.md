# Microservice Implementation

## Communication Contract 
This README serves as the communication contract. I will not amke any major data to the code, besdies waht is needed to accomodate for partners project 
Main communication pipeline will be REST calls

## How to set up the virtual enviroment 
1. open a terminal at the root of the project
2. run the following commands:
```
!pip3 install --user virtualenv
!python3 -m venv .
!source ./bin/activate
!pip3 install flask
```

## How to start up the microservice 
1. open up a terminal at the parent folder of teh microservice.py file
2. ex if your folder structure looks like this:
```
Project
  |- MicroService
    |- main.py
    |- microservice.py
```
You would open the terminal at MicroService 
3. run the following command: 
```
python3 microservice.py
```

## How to programatically request data
### Request for book list data
Get the book title input from the user: 

Use the book title to the call on the mircoservice:
```python
def get_list_of_books(book_title):
    url = "http://127.0.0.1:5001/books/" + book_title
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else: 
        print("Error while fetching data", res.status_code)
        return None
```

### Request for book detail data
Get the volume ID from the user: 

Use the volume ID to call on the microservice:
```python
## Call to microservice to get the book details absed on Volumne ID
def get_book_details(volume_id):
    url = 'http://127.0.0.1:5001/book-details/' + volume_id
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        print("Error while fetching data", res.status_code)
        return None
```

## How to programmatically receive data
