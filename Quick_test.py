from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

df = pd.read_csv('dataset/cleaned_products.csv')

cv = CountVectorizer(stop_words='english')
vectors = cv.fit_transform(df['combined'])

similarity = cosine_similarity(vectors)

print("✅ Similarity matrix created. Shape:", similarity.shape)
