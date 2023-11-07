# Devium
Devium (inspired by Devto and Medium) is a blogging web app where users can read articles related to programming, web development and technology in general.

Powered by an API written in Django REST Framework, users can create their accounts, login and post articles.

## Features
* Users can read articles anonymously
* Users can access a list of tags (categories) and articles related to each tag
* Users can register an account and login on the platform using an email and a password
* Registered users can access to their account details and edit them
* Registered users can create articles and edit / delete them
* Tags can also be created during article creation
* Admin users can delete users accounts

## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)  ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

## Installation
If you know how to manage virtual environments in Python skip to the step four. Otherwise, I recommend you use Pipenv for this process.

1) Install Pipenv globally using pip
   ```
   python pip install pipenv
   ```
   
2) Install the virtual environment using Pipenv
   ```
   pipenv install
   ```
   
3) Activate the virtual environment
   ```
   pipenv shell
   ```

4) Install the dependencies
   ```
   pip install -r requirements.txt
   ```

5) Run the Django server
   ```
   python manage.py runserver
   ```
  
**Note**: If you have Make installed on your system, you can also use a shorter version of the above command by typing:
  ```
  make runserverdev
  ```

## Psycopg2 library error
Since this project is intended to be served in production I used the psycopg2 library to connect to a PostgreSQL database. 

If you have troubles installing this library, make sure you have the libpq-dev package installed on your system. Otherwise install it with this command (for Ubuntu / Linux Mint):

```
sudo apt-get install libpq-dev
```

If you still have issues, other possible solution is to replace the psycopg2 library with psycopg2-binary in the requirements file.


##  Environment variables
In order to run this project on your local environment, you'll have to set the proper environment variables. Make sure you're not adding spaces between the variable, the assignment operator and the value.

To run the project:
```
DEBUG=True
```
```
SECRET_KEY=yourdjangosecretkeyhere
```
```
ALLOWED_HOSTS=listofallowedhostshere
```

**Note**: If you need to generate a secret key, check this [article](https://codinggear.blog/django-generate-secret-key/#generate-secret-key-in-django-using-getrandomsecretkeynbspfunction)

This one is only needed if you're using the production settings file located in 'blog/config/settings/prod.py' when running the Django server:

```
DATABASE_URL=yourdatabaseurlhere
```

You can also find them on the ".env.dist" file on this very repository.

## API Endpoints
These are the endpoints and actions you can perform.
<h3>Auth APP</h3>

Create an account:</br>
_/auth/signup/_

Login:</br>
_/auth/login/_

Logout:</br>
_/auth/logout/_

<h3>Users App</h3>

List of users:</br>
_/users/list/_

User details:</br>
_/users/detail/id_

Update user information (only authorized for account owner):</br>
_/users/update/id_

Delete user account (only authorized for account owner and admin users):</br>
_/users/delete/id_

<h3>Blogging App</h3>

List of posts:</br>
_/blog/posts/_

Create a post (only for registered users):</br>
_/blog/add/_

Post details (author, creation date, etc):</br>
_/blog/posts/detail/id_

Edit a post (only for the author of the post):</br>
_/blog/posts/detail/id/update_

List of tags with every post associated with each tag:</br>
_/blog/tags/_

## Work In Progress
These are the features and improvements I intend to add to this project in the coming weeks.

* Add a versioning system using the djangorestframework-versioning library
* Add API documentation on Swagger UI using the drf-spectacular library
* Allow users to add an account picture hosted in Cloudinary
* Allow users to add an image to serve as a post/article banner
* Add a comment system for registered users in blog posts
* Add a reactions system based on emoji codes for every blog post

## Collaborations
If you want to add a frontend to this API or need help with installing and running this project on your local environment, feel free to contact me through my social media!

<a href="https://twitter.com/esvdev" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="esv343" height="30" width="40" /></a><a href="https://linkedin.com/in/eliassvelazquez/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="https://www.linkedin.com/in/eliassvelazquez/" height="30" width="40" /></a>
