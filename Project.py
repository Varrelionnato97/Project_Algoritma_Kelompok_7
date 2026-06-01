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