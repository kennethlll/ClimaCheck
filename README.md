# ClimaCheck

ClimaCheck is a web application that provides users with up-to-date weather information for any location. Users can search for a city and view the current weather conditions, 5-day forecast, and any active weather alerts issued by Environment Canada. In addition, users can choose to receive weather alerts by SMS and can easily change the location for which they are viewing weather information.


## Technologies

ClimaCheck was built using a variety of technologies, including:

- HTML
- CSS
- Bootstrap
- Django
- Beautiful Soup

## Getting Started

To get started with ClimaCheck, simply clone this repository and run the following command to start the Django development server:

python manage.py runserver


Then, open your web browser and navigate to `http://localhost:8000` to start using ClimaCheck!

## Files

This repository contains the following files:

- `README.md`: This file, containing information about the project
- `manage.py`: A Python script for managing the Django project
- `climacheck/`: A Django app containing the main code for the ClimaCheck application
  - `templates/`: Contains the HTML templates used for the web pages
  - `static/`: Contains the CSS stylesheets and other static files used for styling the web pages
  - `views.py`: Contains the code for the views (web pages) in the ClimaCheck application
  - `models.py`: Contains the code for the data models used in the ClimaCheck application
  - `forms.py`: Contains the code for the forms used in the ClimaCheck application
  - `webscraper.py`: Contains the code for web scraping weather information from Environment Canada's website

## Design Choices

We chose to use Django as our web framework because of its ease of use and built-in features such as URL routing, form handling, and template rendering. We also chose to use Beautiful Soup for web scraping because of its simplicity and compatibility with Python.

## Contributors

- [Your Name](https://github.com/yourusername)

We welcome contributions to ClimaCheck and appreciate any feedback you may have. Please feel free to submit pull requests or open issues if you encounter any problems or have suggestions for improvement.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

