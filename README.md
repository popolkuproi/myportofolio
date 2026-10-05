Nama : Naufal ALvaro Habibullah

NPM : 2506657144

Kelas : PBP F

Jurusan : Ilmu Komputer

## Tugas 1

1. Tidak, karena section yang saya tambahkan masih dalam skala kecil ketika saya mencoba untuk menjalankan website tersebut pada mobile tidak ada skenario yang tidak saya inginkan.
2. Karena saya sendiri belum mengatur CSS agar responsive pada tugas ini, saya belum tau tantangannya, namun ketika saya mencoba-coba properti CSS seperti grid saya merasakan kesulitan karena harus mengatur 3 jenis platform, website, mobile, dan tablet agar tetap rapi ketika layar berubah. Saya mengevaluasi elemen berdasarkan fungsionalitasnya dan prioritas masing-masing elemen agar tidak ada informasi yang penting kelewatan dengan menggunakan bantuan developer tools.
3. Batasan yang saya alami dari static web adalah ketika informasi yang ditampilkan bersifat tetap dan harus diupdate manual dari sintaks HTML nya dan sistem navigasi masih belum berfungsi. Saya ingin membuat navigasi website saya dapat berfungsi, ketika orang klik navigasi yang ada bakalan langsung terarahkan ke section yang diklik

## AI Disclosure

Saya tidak menggunakan AI pada pengerjaan tugas ini.
Proses pemecahan masalah yang saya lakukan adalah membuat section technical-skills serta saya juga menambahkan button yang dapat membuka resume  saya dengan memanfaatkan google drive sebagai platform untuk mengakses resume saya serta saya mengubah properti html ketika klik button yang ada, dengan menambahkan properti target="_blank", yang akan membuat new tab ketika kita klik button.

## Tugas 2

1. Konsep MVT diimplementasikan dengan memisahkan data, proses, dan tampilan. Request dari browser menuju `portofolio/urls.py`, kemudian diteruskan ke `main/urls.py`. Setelah itu, URL `/project/` memanggil fungsi `show_project` pada `main/views.py`. View mengambil data project dari model `Project` menggunakan `Project.objects.all()`, kemudian memasukkannya ke dalam context dan mengirimkannya ke `project.html`. Template kemudian menampilkan data tersebut menggunakan perulangan `{% for project in project_list %}` hingga akhirnya ditampilkan kepada pengguna di browser.

2. Penggunaan model lebih baik karena data portfolio disimpan di database sehingga dapat dikelola dan diperbarui tanpa mengubah kode HTML. Dengan cara ini, penambahan atau perubahan project menjadi lebih mudah dan aplikasi lebih terstruktur serta mudah dikembangkan.

3. `makemigrations` digunakan untuk membuat file migration berdasarkan perubahan pada model Django. Sementara itu, `migrate` digunakan untuk menerapkan migration tersebut ke database.

## AI Disclosure

Dalam pengerjaan proyek ini, saya menggunakan ChatGPT sebagai alat bantu belajar dan debugging. AI membantu saya memahami konsep Django seperti Model, View, Template, URL routing, dan migration, serta memberikan arahan ketika saya menemukan error atau kesulitan dalam implementasi.

Saya tidak menggunakan AI untuk mengerjakan seluruh proyek secara langsung. Saya tetap melakukan implementasi, menyesuaikan kode dengan struktur proyek, dan melakukan pengujian secara mandiri menggunakan `python manage.py test` dan `python manage.py runserver`.

Strategi prompting yang saya gunakan adalah memberikan konteks masalah, potongan kode atau error yang muncul, kemudian meminta penjelasan dan langkah perbaikan. Saya menggunakan hasil dari AI sebagai referensi untuk memahami masalah sebelum menerapkannya.

Contoh penggunaan AI adalah ketika saya mengalami masalah migration dan database pada PWS, serta ketika mengimplementasikan fitur Projects menggunakan konsep MVT. AI membantu memberikan penjelasan dan langkah-langkah, sedangkan penerapan dan pengujian akhirnya saya lakukan sendiri.

## Tugas 3

1. `ModelForm` digunakan karena dapat membuat form berdasarkan model Django secara otomatis. Dengan `ModelForm`, field pada form dapat disesuaikan langsung dengan field yang terdapat pada model sehingga kode yang diperlukan lebih sedikit dan lebih mudah dipelihara. Selain itu, `ModelForm` juga menyediakan validasi berdasarkan tipe dan aturan field pada model. Dengan demikian, data yang dimasukkan melalui form dapat divalidasi sebelum disimpan ke database. `{% csrf_token %}` digunakan untuk memberikan perlindungan terhadap serangan Cross-Site Request Forgery (CSRF). Token ini memastikan bahwa request POST berasal dari form yang dibuat oleh aplikasi kita, bukan dari sumber lain yang mencoba melakukan request secara tidak sah.

2. JSON memiliki struktur yang sederhana dan mudah dibaca oleh manusia maupun mesin. JSON juga memiliki format yang lebih ringkas dibandingkan XML sehingga data dapat dikirim dengan ukuran yang lebih kecil. Selain itu, JSON sangat umum digunakan dalam aplikasi web modern dan mudah diproses menggunakan JavaScript maupun berbagai bahasa pemrograman lainnya.

