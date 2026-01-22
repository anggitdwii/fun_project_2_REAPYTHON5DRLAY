# fun_project_2_REAPYTHON5DRLAY# "🎯 Nana AI Chatbot"

Chatbot AI yang dibangun menggunakan Streamlit dengan integrasi OpenRouter API untuk mengakses berbagai model AI secara gratis.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Fitur Utama

- **💬 Tampilan Chat Modern**: Interface dengan chat bubble yang menarik
- **🧠 Multi-Model AI**: Mendukung berbagai model AI gratis:
  - Mistral 7B
  - DeepSeek Chat V3
  - Llama 3.3 70B
- **📱 Responsif**: Tampilan yang optimal di desktop dan mobile
- **💾 Riwayat Chat**: Menyimpan percakapan selama sesi berjalan
- **⚡ Cepat & Ringan**: Performa optimal dengan kode yang sederhana

## 🚀 Cara Memulai

### Prasyarat
- Python 3.8 atau lebih baru
- Akun [OpenRouter](https://openrouter.ai/) (gratis)

### Instalasi

1. **Clone atau download repository**
```bash
git clone https://github.com/username/chatbot-ai.git
cd chatbot-ai
```

2. **Buat virtual environment (opsional tapi disarankan)**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install streamlit requests
```

4. **Dapatkan API Key**
   - Kunjungi [OpenRouter](https://openrouter.ai/)
   - Buat akun atau login
   - Buka [API Keys page](https://openrouter.ai/keys)
   - Klik "Create Key" dan salin API key Anda

5. **Jalankan aplikasi**
```bash
streamlit run app.py
```

6. **Buka browser** dan akses `http://localhost:8501`

## 🎨 Cara Menggunakan

1. **Masukkan API Key**:
   - Buka sidebar dengan klik tombol panah di kanan atas
   - Tempel API key OpenRouter Anda di kolom "API Key OpenRouter"

2. **Pilih Model AI**:
   - Pilih model yang ingin digunakan dari dropdown (disarankan pilih model meta-llama/llama-3)
   - Setiap model memiliki karakteristik berbeda

3. **Mulai Chatting**:
   - Ketik pesan di kolom chat di bagian bawah
   - Tekan Enter atau klik tombol kirim
   - Tunggu respons dari AI

4. **Kelola Percakapan**:
   - Gunakan tombol "Hapus Chat" di sidebar untuk menghapus riwayat
   - Refresh halaman untuk mengulang dari awal

## 📁 Struktur Kode

```
app.py                    # File utama aplikasi
requirements.txt          # Dependencies (buat dengan: pip freeze > requirements.txt)
```

### `app.py` - Penjelasan Singkat

```python
# 1. Import Libraries
import streamlit as st    # Framework web
import requests           # HTTP requests ke API
import json               # JSON processing

# 2. Custom CSS Styling
#    - Chat bubble styling
#    - Warna dan layout

# 3. get_ai_response() Function
#    - Mengirim request ke OpenRouter API
#    - Mengembalikan respons AI

# 4. Streamlit App Layout
#    - Sidebar dengan pengaturan
#    - Area chat utama
#    - Input pengguna
```

## 🔧 Model AI yang Tersedia

| Model | Provider | Gratis? | Deskripsi |
|-------|----------|---------|-----------|
| `mistralai/mistral-7b-instruct:free` | Mistral AI | ✅ | Model 7B parameter, cepat dan efisien |
| `deepseek/deepseek-chat-v3-0324:free` | DeepSeek | ✅ | Model chat yang powerful dan kontekstual |
| `meta-llama/llama-3.3-70b-instruct:free` | Meta | ✅ | Model 70B parameter, sangat capable |

## ⚠️ Troubleshooting

### Masalah Umum & Solusi

1. **"Masukkan API Key di sidebar terlebih dahulu!"**
   - Pastikan Anda sudah memasukkan API key di sidebar
   - API key harus diawali dengan `sk-or-v1-`

2. **Error API Key tidak valid**
   - Periksa apakah API key sudah benar
   - Pastikan akun OpenRouter Anda aktif
   - Coba buat API key baru

3. **Model tidak merespons**
   - Pilih model lain dari dropdown
   - Beberapa model mungkin sibuk atau offline
   - Coba lagi beberapa saat kemudian

4. **Aplikasi tidak bisa diakses**
   - Pastikan Streamlit berjalan: `streamlit run app.py`
   - Cek firewall/port 8501
   - Gunakan `--server.port 8080` untuk port alternatif

### Rate Limiting
- Model gratis memiliki batas penggunaan harian
- Jika mencapai limit, tunggu 24 jam atau upgrade ke pro

## 📝 Membuat `requirements.txt`

Untuk membuat file requirements:
```bash
pip freeze > requirements.txt
```

Isi `requirements.txt`:
```
streamlit>=1.28.0
requests>=2.31.0
```

## 🌐 Deployment

### Deploy ke Streamlit Cloud (Gratis)

1. **Push ke GitHub**
2. **Kunjungi [share.streamlit.io](https://share.streamlit.io)**
3. **Pilih repository dan file `app.py`**
4. **Tambahkan secrets** di pengaturan:
   ```
   OPENROUTER_API_KEY = "sk-or-v1-your-api-key-here"
   ```

### Deploy dengan Secrets

Untuk deploy di Streamlit Cloud dengan API key aman:

```python
# Ganti bagian API key input dengan:
import os
api_key = st.text_input("API Key", type="password") or os.getenv("OPENROUTER_API_KEY")
```

## 🛠️ Pengembangan

### Menambahkan Model Baru

Tambahkan model ke dropdown di sidebar:
```python
model = st.selectbox(
    "Pilih Model AI:",
    [
        # Model yang ada
        "mistralai/mistral-7b-instruct:free",
        "deepseek/deepseek-chat-v3-0324:free",
        # Model baru
        "openai/gpt-3.5-turbo",  # Contoh model baru
    ],
    index=0
)
```

### Custom Styling

Ubah warna di CSS bagian:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

### Parameter AI

Sesuaikan parameter AI di fungsi `get_ai_response`:
```python
"max_tokens": 1000,      # Panjang maksimal respons
"temperature": 0.7,      # Kreativitas (0.1-1.0)
```

## 📄 Lisensi

Proyek ini menggunakan lisensi MIT. Lihat file `LICENSE` untuk detail.

## 🤝 Kontribusi

Pull request dipersilakan. Untuk perubahan besar, buka issue terlebih dahulu untuk didiskusikan.

## ⭐ Dukungan

Jika proyek ini membantu Anda, berikan ⭐ di GitHub!

---

**Dibuat dengan ❤️ menggunakan Streamlit & OpenRouter API**

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)

---

## 📞 Kontak

- **Email**: anggitdwii@gmail.com
- **Whatsapp**: 089671655695

## 📚 Referensi

- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenRouter API Docs](https://openrouter.ai/docs)
- [Streamlit Chat Elements](https://docs.streamlit.io/library/api-reference/chat)

---

**Catatan**: Pastikan untuk selalu menggunakan API key dengan bertanggung jawab dan tidak membagikannya kepada publik.