# Laporan Proyek Machine Learning Terapan: Sistem Rekomendasi Film Indonesia — Nabilah Wanara

## Domain Proyek

**Domain:** Entertainment / Film Recommendation System  
**Judul:** Sistem Rekomendasi Film Indonesia Menggunakan Content-Based Filtering


## Latar Belakang

Di tengah pesatnya transformasi digital, industri perfilman Indonesia menunjukkan pertumbuhan yang signifikan dengan ratusan film baru yang dirilis setiap tahun. Namun, banyaknya pilihan justru memunculkan tantangan tersendiri bagi penonton, yakni kesulitan dalam menemukan film yang benar-benar sesuai dengan preferensi mereka. Situasi ini dikenal sebagai information overload, yaitu kondisi di mana pengguna kewalahan oleh banyaknya informasi yang tersedia (Bawden & Robinson, 2009).

Untuk menjawab tantangan tersebut, sistem rekomendasi hadir sebagai solusi yang efektif dalam membantu pengguna menavigasi konten yang relevan dengan minat mereka. Ricci et al. (2015) menyebutkan bahwa sistem rekomendasi yang dirancang dengan baik dapat meningkatkan tingkat kepuasan pengguna hingga 35% dan mendorong keterlibatan pengguna pada platform hingga 60%. Dalam konteks perfilman Indonesia, teknologi ini dapat memainkan peran strategis dalam memperluas jangkauan film lokal dan mendorong apresiasi terhadap karya-karya sineas dalam negeri.

Salah satu pendekatan yang banyak digunakan dalam pengembangan sistem rekomendasi adalah Content-Based Filtering (CBF). Metode ini mengandalkan analisis karakteristik konten, seperti genre, sinopsis, durasi, hingga nama sutradara, untuk menentukan kesamaan antar film dan merekomendasikan film serupa kepada pengguna. Pazzani & Billsus (2007) menunjukkan bahwa pendekatan CBF sangat efektif, terutama dalam domain film, dan dapat menghasilkan rekomendasi yang akurat meski data interaksi pengguna terbatas. Ketika dikombinasikan dengan teknik Natural Language Processing (NLP), pendekatan ini semakin kuat dalam memahami makna dari teks deskripsi film dan meningkatkan relevansi hasil rekomendasi.

Pengembangan sistem rekomendasi berbasis konten ini sangat relevan untuk mendukung ekosistem digital Indonesia, khususnya bagi platform streaming lokal, layanan bioskop daring, maupun aplikasi hiburan lainnya. Dengan sistem yang lebih personal dan kontekstual, pengguna tidak hanya terbantu dalam menemukan film yang sesuai, tetapi juga terlibat lebih dalam dalam ekosistem perfilman nasional.

---

## Business Understanding

### Problem Statements

* Bagaimana merancang sistem yang mampu merekomendasikan film Indonesia berdasarkan kesamaan konten?
* Sejauh mana efektivitas sistem rekomendasi dalam menghasilkan saran yang relevan, diukur menggunakan metrik evaluasi standar?


### Goals

* Mengembangkan sistem rekomendasi film Indonesia dengan pendekatan content-based filtering. **content-based filtering**.
* Mengukur kinerja sistem menggunakan metrik evaluasi **Precision@5**.

### Solution Statements

* Menerapkan  **TF-IDF Vectorizer** pada kolom gabungan yang mencakup `title`, `description`, dan `genre` untuk mengekstraksi fitur teks.
* Merancang fungsi rekomendasi yang mampu menampilkan lima film teratas berdasarkan nilai **cosine similarity**.

---

## Data Understanding

