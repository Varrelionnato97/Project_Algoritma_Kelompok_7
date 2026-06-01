import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

class Laptop:
    def __init__(self, id_laptop, merk, tipe, ram, storage, harga, kategori):
        self.id = id_laptop
        self.merk = merk
        self.tipe = tipe
        self.ram = int(ram)
        self.storage = int(storage)
        self.harga = int(harga)
        self.kategori = kategori

# 2. Membuat Algoritma untuk mencari laptop
def cari_binary_search(data_laptop, target_id):
    low = 0
    high = len(data_laptop) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data_laptop[mid].id == target_id:
            return mid
        elif data_laptop[mid].id < target_id:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 # Jika tidak ditemukan 

def saring_linear_search(data_laptop, budget, kebutuhan, syarat):
    """Mencari laptop yang masuk budget dan menghitung skor awal kecocokannya"""
    hasil = []
    for laptop in data_laptop:
        if laptop.harga <= budget:
            skor = 0
            if laptop.kategori == kebutuhan: skor += 50
            if laptop.ram >= syarat["min_ram"]: skor += 25
            if laptop.storage >= syarat["min_storage"]: skor += 25
            
            if skor > 0:
                hasil.append([skor, laptop])
    return hasil

def urutkan_selection_sort(hasil_rekomendasi):
    """Mengurutkan daftar rekomendasi dari Skor Tertinggi ke Terendah (Descending)"""
    n = len(hasil_rekomendasi)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if hasil_rekomendasi[j][0] > hasil_rekomendasi[max_idx][0]:
                max_idx = j
        # Tukar posisi
        hasil_rekomendasi[i], hasil_rekomendasi[max_idx] = hasil_rekomendasi[max_idx], hasil_rekomendasi[i]
        
    return hasil_rekomendasi

class RekomendasiLaptopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Rekomendasi Laptop")
        self.root.geometry("750x650")
        
        self.bg_color = "#F4F6F9" 
        self.root.configure(bg=self.bg_color)
        self.selected_laptop_id = None

        self.data_laptop = [] 
        self.stack_undo = [] 
        self.counter_id = 1 
        
        # Nama file penyimpanan
        self.filename = "data_laptop.csv"

        self.kebutuhan_map = {
            "Gaming": {"min_ram": 16, "min_storage": 512},
            "Office": {"min_ram": 4, "min_storage": 256},
            "Desain": {"min_ram": 8, "min_storage": 512}
        }

        self.setup_style()
        self.setup_ui()
        self.load_data()
        
    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 7:
                        id_laptop, merk, tipe, ram, storage, harga, kategori = int(row[0]), row[1], row[2], int(row[3]), int(row[4]), int(row[5]), row[6]
                        laptop_baru = Laptop(id_laptop, merk, tipe, ram, storage, harga, kategori)
                        self.data_laptop.append(laptop_baru)
                        if id_laptop >= self.counter_id:
                            self.counter_id = id_laptop + 1
            self.refresh_table()
        else:
            self.create_laptop("ASUS", "ROG", 16, 1000, 20000000, "Gaming")
            self.create_laptop("Acer", "Swift", 4, 256, 6000000, "Office")
            self.create_laptop("Lenovo", "Thinkpad", 8, 512, 12000000, "Office")
            self.create_laptop("Lenovo", "Thinkpad", 16, 512, 15000000, "Office")
            self.create_laptop("Axioo", "Hype 5", 8, 256, 5000000, "Office")
            self.create_laptop("MSI", "Katana", 16, 512, 16000000, "Gaming")
            self.create_laptop("Dell", "XPS", 32, 1000, 35000000, "Design")
            self.create_laptop("HP", "Victus", 8, 512, 12000000, "Gaming")
            self.create_laptop("ASUS", "Zenbook", 16, 1000, 20000000, "Design")
            self.create_laptop("Lenovo", "Legion", 32, 1000, 30000000, "Gaming")
    
    def save_data(self):
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for laptop in self.data_laptop:
                writer.writerow([laptop.id, laptop.merk, laptop.tipe, laptop.ram, laptop.storage, laptop.harga, laptop.kategori])
    
