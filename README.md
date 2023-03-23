# News Aggregator Website

The News Aggregator Website is a comprehensive and user-friendly web application designed to deliver the latest news articles from various sources in one convenient location. Built using the Django framework and Bootstrap, the application offers a visually appealing and easily navigable interface that caters to users' diverse interests.

## Features

1. **Aggregated news articles**: The website gathers news articles from multiple sources, providing a wide range of information to users.

2. **REST API integration**: The application integrates with the News API, utilizing HTTP requests and JSON formatting to obtain each article's title, description, image, URL, source, and publish date.

3. **Visually engaging user interface**: The website employs Bootstrap's Album template to create a visually appealing front-end that ensures seamless navigation and an enjoyable user experience.

4. **Category navigation bar**: A functional category navigation bar enables users to filter news articles by various topics, including Business, Health, Science, Sports, and Technology, allowing for personalized content exploration.

5. **Responsive design**: The website is built with a responsive design that ensures optimal display and functionality across various devices, such as desktops, tablets, and smartphones.

6. **Frequent updates**: The news articles are updated regularly, providing users with the latest information from their selected sources.

## Installation and Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/news-aggregator-website.git
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Apply Migrations:
```bash
python manage.py migrate
```

4. Create a News API key from https://newsapi.org/ and add it to the 'settings.py' file:
```bash
NEWS_API_KEY = 'your_api_key_here'
```

5. Run the Django development server:
```bash
python manage.py runserver
```

6. Open your web browser and navigate to http://127.0.0.1:8000/ to access the News Aggregator Website.
```bash
```

## License
This project is released under the MIT License. Please see the 'LICENSE' file for more information.
