# -*- coding: utf-8 -*-
"""ML Terapan 2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nirTMef-7yNA7NJfNMkwfdxLNWICcogG

# Proyek Pertama Machine Learning Terapan - Sistem Rekomendasi
- **Nama:** Nabilah Wanara
- **Email:** 	mc006d5x211p@student.devacademy.id
- **ID Dicoding:** MC006D5X2119

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

"""Diketahui bahwa data memiliki 1272 baris dan 11 kolom

# Data Understanding
"""

# Ringkasan informasi dataset
df.info()

"""Berdasarkan ringkasan informasi dataset, dapat disimpulkan bahwa dataset mengandung banyak nilai yang hilang serta terdapat ketidaksesuaian tipe data pada kolom votes."""

# Statistik deskriptif dataset
df.describe(include="all")

"""Insight :
- **Data tidak sempurna:** Banyak missing value pada beberapa kolom (description, genre, rating, directors, runtime).
- **Genre Drama dominan**
- **Distribusi tahun:** Data meliputi film dari 1926 hingga 2020 dengan mayoritas film modern.
- **Rata-rata rating pengguna cukup baik:** Mayoritas film mendapat rating pengguna di atas 6.
- **Mayoritas film berdurasi 90 menit:** Ini adalah durasi paling umum film Indonesia di dataset.
- **Sutradara dan aktor sangat bervariasi**

# Data Cleaning
"""

# Cek nilai yang kosong
print(df.isnull().sum())

# Cek nilai duplikat
print(f'\njumlah duplikasi data : {df.duplicated().sum()}')

"""Dataset tidak mengandung data duplikat, namun memiliki sejumlah besar nilai yang hilang."""

# Kategori genre pada dataset
print(f"Data unik di kolom genre : {df['genre'].unique()} total ada {df['genre'].nunique()}")

# Kategori rating pada dataset
print(f"\nData unik di kolom rating : {df['rating'].unique()} total ada {df['rating'].nunique()}")

"""Meninjau setiap kategori dalam kolom kategorikal seperti genre dan rating untuk memperoleh pemahaman yang lebih baik sebelum melakukan penanganan terhadap nilai yang hilang."""

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

"""* Kolom 'description', 'genre', 'directors', dan 'runtime' ditangani dengan mengisi nilai yang kosong menggunakan teks 'Unknown', guna menjaga agar data potensial tetap dipertahankan dan tidak terbuang.
* Kolom 'rating' disederhanakan dari 11 kategori menjadi hanya 5 kategori utama untuk memudahkan analisis, sementara film yang belum memiliki rating akan diberi label 'Unrated'.
"""

# mengubah kolom votes menjadi integer setelah menghapus koma
df['votes'] = df['votes'].str.replace(',', '').astype(int)

"""Mengubah tipe data object pada kolom votes menjadi integer"""

# Cek informasi dataset setelah data cleaning
df.info()

"""# Exploratory Data Analysis (EDA)

## Univariate EDA
"""

sns.histplot(df['year'], bins=30, color='skyblue')
plt.title('Distribusi Film per Tahun')
plt.show()

"""Visualisasi jumlah film yang dirilis setiap tahunnya memberikan gambaran tentang tren industri perfilman Indonesia, apakah sedang tumbuh, stagnan, atau menurun. Berdasarkan hasil plot, terlihat adanya lonjakan produksi film secara signifikan setelah tahun 2000, yang mengindikasikan kemajuan dan pertumbuhan positif dalam industri film nasional."""

df['genre'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Genre Film Terbanyak')
plt.show()

"""Analisis ini mengidentifikasi genre yang paling umum atau paling sering diproduksi di industri film Indonesia. Dengan menghitung frekuensi kemunculan setiap genre, dapat diketahui genre-genre yang paling mendominasi dalam dataset. Hasil analisis menunjukkan bahwa genre seperti drama, komedi, dan horor merupakan genre yang paling populer dan banyak diproduksi."""

sns.histplot(df['users_rating'], bins=20, color='skyblue')
plt.title('Distribusi User Rating')
plt.show()

"""Distribusi ini memberikan gambaran mengenai bagaimana pengguna menilai film-film Indonesia. Dari sebaran nilai users_rating, terlihat bahwa sebagian besar film memperoleh rating antara 6 hingga 7. Pola ini tidak hanya mencerminkan persepsi umum penonton, tetapi juga berguna dalam menetapkan ambang batas (threshold) relevansi saat proses evaluasi dilakukan."""

df['rating'].value_counts().head(10).plot(kind='bar', color='skyblue')
plt.title('Rating Kategori Film Terbanyak')
plt.ylabel('Jumlah')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

"""Kategori rating mengacu pada klasifikasi umur atau konten (seperti SU, 13+, 17+, dsb). Analisis ini memeriksa bagaimana distribusi film berdasarkan kategori rating, yang penting untuk memastikan sistem rekomendasi tidak merekomendasikan film yang tidak sesuai dengan preferensi usia pengguna.

