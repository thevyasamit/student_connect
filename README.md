# Student Connect - Faculty Office Hours Management System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.0.1-green)

## Overview

Student Connect is an open-source web application designed to help university students easily access and manage faculty office hours information. This project was developed using publicly available university data and can serve as an excellent undergraduate project for students interested in web development, database management, and user interface design.

## Features

- User authentication system (register/login)
- Faculty office hours information display
- Search and filter faculty by various parameters
- Responsive web interface
- Docker support for easy deployment
- Database management with SQLAlchemy

## Technology Stack

- **Backend**: Python, Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Authentication**: Flask-Login
- **Containerization**: Docker

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Docker (optional, for containerized deployment)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/student_connect.git
cd student_connect
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Initialize the database:
```bash
python app.py
```

## Docker Deployment

To run the application using Docker:

```bash
docker build -t student_connect .
docker run -p 5000:5000 student_connect
```

## Project Structure

```
student_connect/
├── proftimeWebApp/
│   ├── static/          # CSS, JavaScript, and other static files
│   ├── templates/       # HTML templates
│   ├── __init__.py     # Application initialization
│   ├── models.py       # Database models
│   ├── routes.py       # Application routes
│   └── cseDeptData.csv # Sample faculty data
├── app.py              # Main application entry point
├── requirements.txt    # Python dependencies
└── Dockerfile         # Docker configuration
```

## Contributing

This is an open-source project and contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data sourced from publicly available university information
- Built with Flask web framework
- Inspired by the need for better faculty-student communication

## Contact

For any queries or suggestions, please open an issue in the GitHub repository.
