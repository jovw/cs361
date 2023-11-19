# Microservice Implementation 🌐

## Communication Contract 📜
This README serves as the communication contract. I will not make any major changes to the code, besides what is needed to accommodate our partners' projects.\
The main communication pipeline will be REST calls.

## How to Set Up the Virtual Environment 🖥️
1. Open a terminal at the root of the project.
2. Run the following commands:
```
!pip3 install --user virtualenv
!python3 -m venv .
!source ./bin/activate
!pip3 install flask
```

## How to Start Up the Microservice 🚀
1. Open a terminal at the parent folder of the `microservice.py` file.
2. Example: If your folder structure looks like this:
```
Project
  |- MicroService
    |- main.py
    |- microservice.py
```
You would open the terminal at `MicroService`. \
3. Run the following command: 
```
python3 microservice.py
```

## How to Programmatically Request and Receive Data 🔄
Note: This approach is slightly different from what is provided in `main.py`.
In `main.py`, user inputs are gathered under `if __name__ == '__main__'`, and then other functions are called.\
In this example, user input is given within the `get_list_books()` and `get_book_details()` functions

### Request for Book List Data 📚
Use the book title to call the microservice:
```python
def get_list_of_books():
 # Get the book title input from the user: 
 book_title = input("What book would you like to look up?\n")
 url = "http://127.0.0.1:5001/books/" + book_title
 res = requests.get(url)
 if res.status_code == 200:
     books = res.json()
     if books:
         items = books.get('items', [])
         # For demo purposes, only the book title and the thread id are printed,
         # but all data for all the books are returned.
         # Only the first 20 books are printed as sometimes it returns many books.
         if items:
             for item in items[:20]:
                 book_title = item['volumeInfo']['title']
                 volume_id = item['id']
                 print(f'Title: {book_title}, Volume ID: {volume_id}')
 else: 
     print("Error while fetching data", res.status_code)
     return None
```
📥 books will contain the received data

### Request for Book Detail Data 📖
Use the volume ID to call the microservice:
```python
def get_book_details():
    volume_id = input("What is the volume ID of the book you would like to see more details about?\n")
    url = 'http://127.0.0.1:5001/book-details/' + volume_id
    res = requests.get(url)
    if res.status_code == 200:
        # book_details contain received Data 
        book_details = res.json()
        # For this demo, only the Title, Author name, publication date,
        # and description of the given book are printed,
        # but all data for this book is returned.
        if book_details:
            title = book_details['volumeInfo']['title']
            authors = ', '.join(book_details['volumeInfo'].get('authors', []))
            publicationDate = book_details['volumeInfo']['publishedDate']
            summary = book_details['volumeInfo']['description']

            print('\n')
            print(f'Book's Title: {title}')
            print(f'Authors: {authors}')
            print(f'Publication Date: {publicationDate}')
            print(f'\nSummary:\n {summary}\n')
    else:
        print("Error while fetching data", res.status_code)
        return None
```
📥 book_details will contain the received data

[Here are the code reference: `main.py`, `microservice.py`]

## UML Sequence Diagram 📋
![uml](https://github.com/jovw/cs361/blob/main/Images/uml.jpg)
