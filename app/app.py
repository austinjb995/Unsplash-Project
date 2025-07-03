from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Unsplash API key (replace with your own key)
UNSPLASH_ACCESS_KEY = 'your_access_key_here'

@app.route('/', methods=['GET'])
def index():
    return render_template('frontpage.html')

@app.route('/search', methods=['GET', 'POST'])
def search_images():
    images = []
    query = ''
    error = None

    if request.method == 'POST':
        query = request.form.get('tags', '').strip()
        if not query:
            error = "Please enter search tags."
        else:
            url = "https://api.unsplash.com/search/photos"
            params = {
                'query': query,
                'client_id': UNSPLASH_ACCESS_KEY,
                'per_page': 20
            }
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()
                images = [item['urls']['small'] for item in data.get('results', [])]
                if not images:
                    error = f"No results found for '{query}'."
            except requests.RequestException as e:
                error = "Failed to fetch images. Please try again later."
                print(f"Unsplash API error: {e}")

    return render_template('index.html', images=images, query=query, error=error)

if __name__ == '__main__':
    app.run(debug=True)

