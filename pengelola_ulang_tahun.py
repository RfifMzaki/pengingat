import datetime
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class PengelolaUlangTahun:
    def __init__(self):
        self.ulang_tahun = {}
        self.index = 0

    def tambah_ulang_tahun(self, nama, tanggal_ulang_tahun):
        self.ulang_tahun[nama] = tanggal_ulang_tahun

    def urutkan_berdasarkan_tanggal(self):
        return sorted(self.ulang_tahun.items(), key=lambda x: x[1])

    def ulang_tahun_yang_akan_datang(self):
        urutan = self.urutkan_berdasarkan_tanggal()
        if urutan:
            return urutan[self.index % len(urutan)]
        else:
            return None

# Fungsi untuk mengupdate animasi
def update(frame):
    plt.clf()
    plt.axis("off")

    upcoming_birthday = birthday_manager.ulang_tahun_yang_akan_datang()

    if upcoming_birthday:
        name, birthday = upcoming_birthday
        text = f"{name}: {birthday.strftime('%d %B %Y')}"
        plt.text(0.5, 0.5, text, fontsize=14, ha="center")
    else:
        plt.text(0.5, 0.5, "Tidak ada ulang tahun yang akan datang.", fontsize=14, ha="center")

# Fungsi callback untuk tombol kiri
def on_key_press(event):
    if event.key == 'left':
        birthday_manager.index -= 1
        anim.event_source.stop()
        anim.event_source.start()

# Fungsi callback untuk tombol kanan
def on_key_release(event):
    if event.key == 'right':
        birthday_manager.index += 1
        anim.event_source.stop()
        anim.event_source.start()

# Contoh Penggunaan:
if __name__ == "__main__":
    birthday_manager = PengelolaUlangTahun()

    # Menambahkan data ulang tahun teman-teman eighteenagers
    birthday_manager.tambah_ulang_tahun("Khaira", datetime.date(2007, 1, 1))
    birthday_manager.tambah_ulang_tahun("Fiona", datetime.date(2008, 1, 2))
    birthday_manager.tambah_ulang_tahun("Kintan", datetime.date(2009, 3, 28))
    birthday_manager.tambah_ulang_tahun("Daffa", datetime.date(2008, 5, 15))
    birthday_manager.tambah_ulang_tahun("Nabylla", datetime.date(2008, 7, 18))
    birthday_manager.tambah_ulang_tahun("Aura", datetime.date(2008, 9, 7))
    birthday_manager.tambah_ulang_tahun("Farah", datetime.date(2007, 12, 19))
    birthday_manager.tambah_ulang_tahun("Rafif", datetime.date(2007, 12, 23))

    # Membuat animasi
    fig, ax = plt.subplots()
    anim = FuncAnimation(fig, update, frames=None, repeat=False, blit=False, interval=1000)
    fig.canvas.mpl_connect('key_press_event', on_key_press)
    fig.canvas.mpl_connect('key_release_event', on_key_release)
    
    # Menyimpan visualisasi dalam folder "download"
    download_folder = "download"
    os.makedirs(download_folder, exist_ok=True)
    html_path = os.path.join(download_folder, "ulang_tahun.html")
    js_path = os.path.join(download_folder, "ulang_tahun.js")
    
    plt.savefig(html_path, format='html', bbox_inches='tight')
    
    with open(js_path, "w") as js_file:
        js_code = """
        // File JavaScript dapat ditambahkan di sini untuk menambahkan fungsionalitas tambahan
        """
        js_file.write(js_code)

    print(f"File HTML dan JavaScript dapat di-download dari:\n{html_path}\n{js_path}")