## Multivariate EDA
"""

for genre in df["genre"].unique():
    data = df[df["genre"] == genre]
    print("Film populer dengan genre", genre, "=", data.sort_values("users_rating", ascending = False).head(1)["title"].values[0])

"""Analisis ini mengeksplorasi hubungan antara tingkat popularitas (user_rating) dan genre film, dengan tujuan mengidentifikasi genre yang cenderung menghasilkan film-film yang disukai oleh pengguna. Informasi ini berguna untuk menentukan genre-genre yang potensial dan layak menjadi fokus utama dalam pengembangan sistem rekomendasi."""

df.groupby('genre')['users_rating'].mean().sort_values(ascending=False).head(10).plot(kind='barh', color='skyblue')
plt.title('Rata-rata User Rating per Genre')
plt.xlabel('Rata-rata Rating')
plt.tight_layout()
plt.show()

"""Analisis ini bertujuan untuk mengidentifikasi genre dengan rata-rata penilaian pengguna tertinggi, di mana genre 'History' menempati posisi teratas. Genre-genre dengan rata-rata rating yang tinggi dapat dianggap memiliki kualitas konten yang unggul dan berpotensi tinggi untuk menarik minat penonton.

# Data Preparation

Menggabungkan kolom title, description, genre sebagai acuan untuk TF-IDF Vectorizer
"""

# menggabungkan kolom title, description, genre
df['combined'] = df['title'] + ' ' + df['description'] + ' ' + df['genre']

# menggunakan teknik TF-IDF pada kolom yang digabungkan sebelumnya
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['combined'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

"""* TfidfVectorizer digunakan untuk mengubah kumpulan dokumen teks mentah menjadi representasi numerik berupa matriks fitur TF-IDF (Term Frequency–Inverse Document Frequency), yang mencerminkan pentingnya kata-kata dalam dokumen relatif terhadap seluruh korpus.

* Pengaturan parameter stop_words='english' menginstruksikan vektorizer untuk mengabaikan kata-kata umum dalam bahasa Inggris (seperti "the", "is", "and", "a", dll.). Kata-kata ini biasanya tidak memberikan informasi yang signifikan dan dapat mengaburkan makna sebenarnya dalam analisis teks. Dengan menghapusnya, model dapat lebih fokus pada kata-kata yang lebih bermakna dan informatif.
"""

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Melakukan normalisasi dengan Normalizer
normalizer = Normalizer()
tfidf_norm = normalizer.fit_transform(tfidf_matrix)

"""TF-IDF yang sudah dinormalisasi menggunakan Normalizer berfungsi untuk setiap baris dalam matriks ini sekarang mewakili dokumen, dan panjang vektor untuk setiap dokumen adalah 1.

# Model Development : Content based filtering
"""

# membuat model menggunakan cosine similarity
similarity_cb = cosine_similarity(tfidf_norm)
similarity_cb

"""Cosine similarity adalah metrik yang digunakan untuk mengukur kemiripan antara dua vektor non-nol dalam ruang produk skalar. Dalam konteks pengolahan bahasa alami (NLP).

* Bagaimana cara kerjanya?

Setiap dokumen diubah menjadi vektor dalam ruang berdimensi tinggi, dengan setiap dimensi mewakili kata unik. Cosine similarity digunakan untuk mengukur kemiripan antara dua vektor dengan menghitung kosinus sudut di antara keduanya. Nilai cosine similarity berada dalam rentang -1 hingga 1:

1: Menunjukkan bahwa kedua vektor (dokumen) sangat mirip atau identik, dengan sudut antara keduanya adalah 0 derajat.

0: Menunjukkan bahwa kedua vektor (dokumen) tidak terkait sama sekali atau saling tegak lurus, dengan sudut antara keduanya adalah 90 derajat.

-1: Menunjukkan bahwa kedua vektor (dokumen) sangat berlawanan, dengan sudut antara keduanya adalah 180 derajat.

**Karena vektor TF-IDF yang sudah dinormalisasi biasanya hanya memiliki nilai positif (atau nol), maka nilai cosine similarity-nya akan berkisar antara 0 dan 1.**
"""

# Menyimpan nilai simalarity ke dalam dataframe
similarity_df = pd.DataFrame(similarity_cb, index=df['title'], columns=df['title'])

"""Menyimpan perhitungan cosine similarity ke dalam dataframe untuk melihat nilai kemiripan konten pada film

# Testing Model
"""

def recommend_movies(title, n=10):
    if title not in similarity_df.columns:
        return f"Judul film '{title}' tidak ditemukan."

    similar_movies = similarity_df[title].sort_values(ascending=False)[1:n+1]
    return pd.DataFrame({
        'Rekomendasi': similar_movies.index,
        'Skor Similarity': similar_movies.values
    })

# Film yang mirip dilan
recommend_movies('Dilan 1991', 10)

"""Dari testing model untuk Rekomendasi film yang mirip dengan dilan 1991 yaitu ada Milea dan Dilan 1990 yang merupakan film yang memiliki keterkaitan dengan dilan 1991 dengan kemiripan 0.49 dan 0.42 , lalu selanjutnya ada Kera Sakti	 dengan skor similarity 0.12.

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