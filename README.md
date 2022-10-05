# [Wine Yard](https://dashboard.heroku.com/apps/wine-yard)

Wineyard is an e-commerce site that hopes to provide a place for customers and wine enthusiasts to view a selection of wines. The site will provide functionalities to purchase products with delivery and a system for registered users to write reviews about individual wines to be displayed on the site. 


# UX
 
## Project Goals 

The primary goal of Wine Yard is to provide a clean and stylish site with easy navigation for consumers to purchase its products.

The target audience is of casual drinking adults (18+) and of a more experienced and knowledgeable wine consumer.

### User Goals:

- An attractive website to use
- A page to view all products
- A way to filter products
- A way to search for products
- A safe and secure way to purchase products
- A way to register and save information for future purchases
- Feedback and confirmations of the actions taken  
- Ability to write, edit and delete reviews

### Business Goals:

- A way to add products to the site
- A way to edit products
- A way to delete products
- A payment system to make a profit

### User Stories

As a customer I want:
1. A clean and simple website to look at 
2. A navigation bar to easily navigate the site
3. A page showing all products
4. A way to filter products
5. A page showing a products details
6. Images of products
7. A section of reviews of a product
8. The ability to write, edit or delete a review
9. Recognisable buttons and icons
10. An easy way to add products to basket
11. Feedback and confirmations of actions taken
12. A page to show basket and its contents
13. A way to edit or delete products in the basket
14. A simple checkout process
15. A safe and secure payment system
16. A confirmation and details of an order
17. The ability to register and save details for a faster checkout process

## Design Choices
The overall feel is of a simple, clean and stylish e-commerce site. The following design choices were made with this in mind:

**Fonts**
- The logo and headings font **Permanent Marker** was used for its bold and fashionable style

**Icons**
- Familiar and generic icons were used for understandability 

**Colours**
- The primary colours used were black, white and grey. Green was used for buttons. This was decided upon to draw the users attention to only the product images and buttons to Add to basket, View Basket, Checkout etc.

**Images**
- The hero image was used to provide a simple and stylish aspect to the site. Actual product images were used to give a legitimate and professional look and feel to the site.

## Structure

