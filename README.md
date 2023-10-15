# Weatherama

#### Description: An open source weather app made with flask.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Database Schema](#database-schema)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Weatherama is a web app that provides users with up-to-date weather information for their desired locations. This web application is built using Python, Flask, SQL, HTML, and CSS. With Weatherama, users can search for a city, get random city weather on every refresh, view saved search history, change units, and see additional information about humidity, pressure, wind, and real feel.

## Features

- Search for weather information by city
- Display random city weather on every refresh
- Save searched cities in the database and display the most searched ones
- Change temperature units (Celsius or Fahrenheit)
- View additional information (humidity, pressure, wind, real feel)

## Technologies

- Python
- Flask
- SQLite3
- HTML
- CSS

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ak-anas/weatherama.git
cd weatherama
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

The database should be already initialized.

## Usage

1. Run the application:

```bash
cd weatherama
flask run
```

2. Open your web browser and go to `http://localhost:5000` to access Weatherama.

3. Use the search bar to look up weather information for a specific city.

4. Weather for a random city will be displayed on every page refresh.

5. The searched cities will be saved in the database, and the top 3 recent searches will be displayed on the page.

6. You can change the temperature units (Celsius or Fahrenheit) using the provided option.

7. Additional weather details such as humidity, pressure, wind, and real feel will be shown alongside the basic weather information.

## Files

The project uses many files:
    - assets/country-list.json: the program extracts from this file a random city to display it's weather on every page refresh

    - search.db: database to store most searched cities.

    - requirements.txt: list of libraries used in this project. (must install)

    - templates/index.html: our main page.

    - templates/apology.html: error page.

    - static/style.css: the style of our main page and error page.

    - app.py: the backend of our project.

## Database Schema

The database will contain the following table:

- **search**: Stores searched cities (city_name, count).

## Contributing

Contributions to Weatherama are welcome! If you find a bug or want to add a new feature, please follow these steps:

1. Fork the repository.

2. Create a new branch for your changes.

3. Make your changes and commit them.

4. Push your changes to your forked repository.

5. Create a pull request to the main repository.

We appreciate any contributions, whether they are code improvements, bug fixes, or documentation enhancements.

## License

Data is provided by OpenWeatherMap.org

---

Thank you for using Weatherama! We hope this project provides you with valuable weather information and serves as an excellent example of Python, Flask, SQL, HTML, and CSS integration. Enjoy your weather experience with Weatherama!
