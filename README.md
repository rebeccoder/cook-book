# The Vegan Cook Book

The Vegan Cook Book is an online resource for anyone interested in vegan recipes to have the opportunity to share and search for their favourite vegan recipes which they are then able to view, edit or delete if needs be.

## Table of contents

1. [UX](#ux)
    - [Goals](#goals)
        - [Project Goals](#project-goals)
        - [Visitor Goals](#visitor-goals)
    - [User Stories](#user-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)

2. [Features](#features)
    - [Existing Features](#exisiting-features)

3. [Information Architecture](#information-architecture)
    - [Database Choice](#design-choice)
    - [Data Storage](#data-storage)

4. [Technology Used](#technology-used)

5. [Testing](#testing)

6. [Deployment](#deployment)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)


## UX

### Visitor Goals

The main target audience for the website are as follows:

- Vegans
- People who are interested in the vegan diet
- People looking to transition to the vegan diet

The main user goals are:

- Provide a space for users to share their vegan recipes
- Allow the user to create, display, update and delete the recipes that they share
- Ensure all the recipes are displayed on the homepage
- Ensure that the user can only edit and delete their own recipe not anyone elses
- Provide a search bar so that the user can search for any recipes by name
- Each recipe having it's own page with all the instructions in one place

### User Stories

As a logged in user to the site I would like to be able to share my favourite recipes
As a logged in user to the site I want to be able to create, edit and delete my recipes
As a visitor to the site I want to be able to see all the recipes available in one place at a glance
As a vistor to the site I want to be able to click on individual recipes without needing to log in
As a visitor to the site I want to be able to see the recipes on my mobile phone

### Design Choices

#### Colours

To keep within the expected theme of a usual vegan website the main stand out colour I used was a light green on the nav bar and an even lighter green for the forms. 
The image I used for the background has avocado flesh on it (vegans loooove avocado) and the light green I've used is similar to that which I thought really complimented the background.
I also added a splash of orange to brighten the page.
The headers for each page are in black so that they are easy to see.
The text within the forms is currently in grey although I may change this in down the line.

hex code colours are as follows:

----colours hex code & colour chart here -----

### Fonts

After playing around with a few fonts I decided to go with Rajdhani from Google fonts.
Thicker fonts didn't suit the website very much, I liked Rajdhani font as it is minimal, tidy and clear. I also added a shadow to this font which subtly makes it pop out more.

### Styling

A lot of the styling came from the website Materialize such as the template cards, navbar and footer elements and was inspired by the Mini Project Tutorial by Code Institute.


## Wireframes

--- enter wireframes here ---

## Features

### Navigation bar

The navigation bar allows the user to easily browse through only the relevant pages when using the website. If the user is logged in then the navigation bar  only displays the Home, New Recipe and Log Out options. If the user is logged out however then it the only displays the Home, Register and Log In options.

### Home Page

The home page is accessible to anyone on the website whether they're logged in or not. This is where all the recipes are able to be seen at a glance, each recipe has an image, a title and a description with a link to the full recipe. 


### Full Recipe Page

Once the user has chosen which recipe they want to look at they are able to click on the link below it on the home page which will take them to a page displaying the full recipe. This includes a large image followed by the name and category of the dish, a list of any allergens, how many people it serves, cooking time and a list of all the ingredients, a step by step list of instructions and lastly the username of the person who created the recipe.

### Search Bar

I have included a search bar into the home page, users are able to search for recipes by name here. It also includes a reset button taking the user back to the home page so that they don't need to use the back button in their browser.

### User Accounts

There is an option to register an account on the website. 
Once the user has signed up their username gets saved to the database and their password gets encrypted so that their sensitive information is not sent to Mongo DB.

Although anyone is able to browse the website even if they're not logged in, users who have an account are then given access to add a new recipe to the cook book. 

The user is also given the option to log out on the navbar, if they choose to log out then they are redirected to the log in page as it makes it quicker to log back in if they logged out by mistake or are keeping the tab open to log back in later.


### Edit and Delete Functions

Once the user has added a new recipe there will be two buttons on the recipe displaying on the home page, one for edit and one for delete. The user is able to edit and delete their recipes at any time. The person logged in can only change recipes that were made with their account, users are not able to edit or delete any recipes created by other users.

### Flash Messages

This website uses flash messages to let the user know when they've logged in, logged out, created, edited or deleted a recipe. Flash messages are there to give a response to the user so that they know what they've tried to do is successful.


## Future Goals

- Once the website is recieving more traffic I would like to add the option to browse category pages. Birthdays, Chinese Food, Light Lunches... etc. that kind of thing. This would also involve adding more categories to the selector in the New Recipe form so users could determine what category their website fits in to.

- I would also like to increase the search functionality allowing user to refine their searches to filter out certain allergens or to search within certain cooking times etc.

- Create an option to download/send all ingredients to a shopping list via a preferred vendor

- Add a user profile so that the user can have a space for all of their own recipes where they can easily access to edit them.

## Technology Used
### Languages

- HTML
- CSS
- Javascript
- Python

### Tools

MongoDB (https://www.mongodb.com/)
Materialize (https://materializecss.com/)
Flask (https://flask.palletsprojects.com/en/2.2.x/)
jQuery (https://jquery.com/)
fontawesome (https://fontawesome.com/icons)

## Testing

### Validators

- All pages passed HTML Verification with [W3Validator](validator.w3.org)
- All pages passed CSS Verification with [W3Validator](jigswa.w3.org)
- CSS validator errors due to bootstrap.min.css, this is out of my control and an issue with the resource.
- User testing has been used throughout to ensure the website was responding as expected and intuitive to the user.


## UI

### Navigation
- Nav bar displays correctly on all pages
- Clicking each link on the navbar has the expected response
- *Log Out* logs the user out of their session returning them to Home
- Users without an account can not access the *New Recipe* page
- Users logged into a session are not given links for *Register* and *Log In* as they're not relevent

### Footer

- Each text element displays as expected in the correct position
- Footer links displayed for Facebook and Instagram both navigate to the websites as expected
- The links also open in new tabs, aria labels have been added to warn screen readers that they will be redirected to a new web page
- Copyright year is coded to always show the current year

### Add Recipe

- Link from nav bar correctly directs the user to the New Recipe Page
- Information input is required in all fields for the form to submit
- Data is sent to Mongo DB


### Edit Recipe

- Logged in user is able to see their recipes on the main recipe page where there is an edit button that redirects them to the edit form
- Information sudmitted in the *New Recipe* form is retrieved from MongoDB and is displayed in the edit form
- User is able to amend recipe and resubmit to MongoDB
- There is a flash message to confirm the recipe has been edited

### Delete Recipe

- Logged in user is able to see their recipes on the main recipe page where there is a delete button
- User is able to delete recipe from MongoDB and recipe page
- There is a flash message to confirm the recipe has been deleted

### Full Recipe

- All users are able to click link from main page to view recipe instructions
- A large image is displayed to users on navigating to page
- Information is displayed as expected
- The username of the person who created the recipe is displayed
- User cannot amend the recipe from this page even if logged in