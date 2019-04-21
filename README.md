# Simon's Cookbook

Mission statement for project: "Create a web application that allows users to store and easily access cooking recipes.""

## Project guidelines

Put some effort into designing a database schema based on recipes, and any other related properties and entities (e.g. views, upvotes, ingredients, recipe authors, allergens, author’s country of origin, cuisine etc…). Make sure to put some thought into the relationships between them, and use either foreign keys (in the case of a relational database) or nesting (in the case of a document store) to connect these pieces of data
Create the backend code and frontend form to allow users to add new recipes to the site (at least a basic one, if you haven’t taken the frontend course)
Create the backend code to group and summarise the recipes on the site, based on their attributes such as cuisine, country of origin, allergens, ingredients, etc. and a frontend page to show this summary, and make the categories clickable to drill down into a filtered view based on that category. This frontend page can be as simple or as complex as you’d like; you can use a Python library such as matplotlib, or a JS library such as d3/dc (that you learned about if you took the frontend modules) for visualisation
Create the backend code to retrieve a list of recipes, filtered based on various criteria (e.g. allergens, cuisine, etc…) and order them based on some reasonable aspect (e.g. number of views or upvotes). Create a frontend page to display these, and to show some summary statistics around the list (e.g. number of matching recipes, number of new recipes. Optionally, add support for pagination, when the number of results is large
Create a detailed view for each recipes, that would just show all attributes for that recipe, and the full preparation instructions
Allow for editing and deleting of the recipe records, either on separate pages, or built into the list/detail pages
 
## UX and Design
 
The user interface has been design to be contrasting and simple to read and use. I have used bold colours to make the information and buttons stand-out on a plain white background which should be easily readable for all capable users on any device.
The font is simplistic and the styling of the content area is centred on the screen to make the site easily responsive on any screen size.
The buttons and functions are clearly labelled with plain text and relatable icons to help aid the users understanding of what each part of the site does.
The navbar also has few options to keep things as simple as possible.

## Features and functions

The features of the app are simple and easy to use:

1. View a list of all recipes in the cookbook.
2. Filter recipes through different categories.
3. Add new recipes.
4. Edit existing recipes.
5. Delete existing recipes.


## Technologies Used

In this section, you should mention all of the languages, frameworks, libraries, and any other tools that you have used to construct this project. For each, provide its name, a link to its official site and a short sentence of why it was used.

- [Materialize](https://materializecss.com/)
    - The project uses **Materialize** to simplify DOM manipulation, and provide structural and styling templates.
- [MongoDB](https://cloud.mongodb.com)
    - This project uses **MongoDB** to create and manage the database used to store the recipe information.
- [Cloud9](https://c9.io/)
    - This project was written with and terminalised through **Cloud9**, to host the code files and use the bash console asa command line interface(CLI)
- [Heroku](https://www.heroku.com/home)
    - This project was deployed to an application using the **Heroku** deployment interface.
- [GitHub](https://github.com)
    - The code for this project is publically accessible through **GitHub**.


## Testing

For the testing phase I used my own desktop PC with various browsers and my android smartphone.
 
I tested the responsiveness of the design by re-sizing the browser windows on the desktop as one of my challenges I faced was ensuring that the textareas for the ingredients and method of each recipe was large enough and still scrollable for varying amount of information.
 
I used the criteria below:

Browser | Navbar Buttons | Adding Recipes | Editing Recipes | Deleting Recipes | Viewing category list
--- | --- | --- | --- | --- | ---
**Chrome** | Yes | Yes | Yes | Yes | Yes | Yes 
**Firefox** | Yes | Yes | Yes | Yes | Yes | Yes 
**Edge** | Yes | Yes | Yes | Yes | Yes | Yes 
**Opera** | Yes | Yes | Yes | Yes | Yes | Yes 
**Safari** | Yes | Yes | Yes | Yes | Yes | Yes 
**Mobile** | Yes | Yes | Yes | Yes | Yes | Yes


## Deployment

This project was deployed using **Heroku** from the master branch. As of writing this file, there is no difference between the development and deployed version of this project. In order to deploy this project through Heroku, I first had to create the Heroku app on their website. Then, through the terminal, I used `Heroku login ` to connect my Cloud9 environment with Heroku. After entering my credentials I used Heroku apps to check that my recipe app was there. I then pushed the project to Heroku using `git push Heroku master `. I then used `heroku ps:scale web=1` to start the Heroku app.

Once I had these settings in place, I went to the Heroku app and configured and set the **IP (0.0.0.0)** and **PORT (5000)**. Once this was finished I clicked the ‘Open App’ button and my project was officially deployed.

To run this code locally, you may clone this repository from the **Clone or Download** button at the top of the page and write `git clone` followed by the cloned URL into an editor of your choosing. To cut ties with GitHub, use git remote rm origin in the terminal.

# Author

[Simon Law](https://github.com/SimonLaw21)


