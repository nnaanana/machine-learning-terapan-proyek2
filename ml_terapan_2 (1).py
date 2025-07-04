# -*- coding: utf-8 -*-
"""ML Terapan 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nirTMef-7yNA7NJfNMkwfdxLNWICcogG

# Import Library
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.sparse import csr_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer

import warnings
warnings.filterwarnings('ignore')

"""# Data Loading"""

# Load dataset
from google.colab import drive
drive.mount('/content/drive')

movie = '/content/drive/MyDrive/ML Terapan 2/indonesian_movies.csv'
df = pd.read_csv(movie)
df

"""Setelah memuat dan menampilkan dataset, dapat diketahui bahwa data memiliki 1272 baris dan 11 kolom

# Data Understanding
"""

# Ringkasan informasi dataset
df.info()

"""Dari ringkasan informasi dataset kita dapat menilai bahwa dataset memiliki missing values yang banyak, serta tipe data yang belum sesuai pada kolom votes"""

# Statistik deskriptif dataset
df.describe(include="all")

"""Insight :
- **Data tidak sempurna:** Banyak missing value pada beberapa kolom (description, genre, rating, directors, runtime).
- **Genre Drama dominan**
- **Distribusi tahun:** Data meliputi film dari 1926 hingga 2020, dengan mayoritas film modern.
- **Rata-rata rating pengguna cukup baik:** Mayoritas film mendapat rating pengguna di atas 6.
- **Mayoritas film berdurasi 90 menit:** Ini adalah durasi paling umum film Indonesia di dataset.
- **Sutradara dan aktor sangat bervariasi**

# Data Cleaning
"""

# Cek nilai yang kosong
print(df.isnull().sum())
# Cek nilai duplikat
print(f'\njumlah duplikasi data : {df.duplicated().sum()}')

"""Tidak ada duplikasi data namun terdapat banyak nya missing values pada dataset. Mari kita tangani"""

# Kategori genre pada dataset
print(f"data unik di kolom genre : {df['genre'].unique()} total ada {df['genre'].nunique()}")

# Kategori rating pada dataset
print(f"\ndata unik di kolom rating : {df['rating'].unique()} total ada {df['rating'].nunique()}")

"""Melihat masing masing kategori pada kolom kategorik seperti genre dan rating. untuk mendapat pemahaman sebelum penanganan missing values"""

# Mengisi nilai kosong di kolom deskripsi dengan 'unknown'
df['description'] = df['description'].fillna('Unknown')

# Mengisi nilai kosong di kolom genre dengan 'unknown'
df['genre'] = df['genre'].fillna('Unknown')

# Mengisi nilai kosong di kolom rating
df['rating'] = df['rating'].fillna("Unrated")

# Mengubah 11 kategori rating menjadi 5 kategori rating
df['rating'] = df['rating'].replace({
    "Not Rated": "Unrated",
    "PG-13": "13+",
    "TV-14": "13+",
    "TV-MA": "17+",
    "R": "17+",
    "D": "21+"
})

# Mengisi nilai kosong di kolom directors dengan 'unknown'
df['directors'] = df['directors'].fillna('unknown')

# Mengisi nilai kosong di kolom runtime dengan 'unknown'
df['runtime'] = df['runtime'].fillna('unknown')

"""* Penanganan pada kolom 'description', 'genre', 'directors', 'runtime' dengan mengisi nilai kosong dengan teks 'Unknown' agar tidak menghilangkan data yang mungkin dapat bermanfaat
* Penanganan pada kolom 'rating' dengan mengubah dari 11 kategori rating film menjadi hanya 5 kategori film saja, serta film yang belum di beri rating di isi dengan 'Unrated'
"""

# mengubah kolom votes menjadi integer setelah menghapus koma
df['votes'] = df['votes'].str.replace(',', '').astype(int)

"""* Mengubah tipe data object pada kolom votes menjadi integer"""

# Cek informasi dataset setelah data cleaning
df.info()

"""Ringkasan informasi pada dataset untuk mengetahui informasi dataset yang sudah melalui tahap data cleaning

# Exploratory Data Analysis (EDA)

## Univariate EDA
"""

sns.histplot(df['year'], bins=30, color='skyblue')
plt.title('Distribusi Film per Tahun')
plt.show()

