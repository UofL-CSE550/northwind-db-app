<h1 align="center">
    How to Clone and Run Northwind Web Application
</h1>

## 1. Clone the repository
    git clone https://github.com/UofL-CSE550/northwind-db-app.git

##### Note: Open the cloned project in VS Code or any other Text Editor, then open the integrated terminate of your Text Editor or IDE

## 2. Create your own virtual environment
Virtual environments are where dependencies are stored, 
similar to node_modules in JavaScript. 
Every time you start your machine, 
you must activate the virtual environment using source venv/bin/activate.

#### Windows

    python -m venv venv 

#### Mac OS

    python3 -m venv venv

#### Activate the Virtual Environment in Windows Users
    venv\Scripts\activate 

#### Activate the Virtual Environment in Mac OS users
    source venv/bin/activate

## 3. Install your requirements
    pip install -r requirements.txt

## 4. Create a .env file
Create the .env file under "northwindDjango" directory and set the following parameter:

    SECRET_KEY=
    DB_HOST=
    DB_PORT=
    DB_NAME=
    DB_USER=
    DB_PASS=

Run the below git command to remove the file from git 
tracking if the .env file is tracked by git.

    git rm --cached .\northwindDjango\.env

If the above parameter are set, you won't be able to connect to the database

## 5. Database
#### Make sure you connected to UofL VPN to access the database

## 6. Make Migrations (Optional)
Run the below command only if you're connected to your localhost database

    python manage.py makemigrations
    python manage.py migrate

#### Note: Don't run the migrations command when connect to UofL database server through VPN.

## 7. Create a new superuser (Optional)
    python manage.py createsuperuser
Run the above command to create a super-user and follow the prompt.

#### Note: Don't run the migrations command when connect to UofL database server through VPN.

## 8. Run the application
    python manage.py runserver 8083

<h3 align="center">Thank you</h3>
    