3. Alur data pada fitur Education adalah sebagai berikut:
    1. Data Education disimpan di database melalui model `Education`.
    2. View `get_education_json` mengambil data dari database menggunakan `Education.objects.all()`.
    3. Data tersebut kemudian diubah menjadi format JSON menggunakan `serializers.serialize()`.
    4. JSON dikirim sebagai `HttpResponse` dengan `content_type="application/json"`.
    5. View `show_education` memanggil endpoint JSON tersebut.
    6. Data JSON kemudian diubah kembali menjadi object Django menggunakan `serializers.deserialize()`.
    7. Hasil deserialization dikirim ke template melalui context sebagai `education_list`.
    8. Template `education.html` melakukan perulangan terhadap `education_list` dan menampilkan data Education pada halaman web.

    Serialisasi diperlukan agar object atau data dari database dapat diubah menjadi format yang dapat dikirim dan dipertukarkan, seperti JSON. Setelah diterima, data tersebut dapat dilakukan deserialisasi agar kembali dapat digunakan sebagai object dalam aplikasi Django.

## AI Disclosure

Dalam pengerjaan proyek ini, saya menggunakan ChatGPT sebagai alat bantu belajar, debugging, dan referensi selama proses pengembangan. Penggunaan AI terutama membantu saya memahami konsep yang sedang dipelajari dan mencari penyebab error ketika implementasi tidak berjalan sesuai harapan.

Saya tidak menggunakan AI untuk menghasilkan keseluruhan proyek secara langsung. Saya tetap melakukan implementasi dan menyesuaikan kode dengan struktur proyek yang sudah saya buat. Setiap perubahan yang diberikan sebagai saran oleh AI saya periksa kembali dan uji pada project secara lokal sebelum digunakan.

Beberapa bagian yang saya gunakan dengan bantuan ChatGPT antara lain:

- Memahami konsep **Django Model, ModelForm, View, Template, URL routing, migration, serialization, dan deserialization**.
- Membantu menganalisis error yang muncul selama pengembangan dan deployment ke PWS.
- Membantu memahami dan memperbaiki konfigurasi **CSRF_TRUSTED_ORIGINS** ketika form mengalami error 403 pada PWS.
- Membantu melakukan debugging pada fitur **Projects**, terutama ketika data, form, migration, dan gambar belum bekerja sesuai yang diharapkan.
- Membantu memahami struktur dan alur implementasi fitur **Create, Update, Delete, dan JSON Data Delivery**.
- Membantu memahami implementasi fitur **Education** pada Assignment 3.

Strategi prompting yang saya gunakan adalah memberikan konteks mengenai fitur yang sedang dikerjakan, kemudian menyertakan potongan kode atau pesan error yang saya temui. Setelah mendapatkan penjelasan dari AI, saya menerapkan perubahan tersebut secara bertahap dan melakukan pengujian sendiri.

Untuk memastikan hasil implementasi tidak hanya bergantung pada jawaban AI, saya melakukan validasi menggunakan `python manage.py check`, `python manage.py test main`, dan `python manage.py runserver`. Saya juga melakukan pengujian fitur melalui browser dan melakukan deployment ke PWS untuk memastikan aplikasi dapat berjalan pada lingkungan production.

Dalam prosesnya, saya menemukan bahwa beberapa saran AI masih perlu disesuaikan dengan kondisi project saya. Oleh karena itu, saya tidak langsung menyalin seluruh kode yang diberikan, tetapi memeriksa kembali struktur file, nama URL, model, template, dan hasil pengujian sebelum menerapkannya.

## Tugas 5

1. Debouncing adalah teknik untuk menunda eksekusi suatu fungsi sampai pengguna berhenti melakukan suatu aktivitas selama waktu tertentu. Pada fitur pencarian yang menggunakan AJAX, debouncing digunakan agar request ke server tidak dikirim setiap kali pengguna mengetik satu karakter. Misalnya, saya menggunakan jeda sekitar 300 ms setelah input terakhir sebelum menjalankan pencarian.

Teknik ini penting karena tanpa debouncing, ketika pengguna mengetik kata yang panjang akan terjadi banyak request AJAX secara berurutan. Hal tersebut dapat membuat server menerima request yang tidak diperlukan dan membuat aplikasi menjadi kurang efisien. Dengan debouncing, request hanya dikirim setelah pengguna berhenti mengetik sejenak sehingga jumlah request dapat dikurangi dan pencarian menjadi lebih efisien.

2. fetch() digunakan untuk melakukan request secara asynchronous dan menghasilkan sebuah Promise. await digunakan untuk menunggu sampai Promise tersebut selesai sebelum program melanjutkan ke baris berikutnya. Contohnya, setelah melakukan fetch(), saya perlu menunggu response dari server sebelum membaca data JSON menggunakan response.json().

