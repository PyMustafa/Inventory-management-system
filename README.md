# Inventory-management-system


## Setup Instructions

### Using the .env File

1. Copy the `.env.example` file to create a new `.env` file: 
    
   ```sh
   # For Linux/MacOS
   cp .env.example .env
   ```
    or just copy the file manually if you are on Windows.


2. Open the `.env` file and update the required environment variables with your specific configuration.

### Using Poetry

1. Install Poetry if you haven't already:=
   ```sh
    # For Linux/MacOS
   curl -sSL https://install.python-poetry.org | python3 -
   ```
    for Windows users, you can follow the instructions on the [Poetry installation page](https://python-poetry.org/docs/#installation).

2. Create & activate virtual environment.
   Using poetry shell (the easiest way)
    - Install the Shell Plugin
        ```sh
        poetry self add poetry-plugin-shell
        ```
    - Activate the virtual environment.
        ```sh
        poetry shell
        ```
       Or you can use your preferred virtual environment manager (like `venv` or `virtualenv`) to create a virtual environment and activate it.
    

3. Install the project dependencies using Poetry:
   ```sh
   poetry install
   ```

4. start the server
   ```sh
   python manage.py runserver
   ```
