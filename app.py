
import streamlit as st
import pickle
import os
import requests

from dotenv import load_dotenv
from scipy.sparse import load_npz

load_dotenv()

try:
    TMDB_API_KEY = st.secrets["TMDB_API_KEY"]
except Exception:
    TMDB_API_KEY = os.getenv("TMDB_API_KEY")

TMDB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# ---------------- WEBSITE STYLING ----------------

st.markdown("""
<style>
.stApp {
    background-color: #101014;
    color: white;
}

h1 {
    color: #F5C518 !important;
    text-align: center;
    font-weight: 800;
}

h2, h3 {
    color: white !important;
}

.stButton > button {
    background-color: #F5C518;
    color: black;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    height: 45px;
}

.stButton > button:hover {
    background-color: #FFD84D;
    color: black;
}

[data-testid="stSelectbox"] {
    background-color: #1C1C24;
}

[data-testid="stSlider"] {
    color: #F5C518;
}

/* Movie poster styling */
[data-testid="stImage"] img {
    border-radius: 12px;
    transition: transform 0.3s ease;
}

[data-testid="stImage"] img:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)


# ---------------- CHECK API KEY ----------------

if not TMDB_API_KEY:
    st.error("TMDB API key not found. Please check your .env file.")
    st.stop()


# ---------------- LOAD MODEL DATA ----------------

@st.cache_resource
def load_model():

    with open("model/new_df.pkl", "rb") as f:
        new_df = pickle.load(f)

    similarity = load_npz("model/similarity.npz")

    return new_df, similarity


try:
    new_df, similarity = load_model()

except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()


# ---------------- RECOMMENDATION FUNCTION ----------------

def recommend(movie, top_n=5):

    movie = movie.strip().lower()

    matching_movies = new_df[
        new_df["title"].str.strip().str.lower() == movie
    ]

    if matching_movies.empty:
        return []

    movie_index = matching_movies.index[0]

    distances = similarity[movie_index].toarray().ravel()

    movies_list = sorted(
        enumerate(distances),
        key=lambda x: x[1],
        reverse=True
    )

    movies_list = [
        item for item in movies_list
        if item[0] != movie_index
    ][:top_n]

    recommendations = []

    for i, score in movies_list:

        recommendations.append({
            "movie_id": int(new_df.iloc[i]["movie_id"]),
            "title": new_df.iloc[i]["title"],
            "similarity": round(float(score), 3)
        })

    return recommendations


# ---------------- FETCH MOVIE POSTER ----------------
@st.cache_data(ttl=86400)
def get_movie_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}"

    params = {
        "api_key": TMDB_API_KEY
    }

    for attempt in range(3):
        try:
            response = requests.get(
                url,
                params=params,
                timeout=30
            )

            response.raise_for_status()

            data = response.json()
            poster_path = data.get("poster_path")

            if poster_path:
                return TMDB_IMAGE_URL + poster_path

            return None

        except requests.exceptions.SSLError:
            if attempt == 2:
                print("TMDB SSL connection failed.")
                return None

        except requests.exceptions.RequestException:
            if attempt == 2:
                print("TMDB request failed.")
                return None

    return None

# ---------------- WEBSITE DESIGN ----------------

st.title("🎬 Movie Recommendation System")

st.write(
    "Discover movies similar to your favourite movies "
    "using Machine Learning!"
)

st.divider()

st.subheader("🍿 Find Your Next Favourite Movie")

movie_options = sorted(new_df["title"].dropna().unique())

selected_movie = st.selectbox(
    "Choose a movie",
    movie_options,
    index=None,
    placeholder="Search or select a movie..."
)

top_n = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5
)


# ---------------- DISPLAY RECOMMENDATIONS ----------------

if st.button("✨ Recommend Movies", width="stretch"):

    if selected_movie:

        recommendations = recommend(selected_movie, top_n)

        if recommendations:

            st.success(
                f"Movies similar to {selected_movie}"
            )

            for start in range(0, len(recommendations), 5):

                cols = st.columns(5)

                for col, movie in zip(
                    cols,
                    recommendations[start:start + 5]
                ):

                    with col:

                        poster = get_movie_poster(
                            movie["movie_id"]
                        )

                        if poster:
                            st.image(
                                poster,
                                use_container_width=True
                            )
                        else:
                            st.markdown("🎬 Poster unavailable")

                        st.markdown(
                            f"**{movie['title']}**"
                        )

                        st.caption(
                            f"⭐ Similarity: {movie['similarity']}"
                        )

                        st.progress(
                            min(movie["similarity"], 1.0)
                        )

        else:
            st.error("No recommendations found.")

    else:
        st.warning("Please select a movie first.")


# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Movie Recommendation System | Powered by Machine Learning"
)