Jika tidak menggunakan await, hasil dari fetch() masih berupa Promise, bukan response yang sudah selesai. Akibatnya, jika kode langsung mencoba menggunakan hasil tersebut sebagai response, data belum tersedia dan dapat menyebabkan error atau alur program berjalan tidak sesuai yang diharapkan. await membuat alur kode asynchronous lebih mudah dibaca karena terlihat seperti proses yang berjalan secara berurutan.

3. XSS (Cross-Site Scripting) adalah serangan ketika data yang berasal dari pengguna mengandung kode atau markup berbahaya yang kemudian dijalankan oleh browser sebagai bagian dari halaman web. Contohnya, pengguna dapat memasukkan HTML atau JavaScript ke dalam field yang kemudian ditampilkan kembali kepada pengguna lain.

Pada data yang ditampilkan melalui AJAX/JavaScript, data dari server diproses dan dimasukkan ke dalam DOM secara langsung oleh JavaScript. Jika data tersebut dimasukkan menggunakan cara yang tidak aman, seperti innerHTML tanpa melakukan escaping, markup atau script yang terdapat pada data dapat dianggap sebagai HTML oleh browser. Karena itu, pada implementasi saya, data yang berasal dari server di-escape terlebih dahulu menggunakan fungsi escapeHtml() sebelum dimasukkan ke dalam tampilan.

Sementara itu, ketika data ditampilkan langsung melalui template Django, Django secara default melakukan HTML escaping pada variabel template sehingga karakter seperti < dan > tidak langsung diperlakukan sebagai HTML. Meskipun demikian, keamanan tetap harus diperhatikan pada kedua pendekatan. Pada implementasi AJAX, saya secara eksplisit melakukan escaping terhadap data yang akan dirender menggunakan JavaScript.

## AI Disclosure

Dalam pengerjaan Tugas 5, saya menggunakan ChatGPT sebagai alat bantu belajar dan pendamping implementasi. Saya tidak menggunakan AI untuk sekadar menyalin seluruh solusi, tetapi menggunakan AI untuk membantu memahami konsep, mengecek struktur implementasi, mencari kemungkinan kesalahan, dan memberikan saran ketika mengalami masalah saat mengembangkan fitur.

Saya menggunakan AI terutama pada beberapa bagian berikut:
    - memahami penerapan AJAX dan fetch() pada fitur Education;
    - memahami penggunaan JSON untuk mengambil data Education;
    - menerapkan loading, empty state, dan error state;
    - memahami dan menerapkan debouncing pada fitur pencarian;
    - membantu memahami penggunaan CSRF pada request POST;
    - membantu mengecek role check pada endpoint backend;
    - membantu mengidentifikasi potensi XSS dan menerapkan fungsi escapeHtml();
    - membantu menerapkan strip_tags pada EducationForm;
    - membantu membuat dan memperbaiki test untuk endpoint Education;
    - membantu melakukan debugging ketika terdapat error pada konfigurasi URL dan fitur delete Education.

Dalam menggunakan ChatGPT, saya memberikan konteks berupa struktur project, kode yang sedang dikerjakan, error yang muncul, serta hasil test. Saya kemudian meminta bantuan secara bertahap untuk bagian tertentu, bukan meminta AI membuat seluruh project dari awal. Setelah mendapatkan saran, saya menerapkannya pada project dan menjalankan kembali program serta test untuk memastikan perubahan tersebut sesuai dengan project saya.

Saya juga melakukan pengecekan dan perbaikan secara manual. Salah satu contohnya adalah ketika fitur delete Education mengalami error pada main/urls.py. Setelah menjalankan test, saya melihat pesan error dari Django:
TypeError: kwargs argument must be a dict, but got function.

Saya kemudian memeriksa kembali konfigurasi URL dan menemukan bahwa dua function secara tidak sengaja ditulis dalam satu pemanggilan path(). Setelah diperbaiki, saya menjalankan kembali test dan mendapatkan hasil 25 test berhasil (OK).

Saya juga menyadari bahwa AI tidak selalu mengetahui kondisi project saya secara sempurna. Saran yang diberikan tetap perlu dibandingkan dengan kode yang sebenarnya digunakan, dicoba langsung, dan diperbaiki jika tidak sesuai. Karena itu, saya menggunakan AI terutama sebagai alat bantu untuk memahami konsep, debugging, dan review, sedangkan hasil akhirnya tetap saya jalankan dan verifikasi sendiri melalui aplikasi dan automated test.

Referensi Penggunaan AI
AI yang digunakan:
    - ChatGPT (OpenAI)
    Bentuk bantuan:
        - Penjelasan konsep AJAX, fetch(), await, debouncing, CSRF, XSS, dan strip_tags.
        - Review dan debugging kode Django, JavaScript, URL, dan test.
        - Saran implementasi dan perbaikan berdasarkan error yang ditemukan saat menjalankan project.
        - Membantu menyusun dan memperbaiki automated test.
        Strategi penggunaan:
        - Memberikan konteks kode dan error yang spesifik.
        - Mengerjakan implementasi secara bertahap.
        - Menjalankan kode dan test setelah perubahan.
        - Memeriksa kembali hasil saran AI dan melakukan penyesuaian manual apabila diperlukan.