# Tugas2-FastAPI_CRUD

## Cara Menjalankan Aplikasi

1. **Aktifkan virtual environment**
   ```powershell
   .\.venv\Scripts\activate
   ```

2. **Install dependensi**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Jalankan server FastAPI**
   ```powershell
   fastapi dev main.py
   ```

4. **Akses dokumentasi API** melalui browser:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoint CRUD

| Metode | Endpoint             | Deskripsi                                           |
|--------|----------------------|-----------------------------------------------------|
| POST   | `/users`            | Menambahkan pengguna baru                          |
| GET    | `/users`            | Mengambil seluruh data pengguna (khusus admin)    |
| GET    | `/users/{user_id}`  | Mengambil data pengguna berdasarkan ID            |
| PUT    | `/users/{user_id}`  | Memperbarui data pengguna                         |
| DELETE | `/users/{user_id}`  | Menghapus pengguna berdasarkan ID                 |

---

## Contoh JSON Body

Gunakan struktur JSON berikut untuk **POST** dan **PUT**:

```json
{
  "username": "userbaru",
  "email": "user@example.com",
  "password": "Password1!",
  "role": "admin"
}
```

---

## Cara Pengujian API

### 1. Melalui Swagger UI
1. Jalankan aplikasi dan buka: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Klik endpoint yang ingin diuji
3. Klik tombol **Try it out**
4. Isi data JSON seperti contoh di atas
5. Klik **Execute** dan periksa respons dari server

---

### 2. Melalui Postman
1. Buka Postman
2. Buat request baru dengan metode dan URL:
   - **POST**: `http://127.0.0.1:8000/users`
   - **GET**: `http://127.0.0.1:8000/users`
   - **GET**: `http://127.0.0.1:8000/users/1`
   - **PUT**: `http://127.0.0.1:8000/users/1`
   - **DELETE**: `http://127.0.0.1:8000/users/1`
3. Pada tab **Body → raw → JSON**, masukkan data sesuai contoh
4. Klik **Send** untuk melihat hasilnya
