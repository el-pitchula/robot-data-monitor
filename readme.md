<h1 align="center">RoboMonitor: Software Architecture for Robotic Data Monitoring</h1>

<div align="center">
  <strong>🤖 Monitoring and Control System for a Robot with an Attached Weapon 🎯</strong>
</div>

<div align="center">
  <p>robotics, data monitoring, software architecture, API documentation, Postman</p>
</div>

## 📖 Index

- [Overview](#overview)
- [Technologies](#technologies)
- [Environment Setup](#environment-setup)
- [How to Contribute](#how-to-contribute)

## 🔭 Overview

The Robot API project is designed to manage and interact with robotic systems, providing functionalities for monitoring robot statuses and managing user data. It aims to facilitate seamless integration and control of robotic operations through a RESTful API. This repository includes essential endpoints for retrieving robot data, updating statuses, and managing user information.

Key Features:
- Retrieve detailed information about individual robots.
- Update the operational status of robots (e.g., activate, deactivate).
- Manage user profiles and access permissions within the system.

This repository serves as a foundation for developing applications that interface with robotic systems, offering flexibility and scalability for various robotic applications.

## 💻 Technologies

- Front-end: HTML, CSS, JavaScript
- Back-end: Python, Flask
- Database: SQLite
- Cloud: AWS (Amazon Web Services)

[![Tech Icons](https://skillicons.dev/icons?i=html,css,js,python,flask,sqlite,aws)](https://skillicons.dev)

- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/doc/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLite](https://www.sqlite.org/docs.html)
- [AWS](https://aws.amazon.com/documentation/)

## ⚙️ Environment Setup

To set up the environment locally for development, follow these steps:

1. **Prerequisites**:
   - Install Python (version 3.7 or higher): [Python Installation Guide](https://www.python.org/downloads/)
   - Set up a virtual environment (optional but recommended): 
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```

2. **Installation of Dependencies**:
   - Install Flask and other dependencies:
     ```bash
     pip install flask
     ```

3. **Configuration**:
   - Set up environment variables if necessary.
   - Configure the database settings in `config.py`.

4. **Running the Application**:
   - Start the Flask server:
     ```bash
     flask run
     ```
   - Access the application at `http://localhost:5000`.

## How to Contribute

If you want to contribute to the project, follow these steps:

1. Fork the repository and clone it to your local machine.

2. Create a new branch for your modifications:
   ```bash
   git checkout -b my-branch
