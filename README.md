# Awaara
A Basic Travel website made for my first attempt at using Django framework with Log in and Log Out functionality.

As usual, every Django project has a manage.py file. This helps us to start the apps and view the website in the browser by going to the terminal and typing 'python manage.py runserver'

The vagabond folder consists of the meta files of the django project. In here, there are a few important files crucial to the functioning of the project.
- settings.py consists of the configurations such as root directory management, app management, database software management, etc.
- urls.py links all the folders together that need to be searched for different urls.

The templates folder consists of a bunch of HTML files that work as the webpage:
- index.html is the main home page where the user can select log in, log out after logging in, view different travel destinations, etc
- login.html is the page for an existing user to log in
- register.html is the page for new users to sign up
- payment.html and booking.html are unusable as of now since I need to figure out the logic part of that in my views.py of their respective apps.

static folder consists of a few image files, css files, javascript, and fonts. These are also copied to assets folder through a load command given in index.html and set up in settings.py

The booking folder is an app that is currently not functional.

The awaara folder is the main app that displays the main home page.
- urls.py consists of a path to the main page
- views.py renders the main page
- models.py consists of a class Destination and Review that helps us add more travel locations and customer reviews to the template through Django admin and PostgreSQL, PgAdmin
- admin.py registers both classes to the Django admin page
- The migration folder migrates the classes to SQL format in the PostgreSQL database.

The accounts folder is an app that maintains the logic of adding new users to the database, logging them in after verifying credentials and logging them out when they feel like.
- urls.py consists of paths to login and register views
- views.py consists of functions to figure the logic of logging in, registering and logging out

The entire project makes use of Django 3.1.3, PostgreSQL, and PgAdmin4. 
Images are brought from personal files, unsplash.com.

The template of the main webpage has been brought from https://templatemo.com/tm-475-holiday

Other tools used are HTML, CSS, Bootstrap Elements, jQuery, and front-end JS.
