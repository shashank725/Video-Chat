<h1 align="center">Videozz </h1>
<h4 align="center">A Video-Chat Application</h4>

<br>
<p align="center">
<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103"/> <br><br>
<a href="https://www.python.org/" target="blank"><img align="center" src="http://ForTheBadge.com/images/badges/made-with-python.svg" alt="python"/></a>
<a href="https://www.djangoproject.com/" target="blank"><img align="center" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="django" height="37" width="90"/></a>
</p>

### Project Setup :

Prerequisites
1. python3
2. pip3


3. Clone the project.

    ```shell
    git clone https://github.com/shashank725/Video-Chat.git
    ```
    

4. Create a virtual environment with venv (install virtualenv, if its not installed) inside the project floder.
  
    ```shell
    cd Videozz
    ```
  
   #### For Linux/Mac OSX
    ```shell
    sudo apt-get install python3-venv
    python3 -m venv env
    ```
  
   #### For Windows
    ```shell
    pip install virtualenv
    python -m venv env
    ```


5. Activate the virtual environemnt.

    #### For Linux/Mac OSX
    ```shell
    source env/bin/activate
    ```

    #### For Windows
    ```shell
    env\Scripts\activate
    ```
   
6. Install the requirements.

    ```shell
    pip install -r requirements.txt
    ```
 
7. Run the Migrations

    ```shell
    python manage.py makemigrations
    python manage.py migrate
    ```

8. Run the development server

    ```
    python manage.py runserver
    ```
9. Head to server http://127.0.0.1:8000
