import matplotlib.pyplot as plt

# Data dari tabel
items = ['Pulpen Biru', 'Buku Tulis', 'Penghapus', 'Pensil 2B', 'Stapler']
jumlah_catatan = [150, 200, 100, 120, 50]
jumlah_aktual = [145, 205, 100, 115, 50]
selisih = [-5, 5, 0, -5, 0]

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(selisih, bins=5, edgecolor='black', color='skyblue')
plt.title('Histogram Selisih Persediaan')
plt.xlabel('Selisih')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

# Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(items, selisih, color='red')
plt.title('Scatter Plot Selisih Persediaan')
plt.xlabel('Nama Barang')
plt.ylabel('Selisih')
plt.grid(True)
plt.show()

# Pie Chart
labels = ['Pulpen Biru', 'Buku Tulis', 'Penghapus', 'Pensil 2B', 'Stapler']
sizes = [145, 205, 100, 115, 50]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgrey']
explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart Jumlah Aktual Persediaan')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

# Line Chart
plt.figure(figsize=(10, 6))
plt.plot(items, jumlah_catatan, marker='o', label='Jumlah di Catatan')
plt.plot(items, jumlah_aktual, marker='o', label='Jumlah Aktual')
plt.title('Diagram Garis Jumlah Persediaan')
plt.xlabel('Nama Barang')
plt.ylabel('Jumlah')
plt.legend()
plt.grid(True)
plt.show()

# Bar Chart
bar_width = 0.35
index = range(len(items))

plt.figure(figsize=(10, 6))
plt.bar(index, jumlah_catatan, bar_width, label='Jumlah di Catatan', color='b')
plt.bar([i + bar_width for i in index], jumlah_aktual, bar_width, label='Jumlah Aktual', color='g')
plt.xlabel('Nama Barang')
plt.ylabel('Jumlah')
plt.title('Diagram Batang Jumlah Persediaan')
plt.xticks([i + bar_width / 2 for i in index], items)
plt.legend()
plt.show()
