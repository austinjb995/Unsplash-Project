# Unsplash Image Search Web App

A Flask-based web application that allows users to search for high-quality images from the [Unsplash API](https://unsplash.com/developers). Built for quick deployment, lightweight interaction, and demonstration of client-server rendering workflows.

---

## Features

- Search Unsplash images by keywords
- Display responsive image gallery
- Clean UI with Jinja2 templating
- API integration using `requests`
- Server-side form handling and error feedback

---

## 📁 Project Structure

```
Unsplash-Project/
├── app/
│   ├── app.py                # Flask application
│   └── templates/            # HTML templates (Jinja2)
│       ├── frontpage.html    # Landing/search page
│       └── index.html        # Search result display
├── static/
│   ├── style.css             # Optional custom CSS
│   └── main.js               # JS for client-side rendering (optional)
├── .flaskenv                 # Flask environment config
├── webdev/                   # Python virtual environment
└── README.md
```

---

## Prerequisites

- Python 3.8+
- Pip
- A valid [Unsplash API access key](https://unsplash.com/developers)

---

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/unsplash-project.git
   cd unsplash-project
   ```

2. **Set up a virtual environment (optional but recommended):**

   ```bash
   python -m venv webdev
   source webdev/bin/activate  # On Windows use: webdev\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install flask requests python-dotenv
   ```

4. **Configure `.flaskenv`:**

   Create a `.flaskenv` file in the root directory with the following:

   ```
   FLASK_APP=app.app
   FLASK_ENV=development
   ```

5. **Insert your Unsplash API key:**

   Edit `app/app.py` and replace the placeholder:

   ```python
   UNSPLASH_ACCESS_KEY = 'your_access_key_here'
   ```

6. **Run the app:**

   ```bash
   flask run
   ```

7. **Visit your browser:**

   ```
   http://127.0.0.1:5000/
   ```

---

## Example Searches

Try searching for:

- `mountains`
- `dogs`
- `technology`
- `sunset`

---

## Notes

- This project uses a simple form-based search with POST/GET handling.
- Image rendering can be controlled via Jinja or JavaScript (`main.js`).
- API limits apply based on your Unsplash account level.

---

## License

This project is for educational/demo purposes. All images are provided by [Unsplash](https://unsplash.com/terms) under their licensing terms.

---

## Author

Developed by **Austin Bell**  
_For inquiries or contributions, feel free to open a pull request or contact via GitHub._
