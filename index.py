# ==========================================
# STRUKTUR DATA 2: QUEUE (ANTREAN)
# Digunakan nanti untuk algoritma pencarian BFS (Breadth-First Search)
# ==========================================
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

# ==========================================
# STRUKTUR DATA 1: TREE (POHON BERTINGKAT)
# ==========================================
class TreeNode:
    def __init__(self, nama):
        self.nama = nama
        self.anak_anak = []     # Menyimpan daftar anak (bisa lebih dari 1)
        self.orang_tua = None   # Pointer ke orang tua (Sangat penting untuk cari saudara!)

    def tambah_anak(self, node_anak):
        """Fungsi untuk menambahkan anak ke node saat ini"""
        node_anak.orang_tua = self        # Set orang tua dari anak tersebut
        self.anak_anak.append(node_anak)  # Masukkan ke daftar anak

# ==========================================
# CLASS UTAMA: MANAJEMEN SILSILAH KELUARGA
# ==========================================
class SilsilahKeluarga:
    def __init__(self, nama_leluhur_utama):
        # Kakek buyut / akar dari silsilah
        self.root = TreeNode(nama_leluhur_utama)

    def print_silsilah(self, node=None, level=0):
        """Fungsi dasar untuk menampilkan silsilah ke terminal"""
        if node is None:
            node = self.root
            
        # Bikin indentasi biar kelihatan bertingkat
        spasi = " " * (level * 4)
        prefix = "└── " if level > 0 else ""
        print(f"{spasi}{prefix}{node.nama}")
        
        # Panggil fungsi ini lagi untuk setiap anak (Rekursif)
        for anak in node.anak_anak:
            self.print_silsilah(anak, level + 1)

# ==========================================
# TESTING KODE (SIMULASI SEMENTARA)
# ==========================================
if __name__ == "__main__":
    # 1. Buat silsilah dengan akar "Kakek Budi"
    keluarga = SilsilahKeluarga("Kakek Budi")
    
    # 2. Buat node anggota keluarga baru
    ayah_anto = TreeNode("Ayah Anto")
    paman_andi = TreeNode("Paman Andi")
    anak_bima = TreeNode("Anak Bima")
    anak_citra = TreeNode("Anak Citra")
    
    # 3. Susun hubungannya (Kakek -> Ayah -> Anak)
    keluarga.root.tambah_anak(ayah_anto)
    keluarga.root.tambah_anak(paman_andi)
    
    ayah_anto.tambah_anak(anak_bima)
    ayah_anto.tambah_anak(anak_citra)
    
    # 4. Tampilkan hasilnya
    print("=== SILSILAH KELUARGA SEMENTARA ===")
    keluarga.print_silsilah()