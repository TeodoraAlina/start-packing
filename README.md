# Smells Like Vacay - Your Ultimate Vacation Packing List

## Project Overview

- “Smells Like Vacay” is an innovative and user-friendly packing list application designed to simplify your vacation preparations. Powered by Django, this web-based application empowers users to effortlessly create and manage their packing lists, ensuring a stress-free and well-organized travel experience.
- Are you ready to experience hassle-free vacation packing? click [here](https://start-packing-6d194f35b54b.herokuapp.com/) to open the live website and embark on your adventures with “Smells Like Vacay”!

## Table of Contents

- [Smells Like Vacay - Your Ultimate Vacation Packing List](#smells-like-vacay---your-ultimate-vacation-packing-list)
  - [Project Overview](#project-overview)
  - [Table of Contents](#table-of-contents)
  - [UX](#ux)
    - [Project Goal](#project-goal)
    - [User Stories](#user-stories)
  - [Design Choices](#design-choices)
    - [Colors](#colors)
    - [Typography](#typography)
    - [Images/Icons](#imagesicons)
    - [Responsiveness](#responsiveness)
  - [Wireframes](#wireframes)
    - [Home Page](#home-page)
    - [Packing List App](#packing-list-app)
  - [Features/Structure](#featuresstructure)
    - [Navigation](#navigation)
    - [Home Page](#home-page-1)
    - [Packing List App](#packing-list-app-1)
    - [Add Packing List](#add-packing-list)
    - [Add Task](#add-task)
    - [Edit Packing List](#edit-packing-list)
    - [Sign Up](#sign-up)
    - [Login/Logout](#loginlogout)
    - [Error 404/403/500/405](#error-404403500405)
    - [Features for Future Development](#features-for-future-development)
  - [Testing](#testing)
  - [Validation Testing](#validation-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
    - [Automated Testing](#automated-testing)

## UX

### Project Goal

- The goal of the packing list application is to simplify and enhance the vacation preparation process for users by providing a user-friendly and efficient platform to create, manage, and organize packing lists. The project aims to streamline the packing experience, ensuring that users can easily plan and pack for their upcoming trips with confidence and ease.

### User Stories

- For users:

  1.  As a user, I can mark a task as completed so that I can keep track of my progress while packing for my vacation.
  2.  As a user, I can edit a task in my packing list to update the details or make corrections.
  3.  As a user, I can delete a task from my packing list if I decide not to include it in my vacation planning.
  4.  As a user, I can create multiple packing lists for different types of vacations or destinations to stay organized.
  5.  As a user, I can add a new task to my packing list so that I remember to pack all the essential items for my trip.
  6.  As a user, I can toggle the completion status of a task to easily visualize which items I've already packed.
  7.  As a user, I can view the created date of each packing list to keep track of when I planned for my vacations.
  8.  As a user, I can view the created date of each task to see when I added it to my packing list.
  9.  As a user, I can edit the title of my packing list to give it a specific name related to my vacation plans.
  10. As a user, I can view all my packing lists and tasks in a single page for a comprehensive overview of my vacation preparations.
  11. As a user, I can log in to my account to access my private packing lists and tasks securely.
  12. As a user, I can sign up for a new account to start using the “Smells Like Vacay” packing list application.
  13. As a user, I can log out of my account to ensure my packing lists are private and secure.

- For admin :

  14. As an admin, I can access a dashboard to manage all users packing lists and tasks for administrative purposes.
  15. As an admin, I can view and edit any packing list or task in the system for administrative oversight.
  16. As an admin, I can delete any packing list or task if necessary, ensuring data accuracy and relevance.

## Design Choices

### Colors

The color palette for the Smells Like Vacay project is carefully chosen to evoke a sense of vacation, adventure, and serenity. The primary colors used throughout the project are:

- **Coconut Brown (#cd8253)**: This warm brown color is used for main headings and essential elements, providing a comforting and welcoming feel to the website.

- **Turquoise (#20a8b7)**: The vibrant turquoise color is used for lead text, task headings, and other accent elements, adding a touch of excitement and playfulness.

- **Dark Gray (#4c4c4c)**: The dark gray color is used for regular paragraphs, maintaining readability and complementing the other color choices.

- **Soft Green (#7ebdaf)**: This soft green hue is used for primary buttons, offering a refreshing contrast to the background and invoking a feeling of nature.

### Typography

The font choices for the Smells Like Vacay project contribute to its overall aesthetic, ensuring a harmonious and legible reading experience. The selected fonts are:

- **Poppins**: This font is used for main headings (h1) throughout the project, creating a bold and stylish look that captures attention.

- **Roboto**: For regular paragraphs and essential texts, 'Roboto' is utilized to provide clarity and simplicity, enhancing readability.

### Images/Icons

The project uses captivating images and icons to enhance the user experience and align with the vacation theme:

- **Background Image**: The index page features a captivating beach image as the background, transporting users to a relaxing vacation setting.

- **Font Awesome Icons**: The project incorporates Font Awesome icons to add visual appeal and improve user interaction, like the beach umbrella icon in the navigation bar.

### Responsiveness

To ensure that users can access and use the app seamlessly across various devices, the project follows responsive design principles:

- **Viewport Settings**: The `<meta name="viewport">` tag is set to control the page's scaling and responsiveness, making it mobile-friendly.

- **Bootstrap Grid**: The Bootstrap grid system is utilized to create responsive layouts and adapt content to different screen sizes.

## Wireframes

### Home Page

<img width="636" alt="Home Page Desktop" src="images-for-readme/homepage-desktop.png">
<img width="300" alt="Home Page Desktop" src="images-for-readme/homepage-mobile.png">

### Packing List App

<img width="636" alt="Home Page Desktop" src="images-for-readme/packing-list-app-desktop.png">
<img width="300" alt="Home Page Desktop" src="images-for-readme/packing-list-app-mobile.png">

## Features/Structure

### Navigation

- The navigation bar provides easy access to different sections of the website, such as the home page and the packing list app.
- Users can quickly navigate to the "Packing List App", "Home", "Login", "Logout" and "Sign up" pages directly from the navigation bar.
- The navigation bar adjusts responsively for different screen sizes, ensuring a seamless user experience on various devices.

### Home Page

- The home page greets users with an inviting message and call-to-action button to start packing for their future vacation.
- Users can find a user-friendly interface with clear headings and lead text, making it easy to understand the purpose of the application.

### Packing List App

- The "Packing List App" page presents users with their existing packing lists and tasks in an organized manner.
- Each packing list is displayed with its creation date, providing users with a clear overview of their lists.
- Users can toggle the completion status of tasks, helping them track their progress efficiently.

### Add Packing List

- Users can add new packing lists through the "Add Packing List" page.
- The form allows users to input the list's title enhancing list organization.

### Add Task

- The "Add Task" page enables users to add new tasks to a specific packing list.
- Users can change the completion status of tasks.
- Users can select the packing list to associate the task with, providing context and structure to the tasks.

### Edit Packing List

- Users can edit the details of existing packing lists.
- Additionally, users can manage the tasks associated with each packing list through an editable formset.

### Sign Up

- The "Sign Up" page allows new users to create an account, granting them access to additional features such as private checklists and task management.

### Login/Logout

- The "Login" page enables registered users to log in and access their personalized packing lists.
- Users can easily log out from the navigation bar, securing their account information.

### Error 404/403/500/405

- The application includes custom error pages for various HTTP status codes (404, 403, 500, 405).
- Users will be presented with informative and user-friendly error pages in case they encounter any issues.

By incorporating these features and organizing the website with clear navigation and user-friendly interfaces, Smells Like Vacay becomes a reliable and efficient packing list application for users to manage their vacation preparations effortlessly.

### Features for Future Development

For future improvements, I plan to implement the following features:

1. **Blog App**: I aim to add a blog application where users can access valuable tips and tricks for creating efficient packing lists, ensuring a smoother and more organized travel experience.

2. **Enhanced User Experience**: I plan to optimize the user experience by allowing the forms for adding and editing tasks to appear directly on the packing list app. This improvement will eliminate the need for redirection to another page, making the process more seamless.

3. **Checkbox for Tasks**: Instead of using a toggle button, I will introduce checkboxes for tasks. This change will provide users with a more intuitive and visually appealing way to mark tasks as completed or incomplete.

By incorporating these features, I aim to enhance the overall usability and convenience of the Smells Like Vacay packing list application, making it an even more valuable tool for travelers to stay organized and well-prepared for their vacations.

## Testing

## Validation Testing

### HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the site. It was also used to validate the CSS. As the site is created with Django and utilises Django templating language within the HTML, I have checked the HTML by inspecting the page source and then running this through the validator. You can click each page to see the corresponding screenshot evidence.

| Page                                                            | Result |
| :-------------------------------------------------------------- | :----- |
| [Home Page](images-for-readme/w3c-homepage.png)                 | Pass   |
| [Packing List App](images-for-readme/w3c-packinglist-app.png)   | Pass   |
| [Add Packing List](images-for-readme/w3c-add-list.png)          | Pass   |
| [Add Task](images-for-readme/w3c-add-task.png)                  | Pass   |
| [Edit Packing List](images-for-readme/w3c-edit-packinglist.png) | Pass   |
| [Login](images-for-readme/w3c-login.png)                        | Pass   |
| [Logout](images-for-readme/w3c-logout.png)                      | Pass   |
| [Sign up](images-for-readme/w3c-signup.png)                     | Pass   |
| [Error 404](images-for-readme/w3c-error404.png)                 | Pass   |

### CSS

[W3C](https://jigsaw.w3.org/css-validator/#validate_by_input) was used to validate the CSS.

| File                                                  | Result |
| :---------------------------------------------------- | :----- |
| [static/css/style.css](images-for-readme/w3c-css.png) | Pass   |

### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

| File                                                        | Result |
| :---------------------------------------------------------- | :----- |
| [static/js/script.js](images-for-readme/jshint-test-js.png) | Pass   |

### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the python code.

| File                                                          | Result |
| :------------------------------------------------------------ | :----- |
| **Start-Packing**                                             |
| [stearpacking/urls.py](images-for-readme/pep8-urls.py.png)    | Pass   |
| **Packing List App**                                          |
| [packinglist/views.py](images-for-readme/pep8-views.py.png)   | Pass   |
| [packinglist/models.py](images-for-readme/pep8-models.py.png) | Pass   |
| [packinglist/forms.py](images-for-readme/pep8-forms.py.png)   | Pass   |
| [packinglist/admin.py](images-for-readme/pep8-admin.py.png)   | Pass   |

### Automated Testing

- [Django testing tools](https://docs.djangoproject.com/en/3.2/topics/testing/tools/) and Django TestCase was used to create automatic tests for Python files. A total of 25 tests were written for the following files:

  - [forms.py](https://github.com/TeodoraAlina/start-packing/blob/main/packinglist/forms.py) test file: [test_forms.py](https://github.com/TeodoraAlina/start-packing/blob/main/packinglist/test_forms.py)
  - [models.py](https://github.com/TeodoraAlina/start-packing/blob/main/packinglist/models.py) test file: [test_models.py](https://github.com/TeodoraAlina/start-packing/blob/main/packinglist/test_models.py)
  - [views.py](https://github.com/TeodoraAlina/start-packing/blob/main/packinglist/views.py) test file: [test_views.py](https://github.com/TeodoraAlina/start-packing/blob/main/packinglist/test_views.py)

- The Django's test reporting tool '[Coverage](https://coverage.readthedocs.io/en/7.2.7/)' was installed to show the percentage of Python code that's been covered by tests:
  ![Coverage report](images-for-readme/coverage-report.png)


## Lighthouse

#### Desktop Results

[Home Page](images-for-readme/lighthouse-homepage-desktop.png)
[Packing List App](images-for-readme/lighthouse-packinglist-app-desktop.png)

- Desktop performed well on all major pages of the site with minimal improvements needed.

#### Mobile Results

[Home Page](images-for-readme/lighthouse-homepage-mobile.png)
[Packing List App](images-for-readme/lighthouse-packinglist-app-mobile.png)

## Manual Testing

## User Stories and Test Results

| User Story                                                                                                      | Test                                                      | Result |
|---------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|--------|
| 1. As a user, I can mark a task as completed so that I can keep track of my progress while packing for my vacation.   | Create a task and mark it as completed.                   | Pass   |
| 2. As a user, I can edit a task in my packing list to update the details or make corrections.                  | Create a task, edit its details, and save the changes.    | Pass   |
| 3. As a user, I can delete a task from my packing list if I decide not to include it in my vacation planning.   | Create a task, then delete it from the list.              | Pass   |
| 4. As a user, I can create multiple packing lists for different types of vacations or destinations to stay organized. | Create multiple packing lists with different titles.     | Pass   |
| 5. As a user, I can add a new task to my packing list so that I remember to pack all the essential items for my trip. | Add a new task to the packing list.                      | Pass   |
| 6. As a user, I can toggle the completion status of a task to easily visualize which items I’ve already packed. | Create a task and toggle its completion status.           | Pass   |
| 7. As a user, I can view the created date of each packing list to keep track of when I planned for my vacations. | Create a packing list and check its created date.         | Pass   |
| 8. As a user, I can view the created date of each task to see when I added it to my packing list.             | Create a task and check its created date.                 | Pass   |
| 9. As a user, I can edit the title of my packing list to give it a specific name related to my vacation plans. | Create a packing list, edit its title, and save changes.  | Pass   |
| 10. As a user, I can view all my packing lists and tasks on a single page for a comprehensive overview of my vacation preparations. | Access the packing list page and verify all lists and tasks. | Pass   |
| 11. As a user, I can log in to my account to access my private packing lists and tasks securely.             | Log in with valid credentials and access private lists.   | Pass   |
| 12. As a user, I can sign up for a new account to start using the “Smells Like Vacay” packing list application. | Sign up with a new account and access the app's features. | Pass   |
| 13. As a user, I can log out of my account to ensure my packing lists are private and secure.               | Log out from the account and verify successful logout.    | Pass   |
| 14. As an admin, I can access a dashboard to manage all users’ packing lists and tasks for administrative purposes. | Access the admin dashboard and verify access to all data. | Pass   |
| 15. As an admin, I can view and edit any packing list or task in the system for administrative oversight. | Access the admin dashboard, view and edit data for users. | Pass   |
| 16. As an admin, I can delete any packing list or task if necessary, ensuring data accuracy and relevance. | Access the admin dashboard, delete data for users.        | Pass   |