# FizzBuzz Flask App with Docker

A simple **FizzBuzz** web application built with **Flask** and containerized using **Docker**. 
This project serves as a test run of a Flask-based API with a front-end interface, all packaged in a Docker container for deployment.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)


## Installation

### Prerequisites

Make sure you have the following installed on your system:

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

### Clone the Repository

```bash
git clone https://github.com/manuw99/FizzBuzzDocker
cd FizzBuzzDocker
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

You can also set up the project in a virtual environment (optional):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### Run the Flask Application Locally

Once all dependencies are installed, you can run the Flask application:

```bash
python app.py
```

The application will be running at `http://127.0.0.1:5000`. You can test the FizzBuzz functionality by entering a number in the frontend.

### Dockerized Version

Steps for deployment of dockerized version.

#### Build the Docker Image

```bash
docker build -t fizzbuzz-app .
```

#### Run the Docker Container

```bash
docker run -d -p 5000:5000 fizzbuzz-app
```

The app will now be running at `http://localhost:5000`.

