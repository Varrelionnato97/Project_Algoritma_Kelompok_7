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