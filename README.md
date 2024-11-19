# online-shop-ADAO
This project is a Django-based e-commerce web application for a small online store. Users can browse products, add them to their cart, mark products as favorites, manage their profile, and place orders. It includes features for user authentication, personalized dashboards, and dynamic content management.

Features

User Management:
Register, login, and logout functionalities.
Profile management with additional fields (e.g., address, phone number).

Product Management:
Products categorized as Candles and Clay.
Each product has a name, description, price, category, and optional image.

Cart:
Add products to the cart.
Adjust product quantities and remove items.
View the contents of the cart.

Favorites:
Add products to favorites.
View and remove favorite products.

Dashboard:
View personalized information for authenticated users.

Pages:
Home, Products, About, Contact, and Profile pages.
Responsive navigation and active state indicators.

Installation and Setup
Prerequisites
Python 3.7+
Django 4.x
A virtual environment is recommended (e.g., venv).
Steps to Run Locally

Clone the Repository:
https://github.com/anageguchadze/online-shop-ADAO.git

Set Up Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run Migrations:
python manage.py makemigrations
python manage.py migrate

Create a Superuser:
python manage.py createsuperuser

Start the Development Server:
python manage.py runserver

Access the Application:
Open your browser and navigate to http://127.0.0.1:8000.
File Structure
models.py: Defines database models (e.g., Product, UserProfile, Cart, Favourite).
views.py: Implements the core logic for user actions and page rendering.
urls.py: URL patterns for navigating the application.
templates/: Contains HTML templates for pages.
static/: Holds CSS, JavaScript, and image files.
Admin Panel Access
The application includes an admin interface for managing products and users.

Navigate to http://127.0.0.1:8000/admin.
Log in with the superuser credentials created during setup.
Future Enhancements
Integration of a payment gateway for order processing.
Support for product reviews and ratings.
Enhanced filtering and search for products.
Email notifications for order confirmations and updates.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contributions
Contributions are welcome! Feel free to open issues or submit pull requests.

