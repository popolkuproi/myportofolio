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