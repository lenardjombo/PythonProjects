R Web Compiler
Overview

The R Web Compiler is a web application that allows users to write, compile, and execute R code directly in their web browsers. It provides an online platform for learning and practicing R programming without the need for local R installations.
Features

    Write and execute R code in real-time.
    View console output and errors directly in the browser.
    Save code snippets using local storage(client-side storage mechanism).
    Responsive design for use on desktop and mobile devices.
    Admin site to manage users accounts(deletion).
    Users must have accounts

Technologies Used

    Backend: Python, Flask,SQLAlchemy
    Frontend: HTML, CSS, JavaScript
    Storage: LocalStorage for saving user code snippets

Getting Started
Prerequisites

    Python (latest version)
    Flask (latest version)
    Modern web browser (Chrome, Firefox, Safari, etc.)

Installation

    Clone the repository: git clone https://github.com/lenardjombo/r-web-compiler.git
    Navigate into the project directory: cd r-web-compiler
    Install dependencies: pip install -r requirements.txt

Usage

    Start the Flask server: flask run
    Open your web browser and go to http://localhost:5000
    Write your R code in the editor.
    Click the "Run" button to execute the code.
    View the output and any errors in the console.

Demo

You can try a live demo of the R Web Compiler here (demo).
Contributing

We welcome contributions to improve the R Web Compiler. To contribute:

    Fork the repository.
    Create a new branch (git checkout -b feature/improvement)
    Make your changes and commit them (git commit -am 'Add new feature')
    Push to the branch (git push origin feature/improvement)
    Create a new Pull Request

License

This project is licensed under the MIT License - see the LICENSE.md file for details.
Contact

For any questions or support, please contact lenardjombo@gmail.com.
