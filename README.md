# Movie Recommendation System 🎬

## About the Project

The Movie Recommendation System is a machine learning-based web application developed using Python and Streamlit. It recommends movies based on the similarity of their features, helping users discover movies according to their interests.

The project uses **Content-Based Filtering**, TF-IDF Vectorization, and Cosine Similarity to find and recommend similar movies. It also integrates the TMDB API to fetch and display movie posters.

## Features

- Search and select a movie.
- Get recommendations for similar movies.
- Content-Based Movie Filtering.
- TF-IDF Vectorization for text feature extraction.
- Cosine Similarity for calculating movie similarity.
- Fetch movie posters using TMDB API.
- Interactive web interface using Streamlit.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| TF-IDF | Text feature extraction |
| Cosine Similarity | Similarity calculation |
| Streamlit | Web application |
| TMDB API | Movie poster fetching |

## How It Works

1. **Dataset Loading:** Loads movie information from the dataset.
2. **Data Preprocessing:** Cleans and prepares movie information.
3. **Feature Extraction:** Converts movie features into numerical vectors using TF-IDF.
4. **Similarity Calculation:** Calculates similarity between movies using Cosine Similarity.
5. **Recommendation:** Finds movies with similar features and displays recommendations.
6. **Poster Fetching:** Uses TMDB API to retrieve movie posters.

## Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── requirements.txt
├── data/
├── model/
├── .env
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nidhish-bhardwaj/Movie-Recommendation-System.git
```

### 2. Open Project Folder

```bash
cd Movie-Recommendation-System
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure TMDB API

Create a `.env` file and add your TMDB API key:

```text
TMDB_API_KEY=your_api_key
```

### 5. Run the Application

```bash
streamlit run app.py
```

## Machine Learning Concepts

**1. Content-Based Filtering**

Recommends movies by comparing their features, such as genres, keywords, and descriptions.

**2. TF-IDF (Term Frequency-Inverse Document Frequency)**

Converts textual information into numerical vectors based on the importance of words.

**3. Cosine Similarity**

Measures the similarity between movie vectors. A higher similarity score indicates that two movies have more similar features.

## Future Improvements

- Add movie ratings and reviews.
- Improve recommendation accuracy.
- Add user-based recommendation features.
- Include more movie details.
- Improve the user interface.

## Author

**Nidhish Bhardwaj**

GitHub: https://github.com/nidhish-bhardwaj

## Acknowledgement

- [TMDB](https://www.themoviedb.org/) for movie information and poster images.
- [Scikit-learn](https://scikit-learn.org/) for machine learning tools.
- [Streamlit](https://streamlit.io/) for the web application framework.

---

⭐ If you like this project, consider giving it a star!
