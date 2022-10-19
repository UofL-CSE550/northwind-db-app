# Northwind Web Application
## 1. Clone the repository
    git clone https://github.com/UofL-CSE550/northwind-db-app.git
## 2. Create your own virtual environment
    python -m venv venv (python3 -m venv venv for mac os)
    (windows) venv\Scripts\activate or (mac os) source venv/bin/activate
Virtual environments are where dependencies are stored, similar to node_modules in JavaScript. Every time you start your machine, you must activate the virtual environment using source venv/bin/activate.

## 3. Install your requirements
    pip install -r requirements.txt

## 4. Database
#### Make sure you connected to UofL VPN to access the database

## 5. Make Migrations (Optional)
Run the below command only if you're connected to your localhost database

    python manage.py makemigrations
    python manage.py migrate

#### Note: Don't run the migrations command when connect to UofL database server through VPN.

## 6. Create a new superuser (Optional)
    python manage.py createsuperuser
Run the above command to create a super-user and follow the prompt.

#### Note: Don't run the migrations command when connect to UofL database server through VPN.

## 7. Run the application
    python manage.py runserver 8000
    