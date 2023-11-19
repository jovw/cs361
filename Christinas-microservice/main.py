## This is an example on how to call on the REST API
import requests

## Call to microservice for getting list of books absed on given book title
def get_list_of_books(book_title):
    url = "http://127.0.0.1:5001/books/" + book_title
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else: 
        print("Error while fetching data", res.status_code)
        return None

## Call to microservice to get the book details absed on Volumne ID
def get_book_details(volume_id):
    url = 'http://127.0.0.1:5001/book-details/' + volume_id
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    else:
        print("Error while fetching data", res.status_code)
        return None

if __name__ == '__main__':
    book_title = input("What book would you like to look up?\n")
    books = get_list_of_books(book_title)
    if books:
        items = books.get('items', [])
         # For demo purposes, only the book title and the thread id are printed,
         # but all data for all the books are returned.
         # Only the first 20 books are printed as sometimes it returns many books.
        if items:
            for item in items[:20]:
                book_title = item['volumeInfo']['title']
                volume_id = item['id']
                print(f'title: {book_title}, volume_id: {volume_id}')
    print('\n')
    thread_id = input("What is the volume ID of the book you would like to see more details about?\n")
    book_details = get_book_details(thread_id)
    ## For the purpose of this demo I am only going to print the Title, Author name, publication date 
    # and descriptiuon fo the given book 
    ## but al the data for this book is returned - if you do not need anything else, we can adjust this to only
    # return the volume info since it looks like this will contain all info you needed
    if book_details:
        title = book_details['volumeInfo']['title']
        authors = ', '.join(book_details['volumeInfo'].get('authors', []))
        publicationDate = book_details['volumeInfo']['publishedDate']
        summary = book_details['volumeInfo']['description']

        print('\n')
        print(f'Books Title: {title}')
        print(f'Authors: {authors}')
        print(f'Publication Date: {publicationDate}')
        print(f'\nSummary:\n {summary}\n')
