# News Aggregator Website

The News Aggregator Website is a comprehensive and user-friendly web application designed to deliver the latest news articles from various sources in one convenient location. Built using the Django framework and Bootstrap, the application offers a visually appealing and easily navigable interface that caters to users' diverse interests.

## Languages and Tools:
<p align="left"> 
<a href="https://www.w3schools.com/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> 
<a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> 
<a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://cdn.worldvectorlogo.com/logos/django.svg" alt="django" width="40" height="40"/> </a> 
<a href="https://getbootstrap.com" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> 
</p>

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

4. Create a News API key from https://newsapi.org/ and attach the key to the API link
```bash
key = "https://newsapi.org/v2/top-headlines?country=us&apiKey=<INSERT KEY>"
```

5. Run the Django development server:
```bash
python manage.py runserver
```

6. Open your web browser and navigate to http://127.0.0.1:8000/ to access the News Aggregator Website.
<img width="950" alt="image" src="https://user-images.githubusercontent.com/111834642/227087178-9578b9f9-ed45-4ac0-97f7-88e61113b906.png">

## License
This project is released under the MIT License. Please see the 'LICENSE' file for more information.

