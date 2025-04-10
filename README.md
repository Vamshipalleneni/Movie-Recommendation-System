# 🎬 Movie Recommender System

This project is a **Content-Based Movie Recommendation System** that suggests movies based on the similarity of their content. It leverages **Natural Language Processing (NLP)** and **machine learning techniques** to analyze movie metadata and generate personalized recommendations. The system displays both **movie titles and posters**, using data fetched from the **TMDb API**.

## 🚀 Framework

- **[Streamlit](https://streamlit.io/)** — for building an interactive and responsive web application.

## 📦 Libraries Used

- `numpy`
- `pandas`
- `nltk` (Natural Language Toolkit)
- `scikit-learn`
- `pickle`

## 🧠 Algorithms & Modules

- **Porter Stemmer** (`nltk.stem.porter`)
- **CountVectorizer** (`sklearn.feature_extraction.text`)
- **Cosine Similarity** (`sklearn.metrics.pairwise.cosine_similarity`)

## 🔧 Preprocessing Steps

1. Loaded two datasets from Kaggle: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
2. Removed null values to ensure data integrity.
3. Merged both datasets using the `id` column to create a unified dataset.
4. Dropped unnecessary columns to retain only relevant features for recommendation.

## 🧩 Key Techniques Explained

### 1. **Porter Stemmer**
Used to reduce words to their root form. For example, "running", "runs", and "ran" all become "run". This reduces feature space and improves recommendation accuracy.

### 2. **CountVectorizer**
Converts a collection of text documents to a matrix of token counts. This allows the system to quantify the textual content of movies for comparison.

### 3. **Cosine Similarity**
Measures the cosine of the angle between two vectors in a multi-dimensional space. In this case, it computes the similarity between movies based on their content.

## 🌐 How to Run the App

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vamshipalleneni/Movie-Recommendation-System.git
