
# Avatar Generator Web App

## Overview
The Django web application allows users to create unique avatars by combining different sets of eyes, mouths, and background colors. Users can either generate a random avatar or provide a custom seed to create a personalized avatar. The application also supports user registration and login.

## Features
- **User Registration**: Users can sign up for an account.
- **User Login**: Registered users can log in to access additional features.
- **Random Avatar Generation**: Users can generate random avatars.
- **Custom Seed Input**: Users can provide a seed (string), and the application generates an avatar based on the ASCII values of the seed.
- **Avatar Customization**: For custom seed-based avatars, users can choose to copy the URL of the generated avatar or download it as either a PNG or SVG file.
- **Dynamic Avatar Generation**: Random avatars are regenerated every time the page is refreshed, ensuring uniqueness.
- **SVG Eye, Mouth, and Background Components**: The application uses pre-saved SVG images for eyes, mouths, and background colors to create avatars with various combinations.

## Folder Structure
- **`generate`**: Django app folder containing the project's main logic and templates.
- **`static`**: Contains static files, such as images and CSS styles.
- **`templates`**: HTML templates for rendering web pages.


## Database
The project uses SQLite as the database for user data and authentication.

## Getting Started
To set up this project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies (Django, Python).
3. Apply database migrations to create the SQLite database.
4. Start the Django development server.

## Usage
1. Access the web application from your browser.
2. Register for an account or log in if you already have one.
3. Choose between generating a random avatar or creating a custom avatar with a seed.
4. Customize the avatar, copy the URL, and download it in PNG or SVG format.
5. For random avatars, simply refresh the page to see new avatars.

## Future Works
Enhanced Avatar Customization: 
     To allow users to customize various aspects of their avatars. This will include the ability to choose specific eyes, mouths, background colors, and even the shape of the avatar. The aim to provide users with more control over the appearance of their avatars for a truly personalized experience.