def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="#FFFFFF", foreground="#333333", rowheight=25, fieldbackground="#FFFFFF")
        style.configure("Treeview.Heading", font=('Helvetica', 9, 'bold'), background="#E1E8ED")
        style.map('Treeview', background=[('selected', '#007BFF')]) 
        style.configure("TNotebook", background=self.bg_color)
        style.configure("TFrame", background=self.bg_color)

def setup_ui(self):
        tab_control = ttk.Notebook(self.root)
        self.tab_crud = ttk.Frame(tab_control)
        self.tab_rekomendasi = ttk.Frame(tab_control)
        
        tab_control.add(self.tab_crud, text='Kelola Data (CRUD)')
        tab_control.add(self.tab_rekomendasi, text='Cari Rekomendasi')
        tab_control.pack(expand=1, fill="both", padx=10, pady=10)

        self.setup_crud_tab()
        self.setup_rekomendasi_tab()

def setup_crud_tab(self):
        frame_input = tk.Frame(self.tab_crud, bg=self.bg_color)
        frame_input.pack(pady=15)

        def create_label(parent, text, row, col):
            tk.Label(parent, text=text, bg=self.bg_color, font=('Helvetica', 9)).grid(row=row, column=col, sticky="w", pady=5, padx=5)

        create_label(frame_input, "Merk:", 0, 0)
        self.entry_merk = ttk.Entry(frame_input)
        self.entry_merk.grid(row=0, column=1, pady=5, padx=5)

        create_label(frame_input, "Tipe:", 1, 0)
        self.entry_tipe = ttk.Entry(frame_input)
        self.entry_tipe.grid(row=1, column=1, pady=5, padx=5)

        create_label(frame_input, "RAM (GB):", 2, 0)
        self.entry_ram = ttk.Entry(frame_input)
        self.entry_ram.grid(row=2, column=1, pady=5, padx=5)

        create_label(frame_input, "Storage (GB):", 3, 0)
        self.entry_storage = ttk.Entry(frame_input)
        self.entry_storage.grid(row=3, column=1, pady=5, padx=5)

        create_label(frame_input, "Harga (Rp):", 4, 0)
        self.entry_harga = ttk.Entry(frame_input)
        self.entry_harga.grid(row=4, column=1, pady=5, padx=5)

        create_label(frame_input, "Kategori:", 5, 0)
        self.kategori_var = tk.StringVar(value="Office")
        self.combo_kategori = ttk.Combobox(frame_input, textvariable=self.kategori_var, values=["Office", "Gaming", "Desain"], state="readonly")
        self.combo_kategori.grid(row=5, column=1, pady=5, padx=5)

        frame_btn = tk.Frame(self.tab_crud, bg=self.bg_color)
        frame_btn.pack(pady=10)
        
        tk.Button(frame_btn, text="✚ Tambah Data", bg="#28A745", fg="white", font=('Helvetica', 9, 'bold'), relief="flat", padx=10, command=self.action_create).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="📝 Ubah Data", bg="#17A2B8", fg="white", font=('Helvetica', 9, 'bold'), relief="flat", padx=10, command=self.action_update).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="✖ Hapus Data", bg="#DC3545", fg="white", font=('Helvetica', 9, 'bold'), relief="flat", padx=10, command=self.action_delete).pack(side=tk.LEFT, padx=5)
        tk.Button(frame_btn, text="⟲ Undo Hapus", bg="#FFC107", fg="black", font=('Helvetica', 9, 'bold'), relief="flat", padx=10, command=self.action_undo).pack(side=tk.LEFT, padx=5)

        columns = ("ID", "Merk", "Tipe", "RAM", "Storage", "Harga", "Kategori")
        self.tree = ttk.Treeview(self.tab_crud, columns=columns, show="headings")
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=90, anchor="center")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)
        
        self.tree.bind("<<TreeviewSelect>>", self.on_table_click)

