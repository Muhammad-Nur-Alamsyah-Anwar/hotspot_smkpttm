# Portal Hotspot SMK Penerbangan Techno Terapan Makassar

Dokumentasi ini berisi panduan lengkap instalasi, fitur, dan manajemen user untuk halaman login Hotspot MikroTik. Proyek ini menggunakan desain *static* (HTML/CSS) yang ringan dan responsif.

---

## 1. Fitur Utama

### A. Halaman Login (`login.html`)
- **Responsive Design:** Tampilan otomatis menyesuaikan layar HP siswa, Tablet, maupun Laptop guru.
- **Auto-Focus:** Kursor otomatis aktif di kolom username saat halaman dibuka.
- **Feedback Error:** Menampilkan pesan error (warna merah) dari sistem MikroTik jika password salah atau user tidak ditemukan.
- **Secure Form:** Menggunakan metode POST standar MikroTik dengan perlindungan redirect (`dst` & `popup`).
- **Informasi Default:** Menampilkan info login default untuk memudahkan penggunaan awal (Siswa/Guru).

### B. Halaman Status (`status.html`)
- **Real-time Monitoring:** Menampilkan data sesi yang sedang berjalan:
  - **IP Address:** Alamat IP perangkat pengguna.
  - **Traffic Data:** Jumlah Upload / Download yang digunakan.
  - **Uptime:** Durasi waktu user terkoneksi.
- **Auto-Refresh:** Halaman otomatis memuat ulang (refresh) setiap **60 detik** untuk memperbarui data pemakaian.
- **Clean UI:** Tampilan bersih dan fokus pada data penting (tanpa gangguan teks berlebihan).
- **Logout Aman:** Tombol logout yang memicu pembersihan session cookie.

### C. Sistem Redirect (`alogin.html`)
- **Anti-Stuck:** Script otomatis yang memindahkan user dari halaman sukses login langsung ke halaman status, mencegah user terjebak di halaman kosong.

---

## 2. Manajemen User (Skenario Sekolah)

Sistem ini dirancang untuk dua jenis pengguna di MikroTik:

### 1. Siswa
- **Username:** `siswa`
- **Password:** `smkpttmsw`
- **Limitasi:** Kecepatan dibatasi (Dikonfigurasi di User Profile MikroTik, misal: 512kbps).
- **Akses:** Bisa memantau penggunaan data dan durasi online.

### 2. Guru
- **Username:** `guru`
- **Password:** `smkpttmgr`
- **Limitasi:** **Unlimited** (Prioritas tinggi/tanpa limit kecepatan).
- **Akses:** Internet full speed untuk kebutuhan mengajar.

---

## 4. Panduan Instalasi (Deployment)

Ikuti langkah ini untuk memasang di Router MikroTik:

### Langkah 1: Persiapan
1. Siapkan file logo sekolah, beri nama `logo-smkpttm.png`.
2. Masukkan logo ke dalam folder `img/`.

### Langkah 2: Upload ke MikroTik
1. Buka aplikasi **WinBox**.
2. Klik menu **Files**.
3. Cari folder `hotspot` lama, lalu **Backup** (drag & drop ke komputer Anda).
4. **Upload:** Drag & drop semua isi folder proyek ini (`img`, `css`, `*.html`) ke dalam folder `hotspot` di WinBox. Pastikan file lama tertimpa (*overwrite*).

### Langkah 3: Setting Limitasi (PENTING)
HTML tidak mengatur kecepatan, Anda harus setting di WinBox:

1. Masuk ke **IP** > **Hotspot** > **User Profiles**.
2. Buat Profile **Siswa**:
   - Name: `profil_siswa`
   - Rate Limit (rx/tx): `512k/512k` (Contoh limit 512kbps).
3. Buat Profile **Guru**:
   - Name: `profil_guru`
   - Rate Limit: Kosongkan (agar Unlimited).
4. Masuk ke tab **Users**, pastikan user `siswa` menggunakan `profil_siswa` dan user `guru` menggunakan `profil_guru`.

---

## 5. Troubleshooting & Tips

- **Masalah Logout:** Jika user klik logout tapi langsung login lagi otomatis, matikan fitur **Cookie**.
  - Caranya: **IP** > **Hotspot** > **Server Profiles** > Tab **Login** > Hilangkan centang **Cookie**.
- **Gambar Tidak Muncul:** Pastikan nama file logo persis `logo-smkpttm.png` (huruf kecil semua) dan berada di dalam folder `img`.
- **Ganti Password:** Segera ganti password default `smkpttmsw` dan `smkpttmgr` di WinBox untuk keamanan jaringan sekolah.
