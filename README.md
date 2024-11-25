# Flask Todo App 📝

A simple and interactive Todo application built using Flask. This app allows users to manage their tasks with features like creating, updating, deleting, and toggling tasks as completed.

---

## Features 🌟

- ✅ Add new tasks with a user-friendly interface.
- ✔️ Mark tasks as completed or uncompleted.
- ✏️ Edit tasks directly within the app.
- 🗑️ Delete tasks when no longer needed.
- 📱 Responsive UI using [Semantic UI](https://semantic-ui.com/).

---

## Getting Started 🚀

Follow these instructions to set up and run the project locally on your machine.

### Prerequisites 🛠️

Ensure you have the following installed:

- Python 3.8+
- Flask
- A virtual environment tool (e.g., `venv` or `virtualenv`)

### Installation ⚙️

1. Clone the repository:

    ```bash
    git clone https://github.com/whdev36/flask-todo.git
    cd flask-todo
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On Mac/Linux
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:

    ```bash
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

---

## Running the Application 🎉

1. Start the Flask development server:

    ```bash
    flask run
    ```

2. Open your browser and navigate to:

    ```
    http://127.0.0.1:5000/
    ```

---

## Project Structure 🏗️

```plaintext
flask-todo/
├── app/
│   ├── __init__.py         # Application initialization
│   ├── models.py           # Database models
│   ├── forms.py            # Forms for task creation and updates
│   ├── static/             # Static files (CSS, JS, Images)
│   ├── templates/          # HTML templates
│   └── views.py            # Routes for the application
├── migrations/             # Database migrations
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## Built With 🛠️

- [Flask](https://flask.palletsprojects.com/) - Web framework
- [Semantic UI](https://semantic-ui.com/) - Frontend framework

---

## Contributing 🤝

Feel free to contribute to the project by creating issues or submitting pull requests. Contributions are always welcome!

---

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments 🙏

- Thanks to [Semantic UI](https://semantic-ui.com/) for the great UI framework.
- Inspired by various Flask tutorials.