def setup_rekomendasi_tab(self):
        frame_filter = tk.Frame(self.tab_rekomendasi, bg=self.bg_color)
        frame_filter.pack(pady=20)

        tk.Label(frame_filter, text="Budget Maks:", bg=self.bg_color, fg="#DCDEDF", font=('Helvetica', 10, 'bold')).grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_budget = ttk.Entry(frame_filter, width=25)
        self.entry_budget.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_filter, text="Kebutuhan:", bg=self.bg_color, fg="#DCDEDF", font=('Helvetica', 10, 'bold')).grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.rek_kategori_var = tk.StringVar(value="Office")
        ttk.Combobox(frame_filter, textvariable=self.rek_kategori_var, values=["Office", "Gaming", "Desain"], state="readonly", width=22).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(frame_filter, text="🔍 Cari Rekomendasi", bg="#007BFF", fg="white", relief="flat", padx=20, pady=5, command=self.action_rekomendasi).grid(row=2, columnspan=2, pady=15)

        columns = ("Skor", "Merk", "Tipe", "RAM", "Storage", "Harga")
        self.tree_rek = ttk.Treeview(self.tab_rekomendasi, columns=columns, show="headings")
        for col in columns:
            self.tree_rek.heading(col, text=col)
            self.tree_rek.column(col, width=100, anchor="center")
        self.tree_rek.pack(pady=10, fill=tk.BOTH, expand=True, padx=10)

def clear_form(self):
        self.entry_merk.delete(0, tk.END)
        self.entry_tipe.delete(0, tk.END)
        self.entry_ram.delete(0, tk.END)
        self.entry_storage.delete(0, tk.END)
        self.entry_harga.delete(0, tk.END)
        self.selected_laptop_id = None

def on_table_click(self, event):
        selected_item = self.tree.selection()
        if not selected_item: return
        
        row_data = self.tree.item(selected_item)['values']
        self.selected_laptop_id = int(row_data[0])
        
        self.entry_merk.delete(0, tk.END); self.entry_merk.insert(0, row_data[1])
        self.entry_tipe.delete(0, tk.END); self.entry_tipe.insert(0, row_data[2])
        self.entry_ram.delete(0, tk.END); self.entry_ram.insert(0, row_data[3])
        self.entry_storage.delete(0, tk.END); self.entry_storage.insert(0, row_data[4])
        
        harga_clean = str(row_data[5]).replace("Rp ", "").replace(",", "")
        self.entry_harga.delete(0, tk.END); self.entry_harga.insert(0, harga_clean)
        self.kategori_var.set(row_data[6])

def create_laptop(self, merk, tipe, ram, storage, harga, kategori):
        laptop_baru = Laptop(self.counter_id, merk, tipe, ram, storage, harga, kategori)
        self.data_laptop.append(laptop_baru)
        self.counter_id += 1
        
        self.save_data() # Simpan data setelah ditambah
        self.refresh_table()

def action_create(self):
        merk = self.entry_merk.get().strip()
        tipe = self.entry_tipe.get().strip()
        ram = self.entry_ram.get().strip()
        storage = self.entry_storage.get().strip()
        harga = self.entry_harga.get().strip()
        kategori = self.kategori_var.get().strip()

        if not (merk and tipe and ram and storage and harga and kategori):
            messagebox.showwarning("Peringatan", "Semua kolom data wajib diisi, tidak boleh ada yang kosong!")
            return 

        try:
            self.create_laptop(merk, tipe, ram, storage, harga, kategori)
            messagebox.showinfo("Sukses", "Data berhasil ditambahkan dan disimpan permanen!")
            self.clear_form()
        except ValueError:
            messagebox.showerror("Error", "Gagal menyimpan! Input RAM, Storage, dan Harga wajib berupa angka murni (tanpa huruf/titik/koma).")