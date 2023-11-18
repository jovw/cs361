## This contains both API Calls 
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

## To get the list of books absed on the given title 
@app.route('/books/<title>', methods=['GET'])
def book_list(title):
    headers = request.headers
    print('\n')
    print('---- HEADER INFORMATION FOR GET BOOK LIST ----')
    for key, value in headers.items():
        print(f'{key}: {value}')
    print('----------------------------\n')

    try: 
        url = f'https://www.googleapis.com/books/v1/volumes?q={title}'
        res = requests.get(url)
        if res.status_code == 200:
            return jsonify(res.json()), 200
        else:
            return jsonify({"error": "Failed to fetch data from Google Books API"}), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

## To get the details for the book absed on given thread ID
@app.route('/book-details/<volume_id>', methods=['GET'])
def book_detail(volume_id):
    headers = request.headers
    print('\n')
    print('---- HEADER INFORMATION FOR GET BOOK DETAILS----')
    for key, value in headers.items():
        print(f'{key}: {value}')
    print('----------------------------\n')

    try: 
        url = f'https://www.googleapis.com/books/v1/volumes/{volume_id}'
        res = requests.get(url)
        if res.status_code == 200:
            return jsonify(res.json()), 200
        else:
            return jsonify({"error": "Failed to fetch data from Google Books API"}), res.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)