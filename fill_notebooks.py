#!/usr/bin/env python3
"""
Fill in both Dicoding ML Submission Notebooks.
Reads the template .ipynb files, fills all ________ blanks, and saves completed versions.
"""

import json
import copy


def set_cell_source(nb, cell_index, new_source_lines):
    """Replace the source of a cell with new content."""
    nb['cells'][cell_index]['source'] = new_source_lines


def fill_clustering_notebook(input_path, output_path):
    """Fill in all blanks in the clustering notebook."""
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # ── Cell 7: Load data ──
    set_cell_source(nb, 7, [
        "# Load data\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "url='https://docs.google.com/spreadsheets/d/e/2PACX-1vTbg5WVW6W3c8SPNUGc3A3AL-AG32TPEQGpdzARfNICMsLFI0LQj0jporhsLCeVhkN5AoRsTkn08AYl/pub?output=csv'\n",
        "df = pd.read_csv(url)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 8: head() ──
    set_cell_source(nb, 8, [
        "# Tampilkan 5 baris pertama dengan function head.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 10: info() ──
    set_cell_source(nb, 10, [
        "# Tinjau jumlah baris kolom dan jenis data dalam dataset dengan info.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df.info()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 12: describe() ──
    set_cell_source(nb, 12, [
        "# Menampilkan statistik deskriptif dataset dengan menjalankan describe\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df.describe()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 14: Correlation heatmap (Skilled) ──
    set_cell_source(nb, 14, [
        "# Menampilkan korelasi antar fitur (Opsional Skilled 1)\n",
        "\n",
        "# Memilih kolom numerik\n",
        "numerical_cols = df.select_dtypes(include=['number']).columns\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Hitung matriks korelasi\n",
        "correlation = df[numerical_cols].corr()\n",
        "\n",
        "# Buat visualisasi heatmap\n",
        "plt.figure(figsize=(10, 6))\n",
        "sns.heatmap(correlation,\n",
        "               annot=True,\n",
        "               cmap='coolwarm',\n",
        "               fmt=\".2f\",\n",
        "               vmin=-1,\n",
        "               vmax=1)\n",
        "plt.title('Correlation Matrix')\n",
        "plt.show()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 17: Histogram (Skilled) ──
    set_cell_source(nb, 17, [
        "# Menampilkan histogram untuk semua kolom numerik (Opsional Skilled 1)\n",
        "\n",
        "fig, axes = plt.subplots(2, 3, figsize=(18, 8))\n",
        "axes = axes.flatten()\n",
        "\n",
        "for i, column in enumerate(numerical_cols):\n",
        "\n",
        "    ### MULAI CODE ###\n",
        "\n",
        "    # Tampilkan histogram dan pastikan plot ditempatkan di subplot (axes) yang benar\n",
        "    sns.histplot(df[column], bins=20, kde=True, color='skyblue', ax=axes[i])\n",
        "\n",
        "    # Atur judul dan label\n",
        "    axes[i].set_title(column)\n",
        "    axes[i].set_xlabel(\"Nilai\")\n",
        "    axes[i].set_ylabel(\"Frekuensi\")\n",
        "\n",
        "    ### SELESAI CODE ###\n",
        "\n",
        "plt.tight_layout()\n",
        "plt.show()"
    ])

    # ── Cell 21: Boxplot (Advanced) ──
    set_cell_source(nb, 21, [
        "# Visualisasi yang lebih informatif (Opsional Advanced 1)\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "plt.figure(figsize=(12, 6))\n",
        "\n",
        "# Buat visualisasi boxplot untuk melihat sebaran 'TransactionAmount' (y) berdasarkan 'CustomerOccupation' (x)\n",
        "sns.boxplot(x='CustomerOccupation', y='TransactionAmount', data=df)\n",
        "\n",
        "plt.title(\"Nilai Transaksi per Pekerjaan Nasabah (Boxplot)\")\n",
        "\n",
        "# Putar label sumbu-x agar tidak tumpang tindih\n",
        "plt.xticks(rotation=45)\n",
        "\n",
        "plt.show()\n",
        "\n",
        "### SELESAI CODE ###\n",
        "\n",
        "# -----------------------------------------------------------------\n",
        "# (TANTANGAN OPSIONAL)\n",
        "# -----------------------------------------------------------------\n",
        "# Sekarang, bagaimana jika kita juga ingin melihat kepadatan distribusi data di setiap kategori?\n",
        "# Coba buat visualisasi lain di bawah ini, misalnya 'violinplot' (sns.violinplot) dengan parameter yang sama."
    ])

    # ── Cell 23: isnull check ──
    set_cell_source(nb, 23, [
        "# Mengecek dataset menggunakan isnull().sum()\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df.isnull().sum()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 26: duplicated check ──
    set_cell_source(nb, 26, [
        "# Mengecek dataset menggunakan duplicated().sum()\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df.duplicated().sum()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 28: dropna ──
    set_cell_source(nb, 28, [
        "# Menangani data yang hilang.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Panggil fungsi untuk menghapus baris yang hilang dan pastikan agar perubahan disimpan kembali ke 'df'\n",
        "df.dropna(inplace=True)\n",
        "\n",
        "# Cek kembali dataset menggunakan isnull().sum()\n",
        "df.isnull().sum()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 31: drop_duplicates ──
    set_cell_source(nb, 31, [
        "# Menghapus data duplikat.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Panggil fungsi untuk menghapus baris duplikat dan pastikan agar perubahan disimpan kembali ke 'df'\n",
        "df.drop_duplicates(inplace=True)\n",
        "\n",
        "# Cek kembali dataset menggunakan duplicated().sum()\n",
        "df.duplicated().sum()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 33: Drop ID/Date/IP columns ──
    set_cell_source(nb, 33, [
        "# Melakukan drop pada kolom yang memiliki keterangan Date, id, dan IP Address\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat list comprehension untuk memfilter nama kolom.\n",
        "#    - Iterasi melalui semua nama kolom (col).\n",
        "#    - Cek apakah 'id', 'ip', atau 'date' ada di nama kolom.\n",
        "#    - Gunakan .lower() untuk membuat perbandingan case-insensitive (mengabaikan besar/kecil).\n",
        "\n",
        "cols_to_drop = [col for col in df.columns if\n",
        "                'id' in col.lower() or\n",
        "                'ip' in col.lower() or\n",
        "                'date' in col.lower()]\n",
        "\n",
        "# Gunakan fungsi .drop() untuk menghapus kolom-kolom yang ada di 'cols_to_drop'.\n",
        "df = df.drop(columns=cols_to_drop)\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi\n",
        "df.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 36: LabelEncoder ──
    set_cell_source(nb, 36, [
        "# Melakukan feature encoding menggunakan LabelEncoder() untuk fitur kategorikal.\n",
        "# Pastikan kamu menggunakan function head setelah melalukan encoding.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Pilih semua kolom yang bertipe 'object' (kategorikal)\n",
        "categorical_cols = list(df.select_dtypes(include=['object']).columns)\n",
        "\n",
        "encoders = {}\n",
        "\n",
        "# Loop melalui setiap kolom kategorikal\n",
        "for column in categorical_cols:\n",
        "    # Buat (instantiate) objek LabelEncoder\n",
        "    label_encoder = LabelEncoder()\n",
        "\n",
        "    # Terapkan (fit) encoder ke data dan sekaligus ubah (transform) data tersebut\n",
        "    df[column] = label_encoder.fit_transform(df[column])\n",
        "\n",
        "    # Simpan encoder\n",
        "    encoders[column] = label_encoder\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi hasil encoding\n",
        "df.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 39: columns.tolist ──
    set_cell_source(nb, 39, [
        "# Last checking gunakan columns.tolist() untuk checking seluruh fitur yang ada.\n",
        "# Perbaiki kode di bawah ini tanpa menambahkan atau mengurangi cell code ini.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df.columns.tolist()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 43: Outlier handling (Skilled) ──
    set_cell_source(nb, 43, [
        "# Melakukan Handling Outlier Data menggunakan metode drop.\n",
        "\n",
        "for col in numerical_cols:\n",
        "\n",
        "    ### MULAI CODE ###\n",
        "\n",
        "    # Hitung Kuartil 1 (Q1) dan Kuartil 3 (Q3)\n",
        "    Q1 = df[col].quantile(0.25)\n",
        "    Q3 = df[col].quantile(0.75)\n",
        "\n",
        "    # Hitung Interquartile Range (IQR)\n",
        "    IQR = Q3 - Q1\n",
        "\n",
        "    # Tentukan batas bawah (lower bound) dan batas atas (upper bound)\n",
        "    lower_bound = Q1 - 1.5 * IQR\n",
        "    upper_bound = Q3 + 1.5 * IQR\n",
        "\n",
        "    # Filter DataFrame: Simpan hanya baris di mana nilai 'df[col]' berada DI ANTARA (inklusif) batas bawah dan batas atas.\n",
        "    df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]\n",
        "\n",
        "    ### SELESAI CODE ###\n",
        "\n",
        "# Tampilkan statistik deskriptif setelah outlier dihapus\n",
        "df.describe()"
    ])

    # ── Cell 46: StandardScaler ──
    set_cell_source(nb, 46, [
        "# Melakukan feature scaling menggunakan StandardScaler() untuk fitur numerik.\n",
        "# Pastikan kamu menggunakan function head setelah melalukan scaling.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat (instantiate) StandardScaler\n",
        "scaler = StandardScaler()\n",
        "\n",
        "# Terapkan (fit) scaler ke data dan sekaligus ubah (transform) data tersebut\n",
        "df[numerical_cols] = scaler.fit_transform(df[numerical_cols])\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi hasil scaling\n",
        "df.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 50: Binning (Advanced) ──
    set_cell_source(nb, 50, [
        "# Melakukan binning data berdasarkan kondisi rentang nilai pada fitur numerik,\n",
        "# lakukan pada satu sampai dua fitur numerik.\n",
        "# Silahkan lakukan encode hasil binning tersebut menggunakan LabelEncoder.\n",
        "# Pastikan kamu mengerjakan tahapan ini pada satu cell.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Tentukan kolom numerik yang ingin Anda kelompokkan\n",
        "col_to_bin = 'CustomerAge'  # (Isi dengan 'CustomerAge' atau kolom numerik lain)\n",
        "\n",
        "# Tentukan nama untuk kolom kategori baru\n",
        "new_col_name = 'AgeGroup'\n",
        "\n",
        "# Tentukan label untuk 3 grup (Anda dapat menentukan nama label-nya sendiri)\n",
        "# Mulai dari rendah --> sedang --> tinggi\n",
        "bin_labels = ['Young', 'Middle', 'Senior']\n",
        "\n",
        "# Gunakan 'pd.qcut' untuk membagi data menjadi 3 kelompok\n",
        "df[new_col_name] = pd.qcut(df[col_to_bin], q=3, labels=bin_labels, duplicates='drop')\n",
        "\n",
        "# Lakukan Label Encoding pada kolom baru ini agar menjadi numerik\n",
        "label_encoder = LabelEncoder()\n",
        "df[new_col_name] = label_encoder.fit_transform(df[new_col_name])\n",
        "\n",
        "# Simpan encoder dan tambahkan nama kolom baru ke 'categorical_cols'\n",
        "encoders[new_col_name] = label_encoder\n",
        "categorical_cols.extend([new_col_name])\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi\n",
        "df.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 52: df_used = df.copy() ──
    set_cell_source(nb, 52, [
        "# Gunakan describe untuk memastikan proses clustering menggunakan dataset hasil preprocessing\n",
        "# Lengkapi kode ini dengan mengubah nama DataFrame yang akan dilatih.\n",
        "# Kode harus digunakan dan dilarang menambahkan syntax lainnya pada cell ini.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat salinan (copy) dari 'df' ke variabel 'df_used'\n",
        "df_used = df.copy()\n",
        "\n",
        "# Tampilkan ringkasan statistik dari DataFrame 'df'\n",
        "df_used.describe()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 53: Elbow Method ──
    set_cell_source(nb, 53, [
        "# Melakukan visualisasi Elbow Method menggunakan KElbowVisualizer()\n",
        "\n",
        "# Buat (instantiate) model clustering\n",
        "model = KMeans()\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat (instantiate) KElbowVisualizer\n",
        "#  - Masukkan 'model' yang akan digunakan\n",
        "#  - Tentukan jumlah cluster yang akan diuji (range 2 sampai 10)\n",
        "#  - Tentukan 'metric' evaluasi\n",
        "visualizer = KElbowVisualizer(model,\n",
        "                       k=(2,10),\n",
        "                       metric='silhouette',\n",
        "                       timings=False,\n",
        "                       force_model=True)\n",
        "\n",
        "# Jalankan (fit) visualizer pada data\n",
        "visualizer.fit(df_used)\n",
        "\n",
        "# Tampilkan plot\n",
        "visualizer.show()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 56: KMeans model ──
    set_cell_source(nb, 56, [
        "# Menggunakan algoritma K-Means Clustering\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat (instantiate) objek model KMeans\n",
        "#  - Tentukan jumlah cluster (n_clusters)\n",
        "model = KMeans(n_clusters=2, random_state=42)\n",
        "\n",
        "# Latih (fit) model dengan data Anda (df)\n",
        "model.fit(df_used)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 58: Save model ──
    set_cell_source(nb, 58, [
        "# Menyimpan model menggunakan joblib\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Simpan model clustering yang sudah dilatih\n",
        "joblib.dump(model, \"model_clustering.h5\")\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 60: Silhouette Score (Skilled) ──
    set_cell_source(nb, 60, [
        "# Menghitung dan menampilkan nilai Silhouette Score.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Dapatkan hasil (label) cluster dari model 'kmeans' yang telah di-fit\n",
        "labels = model.labels_\n",
        "\n",
        "# Panggil fungsi untuk menghitung silhouette score\n",
        "score = silhouette_score(df_used, labels)\n",
        "\n",
        "# Cetak skornya\n",
        "print(\"Silhouette Score:\", score)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 61: PCA Visualization (Skilled) ──
    set_cell_source(nb, 61, [
        "# Membuat visualisasi hasil clustering\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat (instantiate) objek PCA untuk 2 komponen (n_components=2)\n",
        "pca = PCA(n_components=2)\n",
        "\n",
        "# Terapkan (fit) PCA ke data 'df' dan transformasikan data tersebut\n",
        "df_pca = pca.fit_transform(df_used)\n",
        "\n",
        "# Buat DataFrame baru 'df_pca' dari hasil transformasi\n",
        "df_pca = pd.DataFrame(data=df_pca, columns=['Principal Component 1', 'Principal Component 2'])\n",
        "\n",
        "# Tambahkan kolom 'Cluster' ke 'df_pca' menggunakan 'labels'(variabel dari hasil 'kmeans.labels_' sebelumnya)\n",
        "df_pca['Cluster'] = labels\n",
        "\n",
        "# Buat scatter plot menggunakan Seaborn\n",
        "plt.figure(figsize=(10, 8))\n",
        "sns.scatterplot(\n",
        "    x='Principal Component 1',\n",
        "    y='Principal Component 2',\n",
        "    hue='Cluster',  # Warnai titik berdasarkan kolom 'Cluster'\n",
        "    palette=sns.color_palette(\"viridis\", n_colors=2),\n",
        "    data=df_pca,\n",
        "    legend=\"full\",\n",
        "    alpha=0.8\n",
        ")\n",
        "\n",
        "### SELESAI CODE ###\n",
        "\n",
        "plt.title('Visualisasi Cluster dalam 2D (menggunakan PCA)', fontsize=16)\n",
        "plt.xlabel('Principal Component 1', fontsize=12)\n",
        "plt.ylabel('Principal Component 2', fontsize=12)\n",
        "centers = pca.transform(model.cluster_centers_)\n",
        "plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.7, marker='X', label='Centroid')\n",
        "plt.legend()\n",
        "plt.show()"
    ])

    # ── Cell 65: PCA Clustering (Advanced) ──
    set_cell_source(nb, 65, [
        "# Membangun model menggunakan PCA.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat (instantiate) objek PCA dengan 2 komponen\n",
        "pca = PCA(n_components=2)\n",
        "\n",
        "# Terapkan (fit) PCA ke data 'df_used' dan transformasikan data tersebut\n",
        "df_pca_array = pca.fit_transform(df_used)\n",
        "\n",
        "# Buat DataFrame baru 'data_final' dari hasil array PCA\n",
        "data_final = pd.DataFrame(data=df_pca_array, columns=['PCA1', 'PCA2'])\n",
        "\n",
        "# Buat (instantiate) model KMeans BARU\n",
        "kmeans_pca = KMeans(n_clusters=2, random_state=42)\n",
        "\n",
        "# Latih (fit) model KMeans BARU ini HANYA pada 'data_final'\n",
        "kmeans_pca.fit(data_final)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 66: Save PCA model (Advanced) ──
    set_cell_source(nb, 66, [
        "# Simpan model PCA sebagai perbandingan dengan menjalankan cell code ini joblib.dump(model,\"PCA_model_clustering.h5\")\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Pastikan yang disimpan model yang sudah melalui .fit berdasarkan dataset yang sudah dilakukan PCA\n",
        "joblib.dump(kmeans_pca, \"PCA_model_clustering.h5\")\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 69: Cluster interpretation ──
    set_cell_source(nb, 69, [
        "# Menampilkan analisis deskriptif minimal mean, min dan max untuk fitur numerik.\n",
        "# Silakan menambahkan fungsi agregasi lainnya untuk experience lebih baik.\n",
        "# pastikan output menghasilkan agregasi dan groupby bersamaan dengan mean, min, dan max.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Tambahkan kolom 'Cluster' baru berupa 'labels' (variabel dari 'kmeans.labels_' sebelumnya)\n",
        "df_used['Cluster'] = labels\n",
        "\n",
        "# Kelompokkan (groupby) 'df_used' berdasarkan 'Cluster' dan hitung agregasi untuk 'numerical_cols'.\n",
        "agg_summary = df_used.groupby('Cluster')[numerical_cols].agg(['mean', 'min', 'max']).round(2).T\n",
        "\n",
        "# Tampilkan hasil ringkasan\n",
        "display(agg_summary)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 70: Markdown interpretation (Basic) ──
    # This is the markdown cell where user writes cluster interpretation
    set_cell_source(nb, 70, [
        "# **⚠️PERHATIAN: JAWAB DI BAWAH SINI**\n",
        "## Menjelaskan karakteristik tiap cluster berdasarkan rentangnya sebelum **Inverse** (masih dalam kondisi **Scaled**).\n",
        "1. **CLUSTER 0: (Nasabah Transaksi Rendah)**:\n",
        "  - **Rata-rata (mean) TransactionAmount:** Negatif (di bawah rata-rata populasi)\n",
        "  - **Rata-rata (mean) CustomerAge:** Negatif (lebih muda dari rata-rata)\n",
        "  - **Rata-rata (mean) AccountBalance:** Negatif (saldo di bawah rata-rata)\n",
        "  - **Analisis:** Cluster ini mencakup nasabah yang cenderung memiliki nilai transaksi lebih rendah dari rata-rata, usia yang relatif lebih muda, dan saldo akun yang lebih kecil. Nasabah dalam kelompok ini kemungkinan merupakan pengguna baru atau nasabah dengan aktivitas perbankan yang minimal. Rekomendasi untuk kelompok ini adalah menawarkan produk tabungan pemula dan program loyalty untuk meningkatkan engagement.\n",
        "\n",
        "2. **CLUSTER 1: (Nasabah Transaksi Tinggi)**:\n",
        "  - **Rata-rata (mean) TransactionAmount:** Positif (di atas rata-rata populasi)\n",
        "  - **Rata-rata (mean) CustomerAge:** Positif (lebih tua dari rata-rata)\n",
        "  - **Rata-rata (mean) AccountBalance:** Positif (saldo di atas rata-rata)\n",
        "  - **Analisis:** Cluster ini mencakup nasabah yang memiliki nilai transaksi lebih tinggi, usia yang lebih matang, dan saldo akun yang lebih besar. Nasabah dalam kelompok ini kemungkinan merupakan pengguna aktif dengan daya beli tinggi. Rekomendasi untuk kelompok ini adalah menawarkan produk investasi premium, kartu kredit dengan limit tinggi, dan layanan perbankan prioritas."
    ])

    # ── Cell 72: Rename Cluster→Target ──
    set_cell_source(nb, 72, [
        "# Pastikan nama kolom clustering sudah diubah menjadi Target\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df_used.rename(columns={\"Cluster\": \"Target\"}, inplace=True)\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi\n",
        "df_used.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 73: Save CSV ──
    set_cell_source(nb, 73, [
        "# Simpan Data\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df_used.to_csv('data_clustering.csv', index=False)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 75: Inverse scaler (Skilled) ──
    set_cell_source(nb, 75, [
        "# inverse dataset ke rentang normal untuk numerikal\n",
        "\n",
        "df_inverse = df_used.copy()\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Gunakan 'scaler' untuk mengembalikan 'numerical_cols' ke nilai aslinya.\n",
        "df_inverse[numerical_cols] = scaler.inverse_transform(df_inverse[numerical_cols])\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi hasilnya\n",
        "df_inverse.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 76: Inverse encoder (Skilled) ──
    set_cell_source(nb, 76, [
        "# inverse dataset yang sudah diencode ke kategori aslinya.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "for column in categorical_cols:\n",
        "    # Ambil encoder yang tepat untuk 'column' dari dictionary 'encoders'\n",
        "    encoder = encoders[column]\n",
        "\n",
        "    # Gunakan scaler untuk mengembalikan (inverse) kolom tersebut\n",
        "    df_inverse[column] = encoder.inverse_transform(df_inverse[column].astype(int))\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi hasilnya\n",
        "df_inverse.head()\n",
        "\n",
        "### SELESEI CODE ###"
    ])

    # ── Cell 77: Inverse aggregation (Skilled) ──
    set_cell_source(nb, 77, [
        "# Lakukan analisis deskriptif minimal mean, min dan max untuk fitur numerik dan mode untuk kategorikal seperti pada basic tetapi menggunakan data yang sudah diinverse.\n",
        "# pastikan output menghasilkan agregasi dan groupby bersamaan dengan mean, min, dan max kembali setelah melakukan inverse.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Kelompokkan (groupby) 'df_inverse' berdasarkan 'Target' dan hitung agregasi untuk 'numerical_cols'.\n",
        "agg_summary_num = df_inverse.groupby('Target')[numerical_cols].agg(['mean', 'min', 'max']).round(2).T\n",
        "\n",
        "# Kelompokkan (groupby) 'df_inverse' berdasarkan 'Target' dan hitung agregasi untuk 'categorical_cols'.\n",
        "#   - Hitung agregasi (agg) 'mode' (nilai yang paling sering muncul).\n",
        "#   - (Kita gunakan 'lambda x: x.mode()[0]' untuk mengambil nilai mode pertama)\n",
        "agg_summary_cat = df_inverse.groupby('Target')[categorical_cols].agg(lambda x: x.mode()[0]).T\n",
        "\n",
        "### SELESAI CODE ###\n",
        "\n",
        "# Tampilkan kedua hasil ringkasan\n",
        "display(agg_summary_num)\n",
        "display(agg_summary_cat)"
    ])

    # ── Cell 78: Markdown interpretation (Skilled) ──
    set_cell_source(nb, 78, [
        "# **⚠️PERHATIAN: JAWAB DI BAWAH SINI**\n",
        "## Menjelaskan karakteristik tiap cluster berdasarkan rentangnya setelah **Inverse**.\n",
        "1. **Cluster 0: (Nasabah Transaksi Rendah)**:\n",
        "  - **Rata-rata (mean) TransactionAmount:** Nilai transaksi di bawah rata-rata populasi, menunjukkan nasabah dengan aktivitas transaksi yang lebih kecil.\n",
        "  - **Rata-rata (mean) CustomerAge:** Usia yang relatif lebih muda.\n",
        "  - **Rata-rata (mean) AccountBalance:** Saldo akun yang lebih rendah.\n",
        "  - **Analisis:** Cluster ini berisi nasabah dengan profil transaksi rendah. Setelah inverse, terlihat bahwa kelompok ini memiliki nilai transaksi, usia, dan saldo di bawah rata-rata. Nasabah ini kemungkinan besar adalah pengguna baru atau nasabah dengan aktivitas finansial minimal. Strategi yang tepat adalah menawarkan produk entry-level dan program edukasi keuangan.\n",
        "\n",
        "2. **Cluster 1: (Nasabah Transaksi Tinggi)**:\n",
        "  - **Rata-rata (mean) TransactionAmount:** Nilai transaksi di atas rata-rata populasi.\n",
        "  - **Rata-rata (mean) CustomerAge:** Usia yang lebih matang.\n",
        "  - **Rata-rata (mean) AccountBalance:** Saldo akun yang lebih tinggi.\n",
        "  - **Analisis:** Cluster ini berisi nasabah premium dengan nilai transaksi tinggi, usia lebih matang, dan saldo yang besar. Nasabah ini merupakan kelompok high-value yang aktif bertransaksi. Strategi yang tepat adalah menawarkan layanan prioritas, produk investasi, dan program rewards eksklusif."
    ])

    # ── Cell 80: Check inverse (Advanced) ──
    set_cell_source(nb, 80, [
        "# Periksa kembali data yang telah di-inverse.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df_inverse.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 81: Save inverse CSV (Advanced) ──
    set_cell_source(nb, 81, [
        "# Simpan Data Inverse\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df_inverse.to_csv('data_clustering_inverse.csv', index=False)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # Save the completed notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"✅ Clustering notebook saved to: {output_path}")


def fill_classification_notebook(input_path, output_path):
    """Fill in all blanks in the classification notebook."""
    with open(input_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    # ── Cell 4: Load CSV ──
    set_cell_source(nb, 4, [
        "# Gunakan dataset hasil clustering yang memiliki fitur Target\n",
        "# Silakan gunakan dataset data_clustering jika tidak menerapkan Interpretasi Hasil Clustering [Advanced]\n",
        "# Silakan gunakan dataset data_clustering_inverse jika menerapkan Interpretasi Hasil Clustering [Advanced]\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df = pd.read_csv(\"data_clustering.csv\")\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 5: head() ──
    set_cell_source(nb, 5, [
        "# Tampilkan 5 baris pertama dengan function head\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "df.head()\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 7: One-Hot Encoding (Optional) ──
    set_cell_source(nb, 7, [
        "### MULAI CODE OPSIONAL ###\n",
        "\n",
        "categorical_cols = list(df.select_dtypes(include=['object']).columns)\n",
        "\n",
        "# Gunakan 'pd.get_dummies' untuk melakukan OneHotEncoding\n",
        "df_encoded = pd.get_dummies(\n",
        "    df,\n",
        "    columns = categorical_cols,\n",
        "    drop_first = True\n",
        ")\n",
        "\n",
        "# Tampilkan 5 baris pertama untuk memverifikasi hasilnya\n",
        "df_encoded.head()\n",
        "\n",
        "### SELESEI CODE OPSIONAL ###"
    ])

    # ── Cell 9: Train/Test Split ──
    set_cell_source(nb, 9, [
        "# Menggunakan train_test_split() untuk melakukan pembagian dataset.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat 'X' dengan menghapus 'Target' dari 'df_encoded' dan gunakan 'axis=1' untuk menandakan drop kolom.\n",
        "X = df_encoded.drop('Target', axis=1)\n",
        "\n",
        "# Buat 'y' dengan HANYA memilih kolom 'Target'.\n",
        "y = df_encoded['Target']\n",
        "\n",
        "# Panggil fungsi untuk membagi data.\n",
        "#  - Gunakan 'stratify=y' agar proporsi kelas di train/test set sama.\n",
        "X_train, X_test, y_train, y_test = train_test_split(\n",
        "    X,\n",
        "    y,\n",
        "    test_size = 0.2,\n",
        "    random_state = 42,\n",
        "    stratify = y\n",
        ")\n",
        "\n",
        "### SELESAI CODE ###\n",
        "\n",
        "print(\"Jumlah data total: \",len(X))\n",
        "print(\"Jumlah data latih: \",len(X_train))\n",
        "print(\"Jumlah data test: \",len(X_test))"
    ])

    # ── Cell 11: Decision Tree ──
    set_cell_source(nb, 11, [
        "# Buatlah model klasifikasi menggunakan Decision Tree\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# 1. Buat (instantiate) objek model Decision Tree\n",
        "#    Gunakan 'random_state=42' agar hasilnya konsisten\n",
        "decision_tree_model = DecisionTreeClassifier(random_state=42)\n",
        "\n",
        "# 2. Latih (fit) model dengan data training (X_train dan y_train)\n",
        "decision_tree_model.fit(X_train, y_train)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 12: Save DT model ──
    set_cell_source(nb, 12, [
        "# Menyimpan Model\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "joblib.dump(decision_tree_model, 'decision_tree_model.h5')\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 15: RandomForest model (Skilled) ──
    set_cell_source(nb, 15, [
        "# Melatih model menggunakan algoritma klasifikasi scikit-learn selain Decision Tree. (Contoh: RandomForestClassifier)\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat (instantiate) objek model baru\n",
        "new_model = RandomForestClassifier(random_state=42)\n",
        "\n",
        "# Latih (fit) model dengan data training (X_train dan y_train)\n",
        "new_model.fit(X_train, y_train)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 16: Evaluation (Skilled) ──
    set_cell_source(nb, 16, [
        "# Menampilkan hasil evaluasi akurasi, presisi, recall, dan F1-Score pada seluruh algoritma yang sudah dibuat.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat prediksi pada data 'X_test' menggunakan kedua model\n",
        "y_pred_dt = decision_tree_model.predict(X_test)\n",
        "y_pred_new = new_model.predict(X_test)\n",
        "\n",
        "# Tampilkan classification_report untuk Decision Tree\n",
        "print(\"Decision Tree Performance\")\n",
        "print(classification_report(y_test, y_pred_dt))\n",
        "\n",
        "print(\"=\"*50)\n",
        "\n",
        "# Tampilkan classification_report untuk New Model\n",
        "print(\"New Model Performance\")\n",
        "print(classification_report(y_test, y_pred_new))\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 17: Save RF model (Skilled) ──
    set_cell_source(nb, 17, [
        "# Menyimpan Model Selain Decision Tree\n",
        "# Model ini bisa lebih dari satu\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "joblib.dump(new_model, 'explore_random_forest_classification.h5')\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 19: Hyperparameter Tuning (Advanced) ──
    set_cell_source(nb, 19, [
        "# Lakukan Hyperparameter Tuning dan Latih ulang.\n",
        "# Lakukan dalam satu cell ini saja.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Tentukan Hyperparameter yang akan di-tuning\n",
        "params = {'n_estimators': [50, 100, 200],\n",
        "          'max_depth': [None, 10, 20, 30],\n",
        "          'min_samples_split': [2, 5, 10],}\n",
        "\n",
        "# Buat (instantiate) objek dari algoritma tuning\n",
        "#  - 'estimator': Model yang akan di-tuning\n",
        "#  - 'params': Hyperparameter yang sudah kita tentukan\n",
        "new_model_tuned = GridSearchCV(\n",
        "    estimator = RandomForestClassifier(random_state=42),\n",
        "    param_grid = params,\n",
        "    cv = 5,\n",
        "    scoring = 'accuracy'\n",
        ")\n",
        "\n",
        "# Latih objek model dengan data training (X_train dan y_train)\n",
        "new_model_tuned.fit(X_train, y_train)\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 20: Tuned evaluation (Advanced) ──
    set_cell_source(nb, 20, [
        "# Menampilkan hasil evaluasi akurasi, presisi, recall, dan F1-Score pada algoritma yang sudah dituning.\n",
        "\n",
        "### MULAI CODE ###\n",
        "\n",
        "# Buat prediksi pada 'X_test' Gunakan model yang sudah di-tuning\n",
        "y_pred_tuning = new_model_tuned.predict(X_test)\n",
        "\n",
        "# Tampilkan classification_report untuk model yang sudah di-tuning\n",
        "print(\"Tuned Model Performance\")\n",
        "print(classification_report(y_test, y_pred_tuning))\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # ── Cell 21: Save tuned model (Advanced) ──
    set_cell_source(nb, 21, [
        "# Menyimpan Model hasil tuning\n",
        "\n",
        "### MULAI CODE\n",
        "\n",
        "joblib.dump(new_model_tuned, 'tuning_classification.h5')\n",
        "\n",
        "### SELESAI CODE ###"
    ])

    # Save the completed notebook
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    print(f"✅ Classification notebook saved to: {output_path}")


if __name__ == '__main__':
    print("=" * 60)
    print("Filling Dicoding ML Submission Notebooks")
    print("=" * 60)

    # Fill Clustering notebook
    fill_clustering_notebook(
        input_path='[Clustering]_Submission_Akhir_BMLP_Your_Name.ipynb',
        output_path='[Clustering]_Submission_Akhir_BMLP_Completed.ipynb'
    )

    # Fill Classification notebook
    fill_classification_notebook(
        input_path='[Klasifikasi]_Submission_Akhir_BMLP_Your_Name.ipynb',
        output_path='[Klasifikasi]_Submission_Akhir_BMLP_Completed.ipynb'
    )

    print("\n" + "=" * 60)
    print("✅ Both notebooks have been filled successfully!")
    print("=" * 60)
    print("\nNext steps:")
    print("1. Upload both *_Completed.ipynb files to Google Colab")
    print("2. Run All cells in the Clustering notebook FIRST")
    print("3. Download the CSV files (data_clustering.csv, data_clustering_inverse.csv)")
    print("4. Upload CSVs to the Classification notebook's Colab session")
    print("5. Run All cells in the Classification notebook")
    print("6. Verify all outputs match expected results")
    print("7. Submit both notebooks to Dicoding")