Dataset yang digunakan dalam proyek ini diambil dari [Kaggle-IMDB Indonesian Movies](https://www.kaggle.com/datasets/dionisiusdh/imdb-indonesian-movies). Dataset ini menjadi dasar utama untuk membangun dan menguji sistem rekomendasi berbasis konten.

Struktur Data :

* **Jumlah data:** 1272 film
* **Jumlah fitur:** 11 kolom

**Deskripsi Variabel:**

![image](https://github.com/user-attachments/assets/330226bf-d9ca-4695-b1f3-41f3261da358)

* `title` : Judul dari film       
* `year` : Tahun rilis film          
* `description` : Deskripsi film   
* `genre` : Genre film        
* `rating` : kategori rating film       
* `users_rating` : rating dari user  
* `votes` : Jumlah suara atau ulasan yang diberikan untuk film          
* `languages` : Bahasa dalam film      
* `directors` : Sutradara pada film     
* `actors` : Pemeran dalam film
* `runtime` : Durasi film     

---
## Data Cleaning
* Nilai kosong :
  + `description` (432 nilai kosong): Diisi dengan nilai 'unknown' untuk mempertahankan data yang tetap berguna dalam analisis.
  + `genre` (36 nilai kosong): Diisi dengan 'unknown' agar tetap dapat digunakan dalam sistem rekomendasi.
  + `rating`(896 nilai kosong): Diisi dengan 'unrated'. Selain itu, kategori rating diformulasikan ulang dari 11 jenis menjadi 5 kategori utama untuk menyederhanakan analisis.
  + `directors`(7 nilai kosong): Diisi dengan 'unknown' untuk menjaga kelengkapan informasi film.
  + `runtime` (403 nilai kosong): Nilai kosong digantikan dengan 'unknown' karena informasi durasi tetap relevan bagi pengguna.
 
* Nilai duplikasi : Tidak ditemukan data duplikat dalam dataset. 
* Mengubah tipe data pada kolom :
  + `votes` : Tipe data diubah dari object menjadi integer untuk memungkinkan analisis numerik lebih lanjut.

---
## Exploration Data Analysis (EDA)
### Univariate EDA
* Distribusi film berdasarkan tahun  
  ![image](https://github.com/user-attachments/assets/9f93847d-36ea-4fc5-9139-0329420e6017)
  
Analisis ini dilakukan untuk mengamati tren produksi film Indonesia dari waktu ke waktu. Dengan memvisualisasikan jumlah film yang dirilis setiap tahunnya, dapat dievaluasi apakah industri perfilman Indonesia menunjukkan pola pertumbuhan, stagnasi, atau penurunan. Berdasarkan hasil plot, terlihat adanya lonjakan produksi film setelah tahun-tahun tertentu, yang mencerminkan kemajuan signifikan dalam perkembangan industri film nasional.

* Genre film terbanyak pada data  
  ![image](https://github.com/user-attachments/assets/d78569f7-66c6-4794-bb56-bcac5883fdb1)
  
Analisis ini bertujuan untuk mengenali genre film yang paling populer atau paling sering diproduksi di Indonesia. Dengan menghitung frekuensi kemunculan masing-masing genre dalam dataset, dapat diidentifikasi genre-genre yang mendominasi. Hasil analisis menunjukkan bahwa genre seperti drama, komedi, dan horor merupakan yang paling menonjol, sehingga informasi ini dapat dimanfaatkan sebagai landasan dalam pengembangan sistem rekomendasi yang lebih relevan dan sesuai dengan preferensi penonton.

* Distribusi user rating  
  ![image](https://github.com/user-attachments/assets/c056c465-7552-49e1-898c-d909f547bffd)
  
Distribusi ini memberikan gambaran mengenai bagaimana pengguna menilai film-film Indonesia. Melalui sebaran nilai pada kolom `users_rating`, terlihat bahwa mayoritas film memperoleh rating antara 6 hingga 7. Pola ini tidak hanya mencerminkan persepsi umum penonton, tetapi juga berperan penting dalam menetapkan ambang batas (threshold) relevansi saat proses evaluasi model dilakukan.
* Kategori rating film pada data  
  ![image](https://github.com/user-attachments/assets/ffdf56cc-ac1a-4d8c-99d2-e1fbfd56e494)
  
Kategori rating merujuk pada klasifikasi usia atau konten film (seperti SU, R, D, dan sebagainya). Analisis ini bertujuan untuk melihat distribusi film berdasarkan kategori rating tersebut. Informasi ini penting untuk memastikan bahwa sistem rekomendasi dapat menyaring dan menyesuaikan rekomendasi film sesuai dengan batasan usia atau preferensi pengguna, sehingga hasil rekomendasi tetap relevan dan aman bagi berbagai kelompok penonton.

### Multivariate EDA
* Film populer pada masing masing genre  
  ![image](https://github.com/user-attachments/assets/3c99c0cc-7d7a-45a4-af6c-b221f0ed427a)
  
Analisis ini mengeksplorasi hubungan antara tingkat popularitas (ditinjau dari user_rating) dan genre film. Tujuan utamanya adalah untuk mengidentifikasi genre-genre yang cenderung memiliki film dengan penilaian tinggi dari pengguna. Informasi ini sangat berguna dalam menentukan genre mana yang sebaiknya menjadi fokus utama dalam pengembangan sistem rekomendasi, agar hasil yang diberikan lebih sesuai dengan preferensi dan minat penonton.

* Genre dengan user rating tertinggi  
  ![image](https://github.com/user-attachments/assets/70935be2-0c32-4be2-b4cf-34c16e2daa6f)

Analisis ini bertujuan untuk menemukan genre dengan rata-rata penilaian pengguna tertinggi, di mana genre 'History' muncul sebagai yang paling menonjol. Genre dengan rating rata-rata tinggi umumnya mencerminkan kualitas konten yang lebih baik dan tingkat kepuasan penonton yang tinggi, sehingga dapat menjadi acuan dalam penyusunan strategi rekomendasi yang lebih efektif.

---

## Data Preparation

### Tahapan:
* Membuat kolom `combined` berisi gabungan:

  ```python
  df['combined'] = df['title'] + ' ' + df['description'] + ' ' + df['genre']
  ```
* Melakukan **TF-IDF vectorization** pada kolom `combined` menggunakan **stop words bahasa Inggris**.  
  ```python
  tfidf = TfidfVectorizer(stop_words='english')
  tfidf_matrix = tfidf.fit_transform(df['combined'])
  ```
  
* Melakukan **normalisasi hasil TF-IDF** agar vektor memiliki panjang seragam sebelum dihitung similarity-nya.  
  ```python
  normalizer = Normalizer()
  tfidf_norm = normalizer.fit_transform(tfidf_matrix)
  ```

---

## Modeling and Result

### Model : Content-Based Filtering

* Menghitung **cosine similarity** antar film berdasarkan vektor TF-IDF berikut ini Formula nya :  
  ![image](https://github.com/user-attachments/assets/118fcd36-baac-48f8-883f-ffe483b89a2b)  
    Keterangan:  
  ```
  𝑠𝑖𝑚(𝐴, 𝐵) = nilai similaritas dari item A dan item B
  𝑛(𝐴) = banyaknya fitur konten item A 
  𝑛(𝐵) = banyaknya fitur konten item B 
  𝑛(𝐴 ∩ 𝐵)  = banyaknya fitur konten yang terdapat pada item A dan juga terdapat pada item B
  ```

* Hasil dari perhitungan **cosine similarity** disimpan ke dalam dataframe untuk menilai kemiripan konten film
  ```python
  similarity_df = pd.DataFrame(similarity_cb, index=df['title'], columns=df['title'])
  ```
  
#### Kelebihan:
1. Tidak Bergantung pada Data User
  Sistem hanya memerlukan informasi dari konten film itu sendiri—seperti judul, deskripsi, dan genre—tanpa memerlukan riwayat interaksi pengguna.

2. Mampu Merekomendasikan Film Baru
  Film yang belum pernah ditonton oleh siapa pun tetap dapat direkomendasikan, selama memiliki informasi konten yang memadai.

3. Personalisasi Berdasarkan Karakteristik Film
  Rekomendasi dihasilkan berdasarkan kemiripan konten antar film, sehingga jika preferensi pengguna diketahui, hasilnya akan cenderung lebih relevan dan sesuai minat.

4. Implementasi yang Sederhana dan Efisien
  Dapat dibangun dengan teknik dasar seperti TF-IDF vectorization dan cosine similarity, tanpa perlu algoritma pelatihan kompleks.

5. Tidak Terpengaruh Masalah Cold-Start untuk Pengguna Baru
  Karena tidak memerlukan data historis pengguna, sistem tetap mampu memberikan rekomendasi yang relevan bagi pengguna yang baru pertama kali menggunakan layanan.

#### Kekurangan:
1. Terbatas pada Informasi Item Saja
  Sistem hanya mengandalkan atribut dari film (seperti deskripsi dan genre), tanpa mempertimbangkan preferensi atau perilaku pengguna lain. Akibatnya, film dengan genre berbeda yang sebenarnya disukai oleh pengguna serupa bisa terlewatkan.

2. Rekomendasi Kurang Variatif
  Karena fokus pada kesamaan konten, sistem cenderung merekomendasikan film yang sangat mirip satu sama lain. Hal ini dapat membuat pengguna merasa jenuh karena tidak mendapatkan keberagaman pilihan.

3. Tidak Menangkap Popularitas Secara Kolektif
  Sistem tidak mampu mendeteksi film yang sedang tren atau populer di kalangan banyak pengguna, karena tidak melibatkan data komunitas atau rating secara agregat.

4. Ketergantungan pada Kualitas dan Kelengkapan Fitur Konten
  Jika atribut seperti deskripsi atau genre film tidak lengkap, tidak konsisten, atau berkualitas rendah, maka akurasi sistem rekomendasi akan menurun secara signifikan.

5. Sensitif terhadap Format dan Struktur Teks
  Sistem rentan terhadap variasi kata atau penyusunan deskripsi. Jika deskripsi terlalu singkat, tidak informatif, atau tidak distandarisasi, maka kemiripan antar film yang sebenarnya relevan bisa tidak terdeteksi dengan baik oleh cosine similarity.

---

### Result

Contoh rekomendasi untuk film **Dilan 1991**:

| Rekomendasi            | Skor Similarity |
| :--------------------- | :-------------- |
| Milea                  | 0.489681        |
| Dilan 1991             | 0.424312        |
| Kera Sakti	           | 0.117860        |
| Serigala Terakhir      | 0.106119        |
| The Tarix Jabrix 3     | 0.085149        |

**Insight:**  
Rekomendasi teratas yang dihasilkan mencakup film-film sekuel dan film dengan genre serta deskripsi yang serupa, yang menunjukkan bahwa sistem berhasil mengidentifikasi kemiripan konten dengan baik.

---
## Model Evaluation

### Visualisasi matriks similarity  
![image](https://github.com/user-attachments/assets/8d746f96-09e1-4a94-a1d5-717d86d4ba8a)  

Matriks similarity menunjukkan rendahnya kemiripan antar sebagian besar film berdasarkan konten teks TF-IDF (banyak nilai 0.00). Ini menyiratkan konten film yang sangat beragam/unik.

Namun, terdapat poin kemiripan menarik seperti "Aku tahu kapan kamu mati" dengan "4 Mantan" (0.04) yang menjadi kandidat utama untuk rekomendasi berbasis konten dan menunjukkan model berhasil menangkap koneksi khusus.


### Precision\@5  
![image](https://github.com/user-attachments/assets/482b7b9a-747d-45cc-838c-b562dcfcb576)

Untuk mengukur kualitas rekomendasi, dilakukan evaluasi **Precision\@5**, yaitu proporsi film relevan dalam 5 rekomendasi teratas untuk sebuah film.

**Definisi relevan**:
Film dengan **users\_rating ≥ 6.0** dianggap relevan.

### Hasil Precision\@5

* **Average Precision\@5 = 0.48**  
  Artinya, rata-rata dalam 5 film rekomendasi teratas, sekitar **2-3 film** benar-benar relevan.

---

## Kesimpulan

1. **Business Problem pertama:**  
  Sistem ini berhasil merekomendasikan film berdasarkan kemiripan konten tanpa memerlukan data interaksi pengguna. Rekomendasi yang dihasilkan menunjukkan hubungan yang erat antara deskripsi, genre, dan judul film, seperti contohnya rekomendasi Dilan 1991 dan Milea untuk Dilan 1990. Hal ini membuktikan bahwa metode content-based filtering efektif dalam mengenali kesamaan konten antar film.

2. **Business Problem kedua:**  
  Model ini berhasil mencapai nilai Average Precision@5 sebesar 0.48, yang menunjukkan bahwa rata-rata 2 hingga 3 dari 5 film yang direkomendasikan relevan dengan kriteria user_rating ≥ 6.0. Nilai precision ini cukup baik sebagai baseline untuk sistem rekomendasi berbasis konten, terutama mengingat sistem ini tidak mengandalkan data interaksi pengguna (seperti yang digunakan dalam sistem collaborative filtering).

3. **Insight tambahan dari EDA:**  
  Dari analisis eksplorasi data (EDA), ditemukan bahwa genre drama, komedi, dan horror mendominasi industri perfilman Indonesia, sementara genre history memiliki rata-rata user rating tertinggi. Temuan ini memberikan wawasan yang berguna untuk pengembangan sistem rekomendasi ke depan, dengan mempertimbangkan faktor genre lebih dalam untuk meningkatkan relevansi rekomendasi bagi pengguna.

**Secara keseluruhan, sistem rekomendasi ini siap diimplementasikan pada platform film Indonesia berbasis streaming atau katalog digital untuk membantu pengguna menemukan film yang sesuai preferensi mereka secara lebih cepat dan relevan.**

---
## Referensi 
1. Bawden, D., & Robinson, L. (2009). The dark side of information: overload, anxiety and other paradoxes and pathologies. Journal of Information Science, 35(2), 180–191. 
2. Ricci, F., Rokach, L., & Shapira, B. (2015). Recommender Systems Handbook. Springer. Diakses dari[https://link.springer.com/chapter/10.1007/978-1-0716-2197-4_1]
3. Pazzani, M. J., & Billsus, D. (2007). Content-based recommendation systems. In The adaptive web (pp. 325-341). Springer. Diakses dari [https://link.springer.com/chapter/10.1007/978-3-540-72079-9_10]
4. Aggarwal, C. C. (2016). Recommender systems: the textbook. Springer. Diakses dari [https://link.springer.com/book/10.1007/978-3-319-29659-3]
5. Manning, C. D., Raghavan, P., & Schütze, H. (2008). Introduction to information retrieval. Cambridge University Press. Diakses dari [https://www.cis.uni-muenchen.de/~hs/teach/14s/ir/pdf/19web.pdf]
6. Scikit-learn Documentation. (2023). TfidfVectorizer. Diakses dari [https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html]
7. Badan Ekonomi Kreatif Indonesia. (2020). Data Statistik dan Hasil Survei Ekonomi Kreatif. Jakarta: BEKRAF. [https://kemenparekraf.go.id/publikasi-statistik-ekonomi-kreatif/statistik-ekonomi-kreatif-2020]
---
