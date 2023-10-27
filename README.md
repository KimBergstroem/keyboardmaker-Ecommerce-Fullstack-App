# Easy Keyboard Maker - Your Ultimate Keyboard Shopping Experience
        Keyboard enthusiast since ᴡɪɴᴅᴏᴡs 98.

Easy Keyboard Maker is a Django-based e-commerce application designed for keyboard enthusiasts. The project offers a comprehensive platform for buying and selling keyboards, including new, retail, exclusive, and limited-edition models. Users can also craft customized keyboards to suit their preferences.

The application is engineered for easy navigation and efficient shopping, providing a seamless experience for users. 

<center> 

![Mockup image](/docs/readme.md/readme-header.png) 

</center>


Developer: [Kim Bergström](https://github.com/KimBergstroem) <br>
[Live webpage]()<br>
[Project Repository](https://github.com/KimBergstroem/PP5)<br>


![GitHub Badge](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=for-the-badge)
![Gitpod Badge](https://img.shields.io/badge/Gitpod-FFAE33?logo=gitpod&logoColor=fff&style=for-the-badge)
![Git Badge](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=fff&style=for-the-badge)
![Heroku Badge](https://img.shields.io/badge/Heroku-430098?logo=heroku&logoColor=fff&style=for-the-badge)
![PostgreSQL Badge](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=for-the-badge)

![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=fff&style=for-the-badge)
![CSS3 Badge](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=fff&style=for-the-badge)
![JSS Badge](https://img.shields.io/badge/JSS-F7DF1E?logo=jss&logoColor=000&style=for-the-badge)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)
![Markdown Badge](https://img.shields.io/badge/Markdown-000?logo=markdown&logoColor=fff&style=for-the-badge)

![Bootstrap Badge](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=fff&style=for-the-badge)
![Django Badge](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=fff&style=for-the-badge)


## Table of Content

- 📄[Project Goals](#project-goals)
  + [User Goals](#user-goals)
  + [Site Owner Goals](#site-owner-goals)
- 📄[User Experience](#user-experience)
  + [Target Audience](#target-audience)
  + [User Requirements and Expectations](#user-requirements-and-expectations)
  + [User Stories](#user-stories)
    - [Epic 1: User Experience (Visitor)](#epic-1--user-experience--visitor-)
    - [Epic 2: User Engagement and Interaction (Registered User)](#epic-2--user-engagement-and-interaction--registered-user-)
    - [Epic 3: Administration and Content Management (Admin/Content Moderator)](#epic-3--administration-and-content-management--admin-content-moderator-)
- 📄[Database](#database)
  + [Blog Application Database Schema](#blog-application-database-schema)
    - [GameCategory Table](#gamecategory-table)
    - [UserProfile Table](#userprofile-table)
    - [User Table](#user-table)
    - [Post Table](#post-table)
    - [Comment Table](#comment-table)
- 📄[Design](#design)
  + [Design Choices](#design-choices)
  + [Color](#color)
  + [Fonts](#fonts)
  + [Structure](#structure)
    - [Before Logging In:](#before-logging-in-)
    - [After Logging In:](#after-logging-in-)
    - [Profile Navigation:](#profile-navigation-)
  + [Wireframes](#wireframes)
- 📄[Technologies Used](#technologies-used)
  + [Languages](#languages)
  + [Frameworks](#frameworks)
  + [Database](#database-1)
  + [Tools](#tools)
  + [Supporting Libraries and Packages](#supporting-libraries-and-packages)
- 📄[Methodology](#methodology)
  + [Agile Project Management with GitHub Projects](#agile-project-management-with-github-projects)
  + [User Stories as GitHub Issues](#user-stories-as-github-issues)
  + [Bug Tracking for Seamless Development](#bug-tracking-for-seamless-development)
  + [Iterative Development Approach](#iterative-development-approach)
  + [Future Backlog and Progress](#future-backlog-and-progress)
- 📄[Features](#features)
  + [Landing Page:](#landing-page-)
  + [Blog Pages:](#blog-pages-)
  + [Blog Detail Page:](#blog-detail-page-)
  + [User Account Management:](#user-account-management-)
  + [Navigation:](#navigation-)
  + [Future Features](#future-features)
- 📄[Testing](#testing)
- 📄[Bugs](#bugs)
  + [Known bugs](#known-bugs)
  + [Fixed bugs](#fixed-bugs)
- 📄[Deployment](#deployment)
  + [App Deployment](#app-deployment)
  + [Cloudinary](#cloudinary)
  + [Version Control](#version-control)
  + [Forking the Repository:](#forking-the-repository-)
  + [Clone of the Repository:](#clone-of-the-repository-)
- 📄[Credits](#credits)
  + [Media](#media)
  + [Django Documentation:](#django-documentation-)
  + [W3 Schools:](#w3-schools-)
  + [Bootstrap docs:](#bootstrap-docs-)
  + [Geeksforgeeks:](#geeksforgeeks-)
  + [Various tutorials and YouTube channels:](#various-tutorials-and-youtube-channels-)
  + [Content](#content)
- 📄[Acknowledgments](#acknowledgments)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc and modified by myself</a></i></small>

<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Project Goals 
Example text

- **example:** 


### User Goals
- Example

### Site Owner Goals
- Example

Text description

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# User Experience

### Target Audience
EasyKeyboardMaker is designed for the following target audience:

- Keyboard enthusiasts and individuals looking to purchase mechanical keyboards and accessories.
- Shoppers interested in exploring a variety of keyboard types, brands, and designs.
- Gamers, streamers, and developers who rely on keyboards as a key tool for their work or leisure.
- Users who want to easily browse, select, and purchase mechanical keyboards and related products.
- Individuals seeking a platform to stay updated with the latest keyboard trends and innovations.
- People interested in sharing their own product reviews, recommendations, and experiences.

### User Requirements and Expectations
When using the E-commerce EasyKeyboardMaker, users can expect the following features and characteristics to meet their needs:

- An intuitive and user-friendly interface for effortless navigation and product discovery.
- High-quality product listings, including detailed descriptions, specifications, and user reviews.
- Responsive design for an optimal shopping experience on various devices, including desktop and mobile.
- Personalized user profiles with order history, saved payment information, and preferences.
- Interactive features, such as product reviews, ratings.
- Updates and special promotions to keep users informed.

EasyKeyboardMaker is a e-commerce platform for users, including gamers, streamers, and developers, to explore, select, and purchase mechanical keyboards and accessories while staying updated with the latest trends.


### User Stories

#### **- SPRINT 1 -**

- [Set Up Project Skeleton](https://github.com/KimBergstroem/PP5/issues/1) 
- [Planning and Documentation](https://github.com/KimBergstroem/PP5/issues/2) 

#### **- SPRINT 2 -**
After completing sprint 2, the project will be ready for its initial demonstration, showcasing the Minimum Viable Product (MVP). This milestone will be reached two weeks after the start of development.

#### Epic 1: Viewing and Navigation (Shopper) [#3](https://github.com/KimBergstroem/PP5/issues/3)

- [Easy Product Browsing and Selection](https://github.com/KimBergstroem/PP5/issues/12) _(must-have)_
- [Detailed Product Information Viewing](https://github.com/KimBergstroem/PP5/issues/13) _(must-have)_
- [Quick Identification of Discounts and Special Offers](https://github.com/KimBergstroem/PP5/issues/14) _(must-have)_
- [Easy Access to Total Cost of Selected Items](https://github.com/KimBergstroem/PP5/issues/15) _(should-have)_   


#### Epic 2: Registration and User Accounts (Site User) [#4](https://github.com/KimBergstroem/PP5/issues/4)

- [Convenient User Registration](https://github.com/KimBergstroem/PP5/issues/16) _(must-have)_
- [Easy User Login and Logout](https://github.com/KimBergstroem/PP5/issues/17) _(must-have)_
- [Password Recovery for User Account Access](https://github.com/KimBergstroem/PP5/issues/18) _(must-have)_ 
- [Email Confirmation for Registration](https://github.com/KimBergstroem/PP5/issues/19) _(must-have)_

#### Epic 3: Sorting and Searching (Shopper) [#5](https://github.com/KimBergstroem/PP5/issues/5)

- [Product Sorting Options](https://github.com/KimBergstroem/PP5/issues/20) _(must-have)_
- [Category-Specific Product Sorting](https://github.com/KimBergstroem/PP5/issues/21) _(should-have)_
- [Product Search by Name or Description](https://github.com/KimBergstroem/PP5/issues/22) _(should-have)_
- [Search History and Result Count](https://github.com/KimBergstroem/PP5/issues/23) _(wont-have)_

#### **Epic 4**: Purchasing and Checkout (Shopper) [#6](https://github.com/KimBergstroem/PP5/issues/65)

- [Product Size and Quantity Selection](https://github.com/KimBergstroem/PP5/issues/24) _(should-have)_
- [Review Shopping Bag and Confirm Purchase](https://github.com/KimBergstroem/PP5/issues/25) _(must-have)_
- [Flexible Item Quantity Adjustment in Shopping Bag](https://github.com/KimBergstroem/PP5/issues/26) _(must-have)_

#### **- SPRINT 3 -**

#### Epic 4: Purchasing and Checkout (Shopper) [#6](https://github.com/KimBergstroem/PP5/issues/6) - Continued

- [User-Friendly Payment Information Entry and Swift Checkout](https://github.com/KimBergstroem/PP5/issues/27) _(must-have)_
- [Assurance of Personal and Payment Information Security](https://github.com/KimBergstroem/PP5/issues/28) _(should-have)_
- [Order Confirmation on Website](https://github.com/KimBergstroem/PP5/issues/29) _(must-have)_
- [Email Confirmation for Purchase Record](https://github.com/KimBergstroem/PP5/issues/30) _(should-have)_

#### Epic 5: Admin and Store Management (Store Owner) [#7](https://github.com/KimBergstroem/PP5/issues/7)

- [Add New Products to the Store](https://github.com/KimBergstroem/PP5/issues/31) _(must-have)_
- [Edit/Update Product Details](https://github.com/KimBergstroem/PP5/issues/32) _(must-have)_
- [Delete Products from the Store](https://github.com/KimBergstroem/PP5/issues/33) _(must-have)_  

#### Epic 6: User Profiles and Order History (Site User) [#8](https://github.com/KimBergstroem/PP5/issues/8)

- [Update User Profile Information](https://github.com/KimBergstroem/PP5/issues/34)  _(could-have)_
- [View Detailed Order History](https://github.com/KimBergstroem/PP5/issues/35)  _(could-have)_
- [Track Delivery Status of Current Orders](https://github.com/KimBergstroem/PP5/issues/36) _(wont-have)_
- [Order Confirmation Email with Shipment Details](https://github.com/KimBergstroem/PP5/issues/37) _(could-have)_


#### Epic 7: Product Reviews and Ratings (Site User) [#9](https://github.com/KimBergstroem/PP5/issues/9)

- [Read and Write Product Reviews](https://github.com/KimBergstroem/PP5/issues/38)  _(should-have)_
- [Rate Products and Provide Feedback](https://github.com/KimBergstroem/PP5/issues/39)  _(could-have)_
- [Sort and Filter Products by User Ratings and Reviews](https://github.com/KimBergstroem/PP5/issues/40)  _(could-have)_
- [Receive Review Notifications](https://github.com/KimBergstroem/PP5/issues/41)  _(wont-have)_


#### **- SPRINT 4 -**
After finishing sprint 4, the project will be presented as the finished product. During this presentation, there will also be introduce new features planned for future implementation.

#### Epic 8: Blog (Site Owner) [#10](https://github.com/KimBergstroem/PP5/issues/10)

- [Access to Blog Section for Reading](https://github.com/KimBergstroem/PP5/issues/42) _(should-have)_
- [Search and Filter Blog Posts by Topics](https://github.com/KimBergstroem/PP5/issues/43) _(could-have)_
- [Leave Comments on Blog Posts](https://github.com/KimBergstroem/PP5/issues/44) _(wont-have)_
- [Create, Edit, and Delete Blog Posts](https://github.com/KimBergstroem/PP5/issues/45)  _(must-have)_


#### Epic 9: SEO and Marketing (Site Owner) [#11](https://github.com/KimBergstroem/PP5/issues/11)

- [Optimize Website for Search Engines](https://github.com/KimBergstroem/PP5/issues/46) _(must-have)_
- [Share Product Pages and Blog Posts on Social Media](https://github.com/KimBergstroem/PP5/issues/47) _(could-have)_
- [Receive Email Newsletters](https://github.com/KimBergstroem/PP5/issues/48) _(could-have)_
- [Track Website Traffic and User Behavior](https://github.com/KimBergstroem/PP5/issues/49) _(could-have)_
---
- [Final Testing and Bug Fixes](https://github.com/KimBergstroem/PP5/issues/50) 
- [Final Documentation](https://github.com/KimBergstroem/PP5/issues/51)

<br>

The **38** user stories are implemented into **9** Epics and they are organized into **4** distinct sprints (milestones) to establish a well-defined work structure. You can access the details of these sprints by clicking [here](https://github.com/KimBergstroem/PP5/milestones), which will redirect you to the sprint information and find all the user stories and epics.

<p align="center">
  <img src="docs/readme.md/readme-Milstones.png" />
</p>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>


# Database
When creating the database structure schema for this project, I utilized the [dbdiagram.io](https://dbdiagram.io/) website. This online tool allowed me to visually design and document the database schema, making it easier to plan and implement the database for the e-commerce application.

<center> 

![Database Schema image](/docs/readme.md/readme-database_schema.png) 

</center>

### E-commerce Application Database Schema

#### Example Table
- Example


#### Example Table
- Example

#### Example Table
- Example

#### Example Table
- Example

#### Example Table
- Example

<br>
This database schema defines the structure and relationships for a e-commerce application, including "example of all tables here".

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Design
Text

### Design Choices
Text

### Color
Decision to adopt the 60-30-10 rule in our UI design is driven by its ability to create a cohesive and engaging user experience. This approach guarantees consistency by allocating 60% of our color palette to the dominant color, fostering brand recognition and trust. The 30% dedicated to the secondary color enables us to strike a visual balance, allowing for variations in content, headers, and backgrounds without overwhelming users. The remaining 10% allocated to the accent color serves to highlight interactive elements and calls to action, though we recommend choosing a contrasting shade for improved visibility and user engagement. This strategy ensures that our web application not only looks appealing but also functions effectively, guiding users to key elements while maintaining a harmonious and dependable design.

![Color Palette image](/docs/readme.md/readme-color-palette.png)
**Dominant (60%):** 

Text

**Secondary (30%):** 

Text

**Accent (10%):** 

Text


### Fonts
EasyKeyboard E-commerce embraces the default fonts offered by Bootstrap 5, without any specific alterations, as they significantly enhance the overall aesthetics and user experience.

### Structure

User-friendly structure, ensuring seamless navigation and easy access to the website's content. Here's an overview of the website's structure:

#### Before Logging In:

- **Example Page:** Text<br>
- **Example Page:** Text<br>
- **Example Page:** Text<br>
- **Example Page:** Text<br>


#### After Logging In:
Text

- **Example Page:** Text<br>
- **Example Page:** Text<br>
- **Example Page:** Text<br>
- **Example Page:** Text<br>

Text

#### Profile Navigation:

Text

- **Example Page:** Text<br>
- **Example Page:** Text<br>
- **Example Page:** Text<br>
- **Example Page:** Text<br>


### Wireframes
The wireframes serve as a visual blueprint for our web application, outlining the structure and functionality of each page. They provide a detailed representation of the user interface and overall user experience. These wireframes were meticulously crafted using Figma, a design tool renowned for its ability to facilitate rapid and intuitive prototyping. Click on each page to view the wireframe.

<details><summary>Example page</summary>
<img src="docs/wireframes/">
</details>
<details><summary>Example page</summary>
<img src="docs/wireframes/">
</details>
<details><summary>Example page</summary>
<img src="docs/wireframes/">
</details>
<details><summary>Example page</summary>
<img src="docs/wireframes/">
</details>
<details><summary>Example page</summary>
<img src="docs/wireframes/">
</details>
<details><summary>Example page</summary>
<img src="docs/wireframes/">
</details>

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Technologies Used

### Languages
- HTML
- CSS
- Python

### Frameworks
- Django: A high-level Python web framework used for building the Gamers Insight Blog web application.
- Crispy Forms: A Django package used for rendering forms in a more efficient and customizable way.
- Bootstrap v5.0: A popular CSS framework used for creating responsive and visually appealing user interfaces.
- Amazon Web Services: A cloud-based media management platform used for storing and serving images in the E-commerce plattform.

### Database
- ElephantSQL: ElephantSQL is a PostgreSQL database as a service. It is used as the database for the EasyKeyboardMaker project, providing a reliable and scalable storage solution for the application's data.

### Tools
- **Git**: A distributed version control system used for tracking changes in the project's source code.
- **GitHub**: A web-based hosting service for version control repositories, used for storing and managing the project's source code.
- **Gitpod**: An online integrated development environment (IDE) used for developing and testing the EasyKeyboardMaker project.
- **Heroku**: A cloud platform that enables deployment and hosting of web applications. Heroku was used for deploying the EasyKeyboardMaker project to a live server.
- **Adobe Photoshop**: A professional image editing software used for advanced image manipulation.
- **Figma**: An online collaborative design tool that offers a wide range of design and prototyping capabilities. Figma was used for creating mockups, prototypes, and design assets for the EasyKeyboardMaker website.
- **DB diagram**: An online database design and diagramming tool that simplifies the process of creating and visualizing database schemas. dbdiagram.io was used for designing and documenting the database schema of the EasyKeyboardMaker project.
- **Google Fonts**: A collection of free and open-source fonts used for typography on EasyKeyboardMaker's website.
- **Font Awesome**: A library of icons used for adding scalable vector icons to EasyKeyboardMaker's website.
- **Mailtrap**: In this project, Mailtrap was integrated to power the contact form, providing a secure environment for users to reach out to EasyKeyboardMaker via email.



### Supporting Libraries and Packages
- Copy the fully requirements.txt file at the end of the project and paste it here.

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Methodology

The EasyKeyboardMaker project follows a methodology inspired by agile principles, fostering collaboration, flexibility, and gradual development. The outlined approach has guided the project's evolution:

### Agile Project Management with GitHub Projects
To streamline project management, GitHub Projects is employed as a central hub. User stories and tasks are structured as GitHub issues, creating an organized workflow. The GitHub project board serves as a visual representation, tracking progress effectively.

### User Stories as GitHub Issues
Transforming user stories into GitHub issues captures user-centric functionalities. These issues interlink with respective user stories, simplifying access to criteria, tasks, and discussions.

### Bug Tracking for Seamless Development
Bugs uncovered during development are documented as GitHub issues, offering insights into each bug's characteristics, impact, and reproduction steps. By hyperlinking these issues in README.md, users can stay updated on bug resolutions and contribute insights.

### Iterative Development Approach
The EasyKeyboardMaker project adheres to an iterative development approach, facilitating continuous enhancements within a predefined timeline. Despite its condensed schedule, the project accommodates future iterations and expansions.

### Future Backlog and Progress
The project board efficiently manages user stories, with the "Not started" column representing upcoming iterations. This backlog previews user stories set for subsequent development phases.

Emphasizing that the project timeline is expedited, the iterative approach maintains adaptability, enabling ongoing refinements and improvements aligned with evolving user needs.

**Labels and User Story Distribution (MoSCoW):**

- **Must-Have:** 6/19 EXAMPLE FILL IN
- **Should-Have:** 
- **Could-Have:** 
- **Wont-Have:** 
- **Task:** 

For a comprehensive view of the project's trajectory, user stories, and bug tracking, explore the [Kanban board](https://github.com/users/KimBergstroem/projects/10).

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Features
### Example Page:
- Text <details><summary>See Screenshot **Examplepage**</summary><img src="docs/features/"></details>

- Text <details><summary>See Screenshot **Text**</summary><img src="docs/features/features"></details><details><summary>See Screenshot **Section**</summary><img src="docs/features/features"></details>

### Example Page:
- Text <details><summary>See Screenshot **Examplepage**</summary><img src="docs/features/"></details>

- Text <details><summary>See Screenshot **Text**</summary><img src="docs/features/features"></details><details><summary>See Screenshot **Section**</summary><img src="docs/features/features"></details>

### Example Page:
- Text <details><summary>See Screenshot **Examplepage**</summary><img src="docs/features/"></details>

- Text <details><summary>See Screenshot **Text**</summary><img src="docs/features/features"></details><details><summary>See Screenshot **Section**</summary><img src="docs/features/features"></details>

- Text <details><summary>See Screenshot **Section**</summary><img src="docs/features/features"></details>

### User Account Management:
- The account sign-up form allows new users to create an account and join the exclusive deals at the e-commerce. The form has validation to make sure that the user enters the correct information needed. This is a Django built-in validation system. Such validation is:

    - **Username**: Required and has a maximum of 150 characters or fewer. Only letters, digits, and @/./+/-/_ are allowed.
    - **Email**: Required and must be in a valid email format.
    - **Password**: Subject to the following constraints:
        - Cannot be too similar to your other personal information.
        - Must contain at least 8 characters.
        - Cannot be a commonly used password.
        - Cannot be entirely numeric.
    - See Screenshot<details><summary>**SIGNUP VALIDATION**</summary><img src="docs/features/features-blog-form-valid.png"></details>

- The login form ensures secure access to EasyKeyboardMaker by verifying your username and password. If you face login issues, use the 'Forgot Password?' link to reset your password. The form also displays validation error messages to guide you through any input errors.
    - See Screenshot<details><summary>**LOGIN VALIDATION**</summary><img src="docs/features/features-login-validation.png"></details>


- When an account is successfully created, the user will receive a confirmation message and gain access to the profile menu.<details><summary>See Screenshot **Success**</summary><img src="docs/features/features"></details>


- Text **Example Logout**</summary><img src="docs/features/"></details>


### Navigation:
### Example Page:
- Text <details><summary>See Screenshot **Examplepage**</summary><img src="docs/features/"></details>

- Text <details><summary>See Screenshot **Text**</summary><img src="docs/features/features"></details><details><summary>See Screenshot **Section**</summary><img src="docs/features/features"></details>


### Future Features
Here are some exciting features that I would like to add to the EasyKeyboardMaker E-commerce in the future:

- **Example of topic:**  
  Example

- **Example of topic:**  
  Example

- **Example of topic:**  
  Example

- **Example of topic:**  
  Example

- **Example of topic:**  
  Example

- **Example of topic:**  
  Example

<br>
These future enhancements aim to enrich EasyKeyboards's user experience, foster community engagement, and expand its reach to a global audience.


<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Testing

The EasyKeyboard E-commerce website went through a comprehensive testing process to guarantee its functionality, accessibility, and performance. This included checking the code, such as code validation, accessibility assessment, performance testing, cross-device testing, verification of browser compatibility, assessment of user stories, and the integration of user feedback to enhance the overall user experience.

All testing, including both manual and automated testing, was carried out and documented in [Testing.md](TESTING.md). 

<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Bugs
The bug section descriptions have been linked with the bug issues in my documentation for better visibility, added color coding, and divided the content into sections, all aimed at enhancing readability. The links are clickable for more reading and solution.

### Known bugs

| **Bug** | **Description** |
| ------- | --------------- |
| [Text](https://github.com/KimBergstroem/) | Text |
| [Text](https://github.com/KimBergstroem/) | Text |
| [Text](https://github.com/KimBergstroem/) | Text |



### Fixed bugs

| **Bug** | **Fix** |
| ------- | ------- |
| [Text](https://github.com/KimBergstroem/) | Text |
| [Text](https://github.com/KimBergstroem/) | Text |
| [Text](https://github.com/KimBergstroem/) | Text |


<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Deployment

### App Deployment
For deploying Your app, Heroku is used. Follow these steps:

 **Create a New App:**
   - Create a new app on Heroku dashboard.

 **Configure Settings:**
   - Navigate to "Settings" in new app.

 **Config Vars Setup:**
   - In "Config Vars," add `PORT` as the key and `8000` as its value.

 **Add PostgreSQL Database:**
   - Choose PostgreSQL as database.

        Example "ElephantSQL" was used in this project

 **Configure DATABASE_URL:**
   - In "Config Vars," add `DATABASE_URL` and copy the URL from PostgreSQL dashboard.

     Note: If using ElephantSQL as PostgreSQL provider, you can use the URL provided by ElephantSQL.

 **Environment Variable Setup:**
   - Create a new file in workspace called `env.py`.
   - Import the `os` library and set the environment variable for `DATABASE_URL` to the Heroku address (or ElephantSQL URL)
   - Add a secret key using `os.environ["SECRET_KEY"] = "your secret key here"`.

 **Heroku Config Vars:**
   - Add the secret key to the Heroku app's config vars in the settings.

 **Django Settings:**
   - In `settings.py` of Django app, import `Path` from `pathlib`, `os`, and `dj_database_url`.
   - Add `if os.path.isfile("env.py"): import env` to the file.
   - Replace the SECRET_KEY with `SECRET_KEY = os.environ.get('SECRET_KEY')`.
   - Replace the database section with `DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}`.

 **Migrate Models:**
   - In workspace terminal, migrate the models to the new database connection.

### Version Control
To manage version control and push code to the main repository on GitHub using GitPod, follow these steps:

 **Add Changes:**
   - In the GitPod terminal, use the command `git add .` to stage changes.

 **Commit Changes:**
   - Commit changes with a descriptive comment using the command:
     ```
     git commit -m "Push comment here"
     ```

 **Push to GitHub:**
   - Push the updates to the repository on GitHub with the command:
     ```
     git push
     ```


 **Migrate Models:**
    - In the terminal, migrate the models to the new database connection.

### Forking the Repository:

By forking the GitHub Repository, can create a copy of the original repository without affecting the original. Follow these steps:

 **GitHub Account Setup:**
   - Log into GitHub account or create one if you don't have one.

 **Locate the Repository:**
   - Find the repository at [https://github.com/KimBergstroem/PP5](https://github.com/KimBergstroem/PP5).

 **Fork the Repository:**
   - At the top right of the repository page, click "Fork" to create a copy in your own GitHub repository.

### Clone of the Repository:

Creating a clone allows you to have a local copy of the project. Follow these steps:

 **Repository URL:**
   - Navigate to [https://github.com/KimBergstroem/PP5](https://github.com/KimBergstroem/PP5).
   - Click the green "Code" button at the top right.

 **Clone the Repository:**
   - Select the "Clone by HTTPS" option and copy the provided URL to the clipboard.

 **Terminal and Git:**
   - Open your code editor or terminal and navigate to the directory where you want to clone the repository.
   - Run `git clone` followed by the copied URL.
   - Press enter, and Git will clone the repository to your local machine.


To fork the repository, follow these steps:

1. Go to the GitHub repository.
2. Click on the Fork button in the upper right-hand corner.
3. Wait for the forking process to complete. Once done, you will have a copy of the repository in your GitHub account.

To clone the repository, follow these steps:

1. Go to the GitHub repository.
2. Locate the Code button above the list of files and click it.
3. Select your preferred method for cloning: HTTPS, SSH, or GitHub CLI, and click the copy button to copy the repository URL to your clipboard.
4. Open Git Bash (or your preferred terminal).
5. Change the current working directory to the location where you want the cloned directory to be created.
6. Type the command `git clone` followed by the URL you copied in step 3. The command should look like this: `git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY`.
7. Press Enter to create your local clone.
<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Credits
I would like to express my gratitude to the following resources, which have been a huge help to me in the development of the EasyKeyBoard E-commerce project.

### Media
Images are taken from the following page:
- [Leonardo.ai](https://leonardo.ai/) **Used as a landing page hero image**


### Django Documentation:
The official Django documentation has been an invaluable resource throughout the project, providing comprehensive guidance on models, forms, templates, and various aspects of Django development.

- [Models](https://docs.djangoproject.com/en/4.2/topics/db/models/)
- [Form Validation](https://docs.djangoproject.com/en/4.1/ref/forms/validation/)
- [Model Field Types](https://docs.djangoproject.com/en/4.2/ref/models/fields/#model-field-types)
- [CSRF Trusted Origins](https://docs.djangoproject.com/en/4.0/ref/settings/#csrf-trusted-origins)
- [Built-in template tags and filters](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/)
- [Creating forms from models](https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/)
- [Model instance reference](https://docs.djangoproject.com/en/4.2/ref/models/instances/)
- [Signals](https://docs.djangoproject.com/en/4.2/topics/signals/)
- [Using mixins with class-based views](https://docs.djangoproject.com/en/4.2/topics/class-based-views/mixins/#detailview-working-with-a-single-django-object)
- [Using widgets in the form](https://docs.djangoproject.com/en/4.2/ref/forms/widgets/)
- [Date string form](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date)


### W3 Schools:
- [Overrite Bootstraps css variables](https://www.w3schools.com/css/css_important.asp)

### Bootstrap docs:
- [Increase knowledge of bootstrap framework](https://getbootstrap.com/docs/5.3/getting-started/introduction/)

### Geeksforgeeks: 
- [Using crisp form](https://www.geeksforgeeks.org/styling-django-forms-with-django-crispy-forms/)

### Various tutorials and YouTube channels:
I would like to extend my appreciation to the authors of the tutorials and YouTube channels that have shared their knowledge and expertise in Django development, enabling me to learn and apply best practices in building this project.
- [Django Tutorial - Setup](https://www.youtube.com/watch?v=Z4D3M-NSN58&list=PLzMcBGfZo4-kQkZp-j9PNyKq7Yw5VYjq9)
- [Style The Login Page With Bootstrap](https://www.youtube.com/watch?v=0Z_3APyKwQ4)
- [User Profile Update Display View with Image](https://www.youtube.com/watch?v=7DU-uhhYI6Y&list=PLSPMgrv4IuJ5wS0xSQzKUB038MYIx9ufI&index=12)
- [Style The Post details view](https://www.bootdey.com/snippets/tagged/blog)
- [Automated Testing: Behaviour Driven Development with Naoise Gaffney](https://www.youtube.com/watch?v=tHSJ4-ZqbLs)
- [Django Testing Tutorial - How To Test Your Django Applications](https://www.youtube.com/playlist?list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM)

### Content

- Paragraphs/text for the webpage/readme was written together with [ChatGPT](https://chat.openai.com/)

- Tips and inspiration on how to create a better readme.md file [kera-cudmore PowerPoint](https://docs.google.com/presentation/d/19_7r_To5bu7UjnZD87hrzWQi63Ij0YpaRH1XFnPZZe8/edit#slide=id.g35f391192_00)

- English spellchecker as Google Chrome extension [Grammarly](https://www.grammarly.com/)


<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>

# Acknowledgments
I'd like to give recognition to the individuals who supported me in completing this project:

* My family, for their patience and assistance in identifying spelling mistakes and testing issues. Their support has been invaluable in improving the quality of this project.
* Testers [Debbie B](https://github.com/DebbieBergstrom) and [Sandra B](https://github.com/SandraBergstrom) for their significant contributions in providing feedback, identifying errors, and offering valuable insights.
* [Brian](https://github.com/), my Code Institute Mentor, for his exceptional guidance and expertise, which greatly contributed to my growth as a developer.
* [Alan Bushell](https://github.com/Alan-Bushell), our cohort facilitator, for his dedication and weekly meetings where he has provided guidance, support, and encouragement to our cohort.

[Code Institute Slack Channel:](https://codeinstitute.net/) I received feedback from numerous users in a channel with over 3,000 members where I shared my E-commerce project. I am genuinely appreciative of the valuable feedback I received from the community.

I am truly grateful for their contributions, which have greatly enriched my learning and development.


<p align="right">(<a href="#table-of-content">back to top</a>)</p>
<p align="center">
  <img src="docs/readme.md/readme-divider3.png" />
</p>