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