# Inventory-management-system

## Description

This Inventory Management System is designed and developed as part of my ITI Full-Stack Python Training Journey, to streamline warehouse operations, track inventory and products, manage shipments and orders, and provide real-time analytics. This full-stack application is built with Python (Django) for the backend and HTML, CSS, JavaScript, and Bootstrap for a responsive and intuitive user interface. The system handles everything from user authentication and role management to order processing and real-time inventory tracking.
![image](https://github.com/user-attachments/assets/bd7099c9-3749-4a8f-bf85-cee8ef005ca1)

## Features

- User authentication and role management
- Email verification at registeration and reseting password
- Real-time inventory tracking
- Order processing and management
- Product and inventory management
- Shipment tracking
- Real-time analytics and reporting
- Responsive and intuitive user interface

## Technologies Used

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **Database:** PostgreSQL
- **Version Control:** Git, GitHub
- **Project Management:** Trello

## Demo

🔗 Check out the live demo:
https://web-production-f2a6e.up.railway.app/

use these credentials:
- **Username:** hassan
- **password:** Uyn6ZqvkiIO2
- **Role:** Manager

Note: In the live demo, we have removed the ability for the manager to add or edit products, similar to the employee role. This was done to prevent any inappropriate photos from being added as products.


## Database Design
![image](https://github.com/user-attachments/assets/1ce6475e-773a-4cc9-b7fe-27611d77dc00)

📌 Check the Database Design:
https://dbdiagram.io/d/ims_db_diagram-67d048da75d75cc844acb703

## Setup Instructions

### Using the .env File

1. Copy the `.env.example` file to create a new `.env` file:

   ```sh
   # For Linux/MacOS
   cp .env.example .env

## Setup Instructions

### Using the .env File

1. Copy the `.env.example` file to create a new `.env` file:

   ```sh
   # For Linux/MacOS
   cp .env.example .env
   ```
   or just copy the file manually if you are on Windows.


2. Open the `.env` file and update the required environment variables with your specific configuration.

### Option 1: Using Poetry

1. Install Poetry if you haven't already:
   ```sh
    # For Linux/MacOS
   curl -sSL https://install.python-poetry.org | python3 -
   ```
   for Windows users, you can follow the instructions on
   the [Poetry installation page](https://python-poetry.org/docs/#installation).

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
      Or you can use your preferred virtual environment manager (like `venv` or `virtualenv`) to create a virtual
      environment and activate it.


3. Install the project dependencies using Poetry:
   ```sh
   poetry install --no-root
   #or
   poetry sync
   ```

### Option 2: Using requirements.txt

1. Create and activate a virtual environment:
   ```sh
   # For Linux/MacOS
   python -m venv venv
   source venv/bin/activate
   
   # For Windows
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies from requirements.txt:
   ```sh
   pip install -r requirements.txt
   ```

### Starting the Server

After setting up using either option above:

1. Make sure you have the required database set up (in this case its PostgreSQL).
2. Run the following commands to create a superuser so you can access the system:

```sh
python manage.py createsuperuser
```

3. Run the following commands to apply migrations and start the server:

```sh
# Apply migrations
python manage.py migrate
python manage.py runserver
```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## Contact

For any questions or inquiries, feel free to contact me at:
- Email: [developer.mustafa@outlook.com](developer.mustafa@outlook.com)
- LinkedIn: [Mustafa Said Hassan](https://www.linkedin.com/in/mustafaahassan/)
