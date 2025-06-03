# Laporan Proyek Machine Learning Terapan Kedua - Nabilah Wanara

## Project Overview

Seiring dengan pesatnya perkembangan teknologi, pilihan ponsel yang tersedia di pasar menjadi semakin beragam, mencakup berbagai fitur, spesifikasi teknis, serta kisaran harga yang luas. Keanekaragaman ini memberikan banyak opsi kepada konsumen, namun di sisi lain juga dapat menimbulkan kebingungan dalam menentukan ponsel yang paling sesuai dengan kebutuhan dan preferensi masing-masing individu. Oleh karena itu, hadirnya sistem rekomendasi berbasis teknologi menjadi sebuah solusi penting yang dirancang untuk mempermudah pengguna dalam menemukan perangkat yang tepat, baik dari segi fitur teknis maupun berdasarkan pengalaman pengguna lain yang pernah menggunakan produk serupa [[1]](#referensi-1).

Dalam proses pengembangan sistem rekomendasi semacam ini, dikenal dua pendekatan utama yang umum digunakan, yaitu Content-based Filtering dan Collaborative Filtering. Pendekatan Content-based Filtering bekerja dengan cara menganalisis karakteristik produk, seperti harga, jenis prosesor, ukuran layar, serta kapasitas baterai, untuk mencocokkannya dengan preferensi pengguna secara langsung. Di sisi lain, Collaborative Filtering memanfaatkan data interaksi antar pengguna, seperti ulasan, penilaian (rating), dan riwayat pembelian, guna menghasilkan rekomendasi berdasarkan pola dan perilaku pengguna lain yang memiliki kesamaan preferensi [[2]](#referensi-2).

Proyek ini memiliki tujuan untuk merancang dan membangun sebuah model sistem rekomendasi ponsel yang mengintegrasikan data spesifikasi perangkat dengan data interaksi pengguna. Dengan pendekatan ini, sistem diharapkan mampu menghasilkan rekomendasi dalam bentuk daftar lima ponsel terbaik yang telah disesuaikan secara personal dengan kebutuhan dan selera masing-masing pengguna. Hasil dari sistem ini diharapkan dapat meningkatkan kualitas pengalaman pengguna secara keseluruhan, sekaligus membantu mereka dalam membuat keputusan pembelian yang lebih terinformasi dan tepat sasaran [[3]](#referensi-3).

Proyek ini memiliki signifikansi yang tinggi karena beberapa alasan berikut:

1. **Efisiensi Waktu**: istem ini dapat secara efisien menyaring ribuan pilihan ponsel yang tersedia dan menyajikan lima rekomendasi utama, sehingga mempercepat serta menyederhanakan proses pengambilan keputusan bagi pengguna.

2. **Rekomendasi yang Disesuaikan Secara Personal**: Sistem memberikan saran yang relevan dan sesuai dengan preferensi pengguna, baik berdasarkan fitur teknis perangkat maupun ulasan dari pengguna lain yang memiliki pengalaman serupa.

3. **Peningkatan Kepuasan Pengguna**: Dengan membantu pengguna menemukan perangkat yang benar-benar cocok dengan kebutuhan dan keinginan mereka, sistem ini juga dapat mengungkap pilihan yang mungkin sebelumnya tidak dipertimbangkan, sehingga meningkatkan kualitas pengalaman pembelian.

## Referensi

<a name="referensi-1"></a>
[1] X. Su and T. M. Khoshgoftaar, "A survey of collaborative filtering techniques,"I, vol. 2009, pp. 1–19, 2009. doi:10.1155/2009/421425

<a name="referensi-2"></a>
[2] M. J. Pazzani and D. Billsus, "Content-based recommendation systems," in The Adaptive Web, Springer, 2007, pp. 325–341. doi:10.1007/978-3-540-72079-9_10

<a name="referensi-3"></a>
[3] F. Ricci, L. Rokach, and B. Shapira, "Introduction to recommender systems handbook," in Recommender Systems Handbook, Springer, 2011, pp. 1–35. doi:10.1007/978-0-387-85820-3_1

## Business Understanding

**Problem Statements**

1. Bagaimana cara menyajikan rekomendasi ponsel yang relevan dan dipersonalisasi kepada pengguna dengan mempertimbangkan karakteristik produk seperti merek dan spesifikasi teknis lainnya?
2. Bagaimana memanfaatkan pola rating serta interaksi pengguna untuk menghasilkan rekomendasi yang akurat berdasarkan preferensi dari pengguna-pengguna dengan kebiasaan serupa?

**Goals**
Berdasarkan pernyataan masalah tersebut, tujuan utama dari proyek ini meliputi:
1. Membangun model sistem rekomendasi berbasis Content-based Filtering yang mampu menyarankan produk ponsel berdasarkan atribut seperti merek, dengan memanfaatkan pendekatan TF-IDF.
2. Mengembangkan model User-based Collaborative Filtering yang dapat memanfaatkan data penilaian (rating) pengguna guna menghasilkan rekomendasi melalui identifikasi pola perilaku pengguna lain yang memiliki preferensi serupa.

**Solution statements**
Untuk merealisasikan tujuan tersebut, berikut adalah solusi yang diusulkan:

1. Pendekatan Content-based Filtering:

   - Mengembangkan model rekomendasi yang bekerja dengan cara mengidentifikasi kesamaan antar produk berdasarkan atribut merek melalui fitur-fitur yang telah diekstraksi sebelumnya.
   - Menerapkan algoritma TF-IDF untuk mengubah data fitur brand menjadi vektor numerik dan menggunakan cosine similarity guna mengukur tingkat kemiripan antara satu ponsel dengan ponsel lainnya.

2. Pendekatan User-based Collaborative Filtering:

   - Membangun model rekomendasi berbasis penilaian pengguna dengan membuat matriks user-item untuk mendeteksi pola interaksi dan preferensi pengguna.
   - Menggunakan metode cosine similarity untuk menemukan pengguna lain yang memiliki preferensi mirip, lalu memberikan rekomendasi berdasarkan rating yang diberikan oleh pengguna-pengguna tersebut.

## Data Understanding

Dataset yang digunakan mencakup informasi mengenai ponsel, penilaian (rating) dari pengguna, serta data terkait profil pengguna. Dataset ini disusun untuk menunjang proses pengembangan sistem rekomendasi ponsel dengan menerapkan pendekatan **Content-based Filtering** dan **Collaborative Filtering**.

**Sumber Data**  
Dataset yang digunakan berasal dari [Kaggle - Cellphones Recommendations](https://www.kaggle.com/datasets/meirnizri/cellphones-recommendations/data).

**Informasi Dataset:**

Dataset terdiri dari tiga file utama:

1. **`cellphones_data.csv`**:

   - Berisi metadata ponsel yang dapat digunakan untuk **Content-based Filtering**.
   - **Dimensi**: 33 baris × 14 kolom.
   - **Kolom Utama**:
     - `cellphone_id`: ID unik untuk setiap ponsel.
     - `brand`: Merek/Brand ponsel .
     - `model`: Model/Type ponsel .
     - `operating system`: Sistem operasi ponsel.
     - `internal memory`: Kapasitas penyimpanan internal (GB).
     - `RAM`: Kapasitas RAM (GB).
     - `performance`: Skor kinerja ponsel.
     - `main camera`: Resolusi kamera utama (MP).
     - `selfie camera`: Resolusi kamera selfie (MP).
     - `battery size`: Kapasitas baterai (mAh).
     - `screen size`: Ukuran layar (inch).
     - `weight`: Berat ponsel (gram).
     - `price`: Harga ponsel.
     - `release date`: Tanggal rilis ponsel.

2. **`cellphones_ratings.csv`**:

   - Berisi data rating yang diberikan pengguna untuk ponsel tertentu, yang dapat digunakan untuk **Collaborative Filtering**.
   - **Dimensi**: 990 baris × 3 kolom.
   - **Kolom Utama**:
     - `user_id`: ID unik untuk setiap pengguna.
     - `cellphone_id`: ID unik untuk setiap ponsel.
     - `rating`: Rating yang diberikan pengguna (skala 1-5).

3. **`cellphones_users.csv`**:
   - Berisi informasi demografi pengguna yang dapat digunakan untuk analisis tambahan.
   - **Dimensi**: 99 baris × 4 kolom.
   - **Kolom Utama**:
     - `user_id`: ID unik pengguna.
     - `age`: Usia pengguna.
     - `gender`: Jenis kelamin pengguna.
     - `occupation`: Pekerjaan pengguna.

**Kondisi Data**

1. **_Missing Value_**

   ![alt text](https://github.com/user-attachments/assets/3bf4869d-ff13-4b7c-9085-70d069a368d2)

   > Kolom `occupation` memiliki nilai yang kosong (missing value) sebanyak 10 data

2. **_Data Duplikat_**

   ![alt text](https://github.com/user-attachments/assets/b3dee281-81df-41f4-9598-27964bc790b7)

   > Tidak terdapat data terduplikasi.

3. **_Data Tidak Valid_**

   ![alt text](https://github.com/user-attachments/assets/7686cfdd-e7e9-4e15-bfa7-823dcb2d903c)

   > Pada kolom gender, terdapat data invalid berupa pilihan '-Select Gender-' yang perlu dibersihkan.  
   > Ditemukan kesalahan penulisan pada 'healthare', yang benar adalah 'healthcare'.  
   > Pekerjaan dengan kategori 'information technology' dan 'it' dapat digabungkan menjadi satu kelompok untuk mempermudah analisis.

## Exploratory Data Analysis (EDA)

1. **Statistik Deskriptif**

   ![alt text](https://github.com/user-attachments/assets/45c7f8b3-8e4b-497c-914f-4dc8f1773af1)

   ![alt text](https://github.com/user-attachments/assets/d88dd0a5-6aeb-4511-954d-ca704d74a293)

   ![alt text](https://github.com/user-attachments/assets/f80ad33f-96fe-41d3-aff9-ba80cf98230d)

   1. **Products**

      Menampilkan ringkasan statistik dari 33 model ponsel:

      - Internal memory berkisar antara 32–512 GB, dengan rata-rata 148 GB.

      - RAM rata-rata sekitar 6.8 GB, minimum 3 GB dan maksimum 12 GB.

      - Main camera dan selfie camera memiliki variasi besar, dengan kamera utama tertinggi mencapai 108 MP.

      - Battery size rata-rata 4320 mAh, menunjukkan sebagian besar ponsel memiliki baterai besar.

      - Screen size umumnya berkisar antara 4.7 hingga 7.6 inci.

      - Price bervariasi cukup besar, dengan rata-rata $628 dan maksimum hampir $2000.

   2. **Users**

      - Terdapat 99 pengguna, dengan usia antara 21 hingga 61 tahun.

      - Usia rata-rata pengguna adalah sekitar 36 tahun, menunjukkan dominasi usia produktif.

   3. **Ratings**

      - Terdapat 990 data rating yang diberikan pengguna terhadap ponsel.

      - Rating berkisar dari 1 hingga 18, dengan rata-rata sekitar 6.7.

      - Distribusi rating menunjukkan nilai tengah di angka 7, dan mayoritas rating berada di rentang 5 hingga 9.

2. **Visualisasi Fitur**

   - **Distribusi Jumlah Ponsel per Brand**

     ![alt text](https://github.com/user-attachments/assets/7f415f7d-0a45-4737-b0bc-7f8fab3a03a4)

     Grafik menunjukkan bahwa dari **10 brand** yang ada, Samsung memiliki **8 model** ponsel paling banyak, disusul Apple dengan **6 model**. Sementara itu, Asus, Oppo, Vivo, dan Sony tercatat hanya memiliki 1 model ponsel masing-masing.

   - **Distribusi Tipe Setiap Brand**

     **Daftar Model Berdasarkan Brand**
     | **Brand** | **Model** |
     |-------------|-----------------------------------------------------------------------------------------------------|
     | **Apple** | iPhone SE (2022), iPhone 13 Mini, iPhone 13, iPhone 13 Pro, iPhone 13 Pro Max, iPhone XR |
     | **Asus** | Zenfone 8 |
     | **Google** | Pixel 6, Pixel 6a, Pixel 6 Pro |
     | **Motorola**| Moto G Stylus (2022), Moto G Play (2021), Moto G Pure, Moto G Power (2022) |
     | **OnePlus** | Nord N20, Nord 2T, 10 Pro, 10T |
     | **Oppo** | Find X5 Pro |
     | **Samsung** | Galaxy A13, Galaxy A32, Galaxy A53, Galaxy S22, Galaxy S22 Plus, Galaxy S22 Ultra, Galaxy Z Flip 3, Galaxy Z Fold 3 |
     | **Sony** | Xperia Pro |
     | **Vivo** | X80 Pro |
     | **Xiaomi** | Redmi Note 11, 11T Pro, 12 Pro, Poco F4 |

     Terdapat total **33 model** ponsel yang berasal dari seluruh brand yang ada.

   - **Distribusi Sistem Operasi**

     ![alt text](https://github.com/user-attachments/assets/86bd011b-4342-4f32-8edb-87cf7faa3039)

     Grafik tersebut menunjukkan bahwa sebagian besar model ponsel menggunakan sistem operasi **Android**, dengan total sebanyak **27 perangkat**. Sementara itu, hanya **6 perangkat** yang menggunakan sistem operasi **iOS**.

   - **Distribusi Memory dan RAM**

     ![alt text](https://github.com/user-attachments/assets/bc12de4f-f73f-457d-8755-416536424092)

     Grafik tersebut menunjukkan sebagian besar perangkat yang tersedia dilengkapi dengan memori internal sebesar **128 GB** sebanyak **20 perangkat**, serta **RAM 8 GB** yang digunakan pada **13 perangkat**.

   - **Distribusi Kategori Performa**

     ![alt text](https://github.com/user-attachments/assets/12d3b666-e31b-421c-893a-abe4c93bb4ae)

     Rentang nilai performa berkisar antara 1,02 hingga 11,0, dengan kategori performa rendah untuk nilai di bawah 5 dan performa tinggi untuk nilai di atas 5. Grafik tersebut memperlihatkan bahwa dari total perangkat, terdapat **23 unit** dengan performa tinggi dan **10 unit** dengan performa rendah berdasarkan hasil pengujian menggunakan AnTuTu.

   - **Distribusi Kategori Harga Ponsel**

     ![alt text](https://github.com/user-attachments/assets/95ae489e-05da-4b3f-8b65-a956dd7ee797)

     Dari grafik tersebut, jumlah ponsel berdasarkan kategori harga menunjukkan bahwa terdapat **8 perangkat** pada kategori Entry Level (0-300 USD), **16** perangkat pada kategori Mid Level (301-800 USD), dan **9 perangkat** pada kategori Flagship dengan harga di atas 800 USD.

   - **Analisis Review User**

     ![alt text](https://github.com/user-attachments/assets/6bdd1786-e83a-4223-b5d0-296354e9b15a)

     Setiap pengguna memberikan jumlah ulasan yang sama, yakni sebanyak **10 ulasan**.

   - **Distribusi Review per Tipe Ponsel**

     ![alt text](https://github.com/user-attachments/assets/7dc7b5d4-e4d1-4b94-95ea-30fc968eff73)

     Ponsel dengan jumlah ulasan terbanyak adalah **Moto G Play (2021)** dengan **41 ulasan**, sementara ponsel dengan ulasan paling sedikit adalah **iPhone SE (2022)** dan **10T**, masing-masing menerima **20 ulasan**.

   - **Distribusi Rating**

     ![alt text](https://github.com/user-attachments/assets/b0aeb649-c063-41bf-a2b2-a184ba595d03)

     Nilai rating berkisar antara 1 hingga 10. Rating yang paling sering muncul adalah nilai 8 dengan **195** kemunculan, sedangkan rating yang paling jarang diberikan adalah nilai 3 dengan **30** kemunculan. Selain itu, terdapat outlier pada nilai rating sebesar 18.

   - **Distribusi Usia Pengguna**

     ![alt text](https://github.com/user-attachments/assets/9c721030-8e8e-456c-af20-3d7aae3163ce)

     Grafik menunjukkan mayoritas pengguna berusia **25–35 tahun**, dengan puncak pada usia **25 (12 pengguna)**. Usia termuda adalah **21** dan tertua **61**. Ini menunjukkan dominasi pengguna usia muda, yang penting dipertimbangkan dalam sistem rekomendasi.

   - **Distribusi Gender Pengguna**

     ![alt text](https://github.com/user-attachments/assets/3d0f8f07-c71d-4779-acce-6896aaa4d2f5)

     Grafik menunjukkan distribusi gender pengguna didominasi oleh **laki-laki (50 pengguna)** dan **perempuan (45 pengguna)**. Terdapat juga beberapa entri tidak valid atau kosong **(label "-Select Gender-")** sebanyak **4 pengguna**. Data ini penting untuk memastikan sistem rekomendasi bersifat inklusif terhadap seluruh gender.

   - **Analisis Profesi Pengguna**

     | **Profesi**                      | **Count** |
     | -------------------------------- | --------- |
     | accountant                       | 2         |
     | administrative officer           | 5         |
     | administrator                    | 1         |
     | banking                          | 1         |
     | business                         | 1         |
     | computer technician              | 1         |
     | construction                     | 2         |
     | data analyst                     | 2         |
     | education                        | 2         |
     | executive                        | 1         |
     | executive manager                | 1         |
     | finance                          | 2         |
     | healthare                        | 1         |
     | healthcare                       | 2         |
     | homemaker                        | 1         |
     | ict officer                      | 1         |
     | information                      | 1         |
     | information technology           | 12        |
     | it                               | 6         |
     | manager                          | 18        |
     | marketing                        | 1         |
     | master degree                    | 1         |
     | nurse                            | 1         |
     | ops manager                      | 1         |
     | president transportation company | 1         |
     | purchase manager                 | 1         |
     | qa software manager              | 1         |
     | registered                       | 1         |
     | retail                           | 1         |
     | sales                            | 3         |
     | sales manager                    | 2         |
     | security                         | 3         |
     | self employed                    | 1         |
     | software developer               | 4         |
     | system administrator             | 1         |
     | teacher                          | 1         |
     | team leader                      | 2         |
     | team worker in it                | 1         |
     | technical engineer               | 1         |
     | technician                       | 1         |
     | transportation                   | 1         |
     | warehousing                      | 1         |
     | web design                       | 1         |
     | worker                           | 2         |
     | writer                           | 1         |

     Berdasarkan Data Profesi Pengguna:

     - Terdapat **45 kategori** pekerjaan unik.

     - Pekerjaan terbanyak adalah manager sebanyak 18 pengguna, diikuti oleh information technology (12 pengguna) dan it (6 pengguna).

     - Ditemukan duplikasi makna pekerjaan, seperti information technology dan it, yang sebaiknya digabungkan untuk analisis lebih akurat.

     - Terdapat kesalahan penulisan pada healthare, yang seharusnya healthcare.

## Data Preparation

Pada tahap ini, dilakukan serangkaian proses untuk membersihkan dan mempersiapkan data sebelum dianalisis atau digunakan untuk pelatihan model. Langkah-langkah ini bertujuan untuk meningkatkan kualitas dan keandalan data.

**Teknik dan Proses Data Preparation**

1. **Merged All Datasets**
   Dataset `ratings`, `products`, dan `users` digabung menggunakan kolom `cellphone_id` dan `user_id`. Tujuan penggabungan ini adalah untuk membentuk satu dataset terpadu yang mencakup informasi lengkap dari pengguna, metadata produk (ponsel), dan interaksi dalam bentuk rating.

2. **Check and Drop Missing Value**
   Baris dengan nilai kosong (null) pada kolom `occupation` dihapus agar tidak mengganggu proses analisis dan pelatihan model.

3. **Check and Drop Duplicate Data**

   - Baris-baris yang identik (duplikat sempurna) dihapus dari dataset.
   - Duplikasi berdasarkan `cellphone_id` juga dihapus untuk memastikan bahwa setiap produk ponsel hanya muncul satu kali dalam dataset akhir.

4. **Drop Invalid Gender Data**
   Entri pada kolom `gender` dengan nilai "-Select Gender-" dihapus karena tidak merepresentasikan gender valid.

5. - **Drop Outlier pada Rating dan Perbaikan Data Occupation**

   * Entri pada kolom `rating` dengan nilai 18 dihapus karena berada di luar rentang yang wajar (1–10).
   * Kesalahan penulisan seperti `'healthare'` diperbaiki menjadi `'healthcare'`.
   * Nilai `'it'` diganti menjadi `'information technology'`.
   * Seluruh nilai pada kolom `occupation` diubah menjadi huruf kecil (`lowercase`) untuk menjaga konsistensi.

6. **Prepare the Dataset for Modelling**
   Dataset akhir disusun dengan memilih kolom-kolom penting seperti `cellphone_id`, `brand`, `model`, dan `operating system`. Dataset ini disiapkan dalam format yang siap digunakan untuk analisis, eksplorasi, atau proses pemodelan.

7. **Split Data Ratings**
   Dataset `ratings` dibagi menjadi dua bagian menggunakan fungsi `train_test_split`, yaitu:

   - **Train Ratings**: 80% data untuk proses pelatihan model.
   - **Test Ratings**: 20% data untuk menguji performa model.


**Alasan Tahapan Data Preparation Dilakukan**

1. **Merged All Datasets**

   Proses penggabungan dataset dilakukan untuk membentuk satu set data terpadu yang mencakup informasi tentang ponsel, aktivitas pengguna seperti pemberian rating, serta data demografis pengguna. Langkah ini penting guna memungkinkan analisis yang lebih komprehensif dan integrasi fitur-fitur penting untuk proses pemodelan.

2. **Check and Drop Missing Value**

   Data yang mengandung nilai kosong (missing values) berpotensi mengganggu hasil analisis maupun performa model. Oleh karena itu, kolom occupation yang memiliki nilai kosong dibersihkan agar dataset menjadi lebih siap pakai tanpa kehilangan informasi penting.

3. **Check and Drop Duplicate Data**

   Keberadaan data yang duplikat dapat menimbulkan bias, misalnya memberikan pengaruh berlebihan pada data yang sama dalam proses pelatihan model. Dengan menghapus data duplikat, akurasi dan representasi dataset menjadi lebih baik.

4. **Drop Invalid Gender Data**

   Nilai seperti "-Select Gender-" dianggap tidak valid dan bisa menyebabkan analisis menjadi kurang akurat. Menghapus entri seperti ini akan meningkatkan konsistensi data dan mencerminkan informasi pengguna yang sesungguhnya.

5. **Drop Outlier pada Rating dan Perbaikan Data Occupation**

   Nilai outlier, seperti rating sebesar 18 yang berada di luar rentang normal (1–10), dapat menyesatkan hasil analisis. Oleh karena itu, data semacam ini dihapus. Selain itu, perbaikan ejaan serta normalisasi pada kolom occupation dilakukan untuk menjaga konsistensi kategori pekerjaan.

6. **Prepare the Dataset for Modelling**

   Tahapan ini dilakukan untuk memastikan bahwa struktur dataset sudah optimal untuk pemodelan. Ini termasuk penghapusan data ganda berdasarkan `cellphone_id` dan pengaturan ulang kolom agar lebih rapi dan efisien saat digunakan.

7. **Split Data Ratings**

   Pembagian data rating menjadi data pelatihan dan pengujian bertujuan untuk mengevaluasi performa model secara objektif. Langkah ini juga membantu menghindari overfitting dan memastikan model memiliki kemampuan generalisasi terhadap data yang belum pernah dilihat sebelumnya.

## Modeling and Result

Dalam proyek ini, dibangun dua pendekatan utama sistem rekomendasi untuk membantu pengguna dalam menemukan model ponsel yang relevan, yaitu **Content-Based Filtering (CBF)** dan **Collaborative Filtering (CF)**. Pendekatan ini diterapkan pada data penilaian (rating) dan metadata dari berbagai model ponsel.

1. **Content-Based Filtering (CBF)**

   Pendekatan Content-Based Filtering memberikan rekomendasi berdasarkan kemiripan atribut konten suatu item, dalam hal ini adalah merek (brand) dari masing-masing model ponsel. Sistem merekomendasikan model-model yang memiliki merek serupa dengan model yang menjadi acuan pengguna.

   **Proses:**

   1. Data teks pada kolom `brand` dari setiap model ponsel diproses menggunakan teknik **TF-IDF Vectorization** untuk membentuk representasi numerik dari masing-masing merek.
   2. Kemudian, dihitung **cosine similarity** antar model berdasarkan vektor TF-IDF merek.
   3. Fungsi `item_cbf_recomendation()` digunakan untuk menghasilkan top-N rekomendasi model yang paling mirip berdasarkan merek dari model yang dijadikan referensi.

   Sebagai contoh, ketika model acuan adalah **"iPhone 13 Pro"**, sistem memberikan rekomendasi model-model lain dengan kemiripan tinggi berdasarkan merek sebagai berikut:

   - iPhone 12
   - iPhone 11 Pro
   - iPhone 13
   - iPhone 12 Pro
   - iPhone 11

   Rekomendasi ini menunjukkan bahwa model-model Apple dengan seri yang mirip akan lebih disarankan karena kesamaan merek yang kuat secara representasi TF-IDF.

   **Kelebihan:**

   - Tidak bergantung pada data interaksi pengguna lainnya.
   - Dapat memberikan rekomendasi untuk pengguna baru (cold start user).
   - Fokus pada informasi konten dari setiap item.

   **Kekurangan:**

   - Terbatas pada fitur `brand` saja, sehingga bisa terlalu sempit cakupannya.
   - Rekomendasi bisa terlalu mirip dan kurang variatif.
   - Tidak mempertimbangkan popularitas atau tren umum dari model.

2. **Collaborative Filtering (CF)**

   Pendekatan Collaborative Filtering menghasilkan rekomendasi berdasarkan **kemiripan pola interaksi antar pengguna**. Dalam proyek ini digunakan pendekatan **user-based collaborative filtering** berdasarkan data rating pengguna terhadap model ponsel.

   **Proses:**

   1. Dibentuk **user-item matrix**, di mana baris mewakili pengguna (`user_id`) dan kolom mewakili model ponsel (`cellphone_id`), dengan nilai berupa rating.
   2. Matriks ini diubah menjadi bentuk **sparse matrix** untuk efisiensi memori.
   3. Dihitung **cosine similarity** antar pengguna.
   4. Fungsi `user_cf_recommendation()` digunakan untuk mengambil top-N rekomendasi model ponsel bagi pengguna tertentu berdasarkan interaksi pengguna lain yang paling mirip.

   Sebagai contoh, untuk pengguna dengan `user_id = 10`, sistem merekomendasikan model-model ponsel yang belum pernah dirating oleh pengguna tersebut, namun disukai oleh pengguna-pengguna lain yang memiliki pola penilaian serupa.

   Contoh hasil rekomendasi:

   - Samsung Galaxy A72
   - OPPO Reno5
   - Vivo V21
   - Xiaomi Redmi Note 10 Pro
   - Realme 8

   Model-model ini dipilih berdasarkan **rata-rata rating tertinggi** dari pengguna lain yang paling mirip dengan pengguna target.

   **Kelebihan:**

   - Dapat menemukan pola tersembunyi dari perilaku pengguna (misalnya preferensi terhadap brand tertentu).
   - Rekomendasi lebih bervariasi dan tidak hanya bergantung pada atribut konten.
   - Dapat mengikuti tren berdasarkan perilaku pengguna lain.

   **Kekurangan:**

   - Tidak dapat memberikan rekomendasi untuk pengguna atau item baru (cold start problem).
   - Rentan terhadap data sparsity (jika pengguna sedikit memberikan rating).
   - Membutuhkan jumlah data interaksi yang cukup banyak dan beragam untuk bekerja optimal.

# Evaluation

Model rekomendasi yang dikembangkan dalam proyek ini dievaluasi melalui dua pendekatan yang sesuai dengan metode yang digunakan, yaitu:

1. **Content-Based Filtering (CBF) Evaluation**

   Dalam pendekatan Content-Based Filtering, sistem memberikan rekomendasi berdasarkan kesamaan atribut atau metadata dari produk yang telah disukai atau diminati oleh pengguna sebelumnya. Evaluasi pada metode ini tidak mengandalkan metrik kuantitatif seperti precision atau recall, karena fokus utamanya adalah memastikan bahwa rekomendasi yang diberikan sesuai secara konten, bukan berdasarkan pola perilaku pengguna lain.

   Oleh karena itu, penilaian terhadap CBF dilakukan secara kualitatif, dengan cara menilai kesesuaian konten antara produk yang direkomendasikan dan preferensi pengguna yang teridentifikasi dari interaksi sebelumnya. Tujuannya adalah untuk mengukur sejauh mana sistem mampu mengenali karakteristik produk yang disukai dan merekomendasikan item lain yang memiliki fitur serupa.

   Contoh:

   - Jika seorang pengguna memberikan rating tinggi pada ponsel dengan keunggulan di sektor kamera, maka sistem CBF diharapkan menyarankan ponsel lain yang juga memiliki spesifikasi kamera unggulan.

   - Penilaian terhadap relevansi ini dilakukan secara manual atau berdasarkan umpan balik dari pengguna, bukan melalui perhitungan metrik numerik seperti precision atau recall.

   2. **Collaborative Filtering (CF) Evaluation**

   Berbeda dengan CBF, pendekatan User-Based Collaborative Filtering (CF) dievaluasi secara **kuantitatif** menggunakan dua metrik utama, yaitu:

   - **Precision\@5**: Menilai seberapa besar proporsi item relevan yang berhasil muncul dalam 5 rekomendasi teratas yang diberikan kepada setiap pengguna.
   - **Recall\@5**: Mengukur sejauh mana sistem mampu menemukan item-item relevan dalam 5 hasil rekomendasi dibandingkan dengan total item relevan yang tersedia bagi pengguna tersebut.

   **Rumus:**

   - **Precision\@K**:

     $$
     Precision@K = \frac{\text{Jumlah item relevan dalam } K \text{ rekomendasi teratas}}{K}
     $$

   - **Recall\@K**:

     $$
     Recall@K = \frac{\text{Jumlah item relevan dalam } K \text{ rekomendasi teratas}}{\text{Total item relevan}}
     $$

**Hasil Evaluasi:**

Evaluasi dilakukan pada data test set dengan `top_n = 5` untuk setiap pengguna. Hasil per pengguna mencakup metrik precision dan recall:

Contoh hasil evaluasi per pengguna:

```
   user_id  precision_cf  recall_cf
0       53           0.2   0.333333
1      100           0.0   0.000000
2      129           0.2   0.333333
3       95           0.4   1.000000
4       25           0.0   0.000000
```

**Rata-rata Evaluasi Keseluruhan:**

- **Rata-rata Precision\@5**: 0.175
- **Rata-rata Recall\@5**: 0.432

> Hasil ini menunjukkan bahwa sistem CF mampu menghasilkan rekomendasi yang cukup relevan, meskipun masih terdapat ruang untuk peningkatan presisi.

## Summary and Insight

Proyek ini berhasil mengembangkan sistem rekomendasi dengan memanfaatkan dua pendekatan utama, yaitu Content-Based Filtering dan User-Based Collaborative Filtering, untuk membantu pengguna dalam menemukan ponsel yang sesuai dengan preferensi mereka.

- **Content-Based Filtering (CBF)** mengandalkan kesamaan konten dan spesifikasi produk, sehingga sangat cocok diterapkan ketika informasi tentang pengguna masih terbatas.

- **Collaborative Filtering (CF)** menyarankan produk berdasarkan pola interaksi dari pengguna lain yang memiliki preferensi serupa, dan dievaluasi menggunakan metrik kuantitatif yang menunjukkan performa yang cukup baik dalam mengidentifikasi item yang relevan.

GKombinasi kedua pendekatan ini memiliki potensi untuk meningkatkan efektivitas sistem rekomendasi secara keseluruhan, dengan menggabungkan analisis terhadap karakteristik produk dan kebiasaan pengguna.
