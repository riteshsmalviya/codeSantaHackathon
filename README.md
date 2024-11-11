# CodeSanta

**CodeSanta** is a simple Django-based web application designed to allow users to upload and search for code snippets. It is an introductory-level project that demonstrates basic Django functionality such as file upload and search features. This application does not include user authentication, code execution, or any advanced features. It serves as a lightweight platform for storing and discovering code.

## Features
- **Code Upload**: Users can upload code files in various programming languages (e.g., Python, Java, C++).
- **Code Search**: Users can search for uploaded code snippets by keywords or file names.
- **Simple Interface**: The application features a basic user interface using HTML and Bootstrap for styling.

## Tech Stack
- **Backend**: Django (Python)
- **Database**: SQLite (used by default in Django for simplicity)
- **Frontend**: HTML, CSS, Bootstrap
- **File Handling**: Basic file upload functionality using Django’s built-in features.

## Project Purpose
The primary goal of **CodeSanta** is to showcase basic web development skills using Django. The project was built to demonstrate:
- Handling file uploads.
- Implementing a simple search feature.
- Managing code snippets in a database.

## Key Features Implemented
- **File Upload**: Code files are uploaded to the server and stored in the database.
- **Search Functionality**: Users can search for code snippets by filename or keyword, making it easier to find specific pieces of code.

## Future Enhancements
While the current version of **CodeSanta** is basic, some possible enhancements include:
- **Authentication**: Allow users to register and log in to manage their own uploaded code.
- **Code Execution**: Integrate a code execution engine to allow users to run uploaded code directly from the platform.
- **User Profiles**: Add the ability for users to manage and save their own uploaded code snippets.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Set up a virtual environment:
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```
6. Access the app via `http://127.0.0.1:8000/`.

---
