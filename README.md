# django-rest-message

## Local Machine development setup
- Clone the repository on your machine 
    ```
    git clone https://github.com/yankit293/django-rest-message.git
    ```
    
- Install all dependencies by executing the following command:
    ```
    pip install -r dependency.txt

- Now open a terminal in that directory and run follwing commands:
 ```
    python manage.py createsuperuser
    # follow further instruction there
    
    - After super user is created 
    python manage.py makemigrations
    python manage.py migrate
    
    python manage.py runserver
    ```
- Now server will start at - http://127.0.0.1:8000/