### Database Models
- [DrawSQL](https://https://drawsql.app/) was used to create visual diagram of the database models.
![Database models](media/drawSQL-wineyard.png)

### Wireframes
- These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.

# Features

## Existing Features

#### Navbar
- The navbar is a feature on every page.

- In **desktop view** The Wine Yard logo font features on the far left which links to the home page of the site.
- The search bar is featured at the centre top of the navbar, here users can search for their desired product.
- On the far right is the basket icon. Once a user has at least one item in their basket the icon will turn green and the grand total will appear beneath it. This works for registered as well as unregistered customers as all the information on which products users have added to basket is stored in their session data.
- To the left of the basket icon is the user account icon. A logged in user will see options to visit their profile or to logout. Whilst a logged out user will have options to register or login.
- Centered to the navbar and below the search bar there are a list of key website pages: Full Range, Wine, Champagne and Sparkling and Country.

- In **tablet and mobile view** the toggle button features on the far left which provides drop down links to the key website pages.
- On the far right is the search, account and basket icons. The search icon drops down to reveal a search bar for users to search for their desired product.

#### Footer
- The footer features on the home page
- It contains a contact email address, copyright information and links to Wine Yard social media pages.

### Home Page

#### Hero Image
- The home page hero image features repeating sketches of wine bottles, corkscrews and glasses of wine. This gives the user a sense of what the site is offering and provides a stylish backdrop.

#### Overlay 
- At the forefront of the image is an overlay which provides a sentence in the logo font explaining what the site is about, beneath this is a green button inviting user to shop now.

### Products Page
The products page utilises the same layout for all products and filtered products.

#### Heading
- Centered at the top of the products page is a header in the logo font informing the user of the page they are on, full range.

#### Links
- When filtered by wine, champagne or sparkling or country links provide the user with a visual confirmation of the product type they are viewing e.g White, Champagne or Argentina. If all wine category is chosen three links will appear for each wine type. These links will direct the user to a products page containing products with that specific wine attribute.

#### Number of Products
- At the far left of the page, below the header is a products number calculation. This shows how many products are available in the store, if a category is chosen the number will correspond to the number of products in this category.
- When filtered by search term the calculation will display the search term used by the user as well as the products number.

#### Cards
- Bootstrap cards are used to display each product on the page. They are styled to show one product per line on mobile screens, two on small screens, three on medium and four on larger screens.  
- Each card displays an image of the product which is a link to the products details page.
- The card features the product name, country of origin with corresponding image and price.

### Product Detail Page

- The product title, price, description and image and visible on the page, along with other specificities such as size of the product (cl), ABV (%) and country of origin with corresponding image of its flag styled as an icon. 
- A quantity bar is featured allowing the user to choose the amount of the product they would like which is capped at 99.
- Add to basket and keep browsing buttons add products to the basket and direct back to the products page respectively.

#### Toasts

- A succesful confirmation notification with a checkmark icon appears when the user adds an item to their basket, with details of the product name and a button to view basket.
- If more than one quantity of the product is added, the notification will display the number of that product added.

#### Reviews
Below the products details a review section lists reviews made by users. Each review is a card and is styled to show the rating out of five with star icon, the users chosen display name and review body.

- Logged in users will see a Add Review button which takes them to the add review page.
- If a user has created a review they will be able to see their review on the product details page with the option to edit or delete their review.
- Logged out users will not see a Add Review button, but a simple message inviting them to register or login to write a review
- If there are no reviews for a product a message stating that there are currently no reviews for this product will be displayed.

### Register/Sign Up Page

A user who is not logged in can create a new account using the sign up page. The form on this page includes an email address and email confirmation, username, password and password confirmation fields.

### Login/Sign In Page

The sign in page features a standard login form asking for username and password.
- Validation for this form is handled in the backend and relevant feedback is sent to the user when they sign in. 

### Profile Page

- The user profile page can only be accessed by a logged in user. Any user not logged in trying to access this page will be redirected to the sign in page.
- The default delivery information section allows the user to update their delivery information to be used in the checkout process.
- The Order History section details previous orders made by the user with details of the order number, date, items and order total. 

### Logout/Sign Out Page

The sign out page features a message to the user to confirm if they want to sign out then directs the user to the home page.

### Basket Page

- The basket page features a summary of all the products added.
- Each product is contained in a table with an image, product name, price and quantity. Here the quantity of items can be updated or product removed.
- The page featured a summary including the subtotal which is updated and displayed if a user alters the quantity of items in the basket, delivery cost which is calculated as 15% of their subtotal and the grand total which is a calculation of subtotal + delivery.
- Within the summary section there are buttons to direct the user to the checkout page or back to the products page.

### Checkout Page

- The checkout page features the order summary and number of items in the basket. Details of product name and quantity, product image, delivery cost and totals are displayed.
- The payment form on the page features fields for user details, delivery address and a stripe card number field. 
- If logged in the user can select a checkbox which will save their details which will be auto-filled for future purchases.
- The form uses Django's form validation and cross site request forgery protection.
- A loading overlay with a spinning icon is produced when user confirms payment. The user is then directed to the checkout success page.

### Checkout Success Page

- On checkout success a toast notification is produced confirming that the order was succesfully processed along with the order number and copy of users email address where a confirmation email will be sent to.
- The page displays all information of the order, users details, delivery address and billing info.

### Product Management Page
This page is available to superusers only.

- When logged in, a superuser can visit this page from the Profile toggler in the navbar.
- Here a superuser can fill out a form to add a new product to the site. The form includes category, name, description, price, size, country, abv, image url and image upload. 
- Each product added can be edited or deleted by the superuser. These buttons are located for each product on the products page and product detail.

## Features for Future Releases

1. Wine Yard Club
- I would like to introduce functionality where a user will be enticed to register in order to receive 10% discount on their orders. This will drive sales and profit for the company. 

2. User favourites
- For registered users, functionality to save products in order to return to the site and quickly find their favourite wines to purchase,

3. Additional payment methods
- A broader range of payment methods such as PayPal or Klarna where users can pay monthly useful for large orders.

# Technologies Used

## Tools

- [Django](https://www.djangoproject.com/) as python web framework for rapid development and clean design.
- [Stripe](https://stripe.com) as payment platform to validate and accept credit card payments securely.
- [AWS S3 Bucket](https://aws.amazon.com/) to store images entered into the database.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) to style django forms.
- [Django Countries](https://pypi.org/project/django-countries/) to provide country choices for use with forms.
- [Django allauth](https://django-allauth.readthedocs.io/en/latest/index.html) for account authentication, registration and management.
- [Gunicorn](https://pypi.org/project/gunicorn/) WSGI HTTP Server for UNIX to aid in deployment of the Django project to heroku.
- [Pillow](https://pillow.readthedocs.io/en/stable/) as python imaging library to aid in processing image files to store in database.
- [Psycopg2](https://pypi.org/project/psycopg2/) as PostgreSQL database adapter for Python.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://git-scm.com/) to handle version control.
- [GitHub](https://github.com/) to store and share all project code remotely.
- [Heroku](https://www.heroku.com/) for deployment. 
- [Balsamiq](https://balsamiq.com/) to create the wireframes for this project.
- [DrawSQL](https://drawsql.app/) to create the database diagram for this project.

## Databases

- [PostgreSQL](https://www.postgresql.org/) for production database.
- [SQlite3](https://www.sqlite.org/index.html) for development database, provided by django.

## Libraries

- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://fontawesome.com/) to provide icons.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.

## Languages

- This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing
Testing information can be found in seperate [TESTING.md](TESTING.md) file.

# Deployment 

## Run this project locally

To run this project the following must be installed on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Python 3](https://python.org/downloads/) 
- [Git](https://git-scm.com/)

To allow payment functionality ensure you have created a free account with [Stripe](https://dashboard.stripe.com/register).

### Installation

1. Clone the Github repo to the desired location on your computer.
   ```sh
   git clone git@github.com:shaun-davies/wine-yard.git
   cd wine-yard
   ```
2. Create and run a Python virtual environment in terminal.
   ```sh
   python3 -m venv env
   . env/bin/activate
   ```
3. Install the Python dependencies from `requirements.txt`.
   ```sh
   pip3 install -r requirements.txt
   ```
4. Create an `env.py` based on the `sample-env.py` file.
   - Create and add a [Django secret key](https://django-secret-key-generator.netlify.app/).

5. Make migrations to prepare the database. This will create a `db.sqlite3` in the root. Remove the flags when happy to proceed.
   ```sh
   python3 manage.py makemigrations --dry-run
   python3 manage.py migrate --plan
   ```
6. Create a new superuser.
   ```sh
   python3 manage.py createsuperuser
   ```
7. Run the site locally.
   ```sh
   python3 manage.py runserver
   ```

## Deploy to Heroku