"""Plot jumlah film yang dirilis setiap tahun, dapat diamati apakah industri perfilman Indonesia mengalami pertumbuhan, stagnasi, atau penurunan. Hasil visualisasi menunjukkan peningkatan signifikan dalam jumlah film yang diproduksi setelah tahun-tahun 2000, menandakan adanya perkembangan industri film lokal"""

df['genre'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Genre Film Terbanyak')
plt.show()

"""Analisis ini mengidentifikasi genre paling populer atau paling sering diproduksi di Indonesia. Dengan menghitung frekuensi tiap genre, diketahui genre mana yang mendominasi dataset. Hasilnya memperlihatkan beberapa genre seperti drama, komedi, dan horror menjadi genre favorit"""

sns.histplot(df['users_rating'], bins=20, color='skyblue')
plt.title('Distribusi User Rating')
plt.show()

"""Distribusi ini menggambarkan bagaimana penilaian pengguna terhadap film-film Indonesia. Dengan melihat sebaran nilai `users_rating`, dapat diketahui bahwa kebanyakan film mendapat rating 6 sampai 7. Pola sebaran ini juga membantu dalam menentukan threshold relevansi pada tahap evaluasi"""

df['rating'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Rating Kategori Film Terbanyak')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Kategori rating mengacu pada klasifikasi umur/konten (seperti SU, 13+, 17+, dsb). Analisis ini memeriksa bagaimana distribusi film berdasarkan kategori rating, yang penting untuk memastikan sistem rekomendasi tidak merekomendasikan film yang tidak sesuai dengan preferensi usia pengguna

## Multivariate EDA
"""

for genre in df["genre"].unique():
    data = df[df["genre"] == genre]
    print("Film populer dengan genre", genre, "=", data.sort_values("users_rating", ascending = False).head(1)["title"].values[0])

"""Analisis ini menghubungkan antara popularitas (user_rating) dengan genre film. Tujuannya untuk mengetahui genre apa yang memiliki film-film yang disukai user. Informasi ini bermanfaat untuk mengidentifikasi genre yang layak difokuskan pada sistem rekomendasi."""

df.groupby('genre')['users_rating'].mean().sort_values(ascending=False).head(10).plot(kind='barh', color='skyblue')
plt.title('Rata-rata User Rating per Genre')
plt.xlabel('Rata-rata Rating')
plt.tight_layout()
plt.show()

"""Analisis ini mencari genre yang rata-rata memiliki penilaian pengguna paling tinggi yaitu genre 'History'. Genre dengan rating rata-rata tinggi dapat dianggap memiliki kualitas konten yang baik

# Data Preparation
"""

# menggabungkan kolom title, description, genre
df['combined'] = df['title'] + ' ' + df['description'] + ' ' + df['genre']

"""Menggabungkan kolom title, description, genre sebagai acuan untuk TF-IDF Vectorizer"""

# menggunakan teknik TF-IDF pada kolom yang digabungkan sebelumnya
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""* TfidfVectorizer digunakan untuk mengubah koleksi dokumen teks mentah menjadi matriks fitur TF-IDF.

* Parameter stop_words='english' memberi tahu vektorizer untuk mengabaikan stop words bahasa Inggris. Stop words adalah kata-kata umum seperti "the", "a", "is", "and", dll., yang biasanya tidak membawa banyak makna dan dapat mengganggu analisis teks. Dengan menghapusnya, Model akan lebih fokus pada kata-kata yang lebih relevan.
"""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Melakukan normalisasi dengan Normalizer
normalizer = Normalizer()
tfidf_norm = normalizer.fit_transform(tfidf_matrix)

"""* TF-IDF yang sudah dinormalisasi menggunakan Normalizer berfungsi untuk setiap baris dalam matriks ini sekarang mewakili dokumen, dan panjang vektor untuk setiap dokumen adalah 1.

# Model Development : Content based filtering
"""

# membuat model menggunakan cosine similarity
similarity_cb = cosine_similarity(tfidf_norm)
similarity_cb

"""Cosine similarity adalah metrik yang digunakan untuk mengukur kemiripan antara dua vektor non-nol dalam ruang produk skalar. Dalam konteks pengolahan bahasa alami (NLP).

* Bagaimana cara kerjanya?

Setiap dokumen direpresentasikan sebagai vektor dalam ruang multidimensi (dimana setiap dimensi adalah kata unik).
Cosine similarity menghitung kosine dari sudut antara dua vektor.
Nilai cosine similarity berkisar antara -1 hingga 1:

1: Menunjukkan bahwa kedua vektor (dokumen) sangat mirip atau identik. Sudut antara mereka adalah 0 derajat.

0: Menunjukkan bahwa kedua vektor (dokumen) tidak terkait sama sekali atau ortogonal. Sudut antara mereka adalah 90 derajat.

-1: Menunjukkan bahwa kedua vektor (dokumen) sangat berlawanan. Sudut antara mereka adalah 180 derajat.

**Karena vektor TF-IDF yang sudah dinormalisasi biasanya hanya memiliki nilai positif (atau nol), maka nilai cosine similarity-nya akan berkisar antara 0 dan 1.**
"""

# Menyimpan nilai simalarity ke dalam dataframe
similarity_df = pd.DataFrame(similarity_cb, index=df['title'], columns=df['title'])

"""Menyimpan perhitungan cosine similarity ke dalam dataframe untuk melihat nilai kemiripan konten pada film

# Testing Model
"""

def recommend_movies(title, n=5):
    if title not in similarity_df.columns:
        return f"Judul film '{title}' tidak ditemukan."

    similar_movies = similarity_df[title].sort_values(ascending=False)[1:n+1]
    return pd.DataFrame({
        'Rekomendasi': similar_movies.index,
        'Skor Similarity': similar_movies.values
    })

# Film yang mirip dilan
recommend_movies('Dilan 1990', 5)

"""Dari testing model untuk Rekomendasi film yang mirip dengan dilan 1990 yaitu ada Dilan 1991 dan Milea yang merupakan sekuel dari dilan 1990 dengan kemiripan sekitar 0,4, lalu selanjutnya ada #FriendButMarried dengan skor similarity 0.08

# Model Evaluation
"""

# Menampilkan dataframe
similarity_df.head()

plt.figure(figsize=(10,7))
sns.heatmap(similarity_df.iloc[:5, :5],
            cmap='Blues',
            annot=True,
            fmt=".2f",
            linewidths=0.5)
plt.xticks(rotation=45)
plt.title("Similarity Matrix antar Film (Top 5) dengan Nilai Cosine Similarity")
plt.show()

"""Matriks similarity menunjukkan rendahnya kemiripan antar sebagian besar film berdasarkan konten teks TF-IDF (banyak nilai 0.00). Ini menyiratkan konten film yang sangat beragam/unik.

Namun, terdapat poin kemiripan menarik seperti "Aku tahu kapan kamu mati" dengan "4 Mantan" (0.04) yang menjadi kandidat utama untuk rekomendasi berbasis konten dan menunjukkan model berhasil menangkap koneksi khusus.
"""

threshold = 6.0  # batasan rating >= 6 dianggap relevan

def get_top_k_recommendations(title, k=5):
    similar_movies = similarity_df[title].sort_values(ascending=False)[1:k+1]
    return similar_movies.index.tolist()

def precision_at_k(title, k=5, threshold=threshold):
    top_k = get_top_k_recommendations(title, k)

    # Hitung jumlah rekomendasi relevan (users_rating >= threshold)
    relevan = df[df['title'].isin(top_k)]
    relevan_count = (relevan['users_rating'] >= threshold).sum()

    precision = relevan_count / k
    return precision

film_sample = df['title'].sample(10, random_state=1)
precision_list = []

for film in film_sample:
    try:
        p = precision_at_k(film, k=5)
        precision_list.append(p)
    except:
        continue

average_precision = np.mean(precision_list)
print(f'Average Precision@5: {average_precision:.2f}')

"""Rata-rata precision@5 sekitar 48% dari 5 rekomendasi teratas yang diberikan oleh sistem Anda 2 sampai 3 di antaranya adalah relevan bagi pengguna.

**Ini menunjukkan bahwa sistem rekomendasi memiliki kemampuan yang cukup bagus untuk mendapatkan rekomendasi film dengan genre, deskripsi, dan judul yang mirip**
"""