# Login-Logout-Registration
Django User Authentication Application
This is a simple Django application that provides a basic user authentication system. It includes the following features:

User Signup: Allows new users to create an account with a username, email, and password. It checks for existing usernames and ensures passwords match.
User Login: Enables existing users to log in with their username and password, redirecting them to the home page upon successful authentication.
User Logout: Logged-in users can log out, which redirects them to the login page.
Home Page: A protected page that only logged-in users can access. It includes a logout button for users to sign out.
Key Files:
urls.py: Maps URL patterns to the corresponding view functions for signup, login, logout, and the home page.
views.py: Contains the logic for user registration, authentication, logout, and rendering the home page.
signup.html: Template for the user signup page.
login.html: Template for the user login page.
home.html: Template for the home page, accessible only to logged-in users.
