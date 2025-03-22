# Flask To-Do List

A simple To-Do List web application built using Flask and SQLAlchemy for task management.

## Features
- Add new tasks with a title and description
- View all tasks
- Update existing tasks
- Delete tasks

## Technologies Used
- Python
- Flask
- SQLAlchemy (SQLite Database)
- HTML, CSS (for frontend rendering)

## Installation and Setup

### Prerequisites
Ensure you have Python installed on your system. You can check by running:
```sh
python --version
```

### 1️⃣ Clone the Repository
```sh
git clone <repository_url>
cd <repository_folder>
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
If `requirements.txt` is not available, manually install Flask and SQLAlchemy:
```sh
pip install flask flask_sqlalchemy
```

### 4️⃣ Run the Application
```sh
python app.py
```
The application will run on `http://127.0.0.1:8000/`.

## Project Structure
```
├── app.py          # Main Flask application
├── templates/      # HTML templates
│   ├── index.html  # Main To-Do List page
│   ├── update.html # Update task page
├── todo.db         # SQLite database (auto-created)
└── static/         # CSS and JS files (if any)
```

## Routes and Functionality
| Route | Method | Description |
|--------|--------|--------------------------|
| `/` | GET, POST | Displays all tasks, allows adding new ones |
| `/show` | GET | Shows all tasks in text format |
| `/update/<sno>` | GET, POST | Updates a specific task |
| `/delete/<sno>` | GET | Deletes a specific task |

## working

<img src="/working1.png" alt="adding" width="500" height="300">
<img src="/working2.png" alt="adding" width="500" height="300">
<img src="/working3.png" alt="adding" width="500" height="300">

## License
This project is licensed under the MIT License.

## Contributions
Feel free to fork this repository and improve the project by submitting pull requests!

