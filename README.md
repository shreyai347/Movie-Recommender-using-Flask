

---

# 🎬 Movie Recommendation System 🍿

![Screenshot (82)](https://github.com/user-attachments/assets/fd8c0f83-df24-4661-990f-86ac24355649)
![Screenshot 2024-09-28 172425](https://github.com/user-attachments/assets/2a146abd-8753-425e-8eb4-b2ef8fe90532)
![Screenshot 2024-09-28 163759](https://github.com/user-attachments/assets/07b17643-3e93-4596-8951-8fe03b6c60ec)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction
Welcome to the **Movie Recommendation System**! This application leverages advanced data analysis techniques and machine learning algorithms to suggest movies based on user preferences. Whether you're a cinephile or just looking for something to watch, this app has you covered!

## Features
- **Personalized Recommendations**: Get movie suggestions tailored to your taste.
- **Dynamic Trailer Links**: Watch trailers directly from the recommendations.
- **Rich Movie Posters**: View visually appealing posters fetched from Wikipedia.
- **User-Friendly Interface**: Intuitive design to enhance user experience.

## Technologies Used
- **Backend**: Flask
- **Data Processing**: Pandas, NumPy, SciPy
- **Fuzzy Matching**: FuzzyWuzzy
- **Web Scraping**: BeautifulSoup
- **API Integration**: YouTube Data API, Wikipedia API
- **Frontend**: HTML, CSS

## Getting Started
### Prerequisites
Before you begin, ensure you have the following installed:
- Python 3.x
- pip

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/movie-recommendation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie-recommendation-system
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### API Keys
You'll need to set up your API keys for the YouTube Data API. Visit the [Google Cloud Console](https://console.cloud.google.com/) to create your API key and replace it in `app.py`.

## Usage
1. Start the Flask app:
   ```bash
   python app.py
   ```
2. Open your web browser and navigate to `http://127.0.0.1:5000/`.
3. Enter the name of the movie you want recommendations for and hit **Get Recommendations**!

## File Structure
```
movie-recommendation-system/
│
├── app.py                  # Main application file
├── requirements.txt        # Required libraries
├── dataset/                # Directory containing datasets
│   ├── TrainData.pkl       # Trained model data
│   └── similarity.pkl       # Similarity matrix
├── templates/              # HTML templates
│   ├── index.html          # Home page
│   ├── recommendations.html # Recommendations display
│   └── no_output.html      # No match found page
└── static/                 # Static files (CSS, images)
```

## Contributing
We welcome contributions! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License
No License.

## Acknowledgments
- Thanks to the contributors of the libraries used in this project.
- Inspired by various movie recommendation systems.

---


