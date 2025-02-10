# -*- coding: utf-8 -*-
"""computeSales.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zwXvyBFw554KGZvMaqbVSZ8TDZWL4um0
"""

#Google Drive Connection
from google.colab import drive
drive.mount('/content/drive')

import json
import time
import os

PRICE_FILE = "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/TC1.ProductList.json"
SALES_FILE = "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/TC1.Sales.json"
OUTPUT_FILE = "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/SalesResults.txt"

def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found - {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
    return None

def compute_total_sales(products, sales):
    product_prices = {item["title"]: item["price"] for item in products}
    total_cost = 0
    errors = []

    for sale in sales:
        product_name = sale["Product"]
        quantity = sale["Quantity"]

        if product_name in product_prices:
            total_cost += product_prices[product_name] * quantity
        else:
            errors.append(f"Warning: Product '{product_name}' not found in catalog.")

    return total_cost, errors

def save_results(file_path, total_cost, errors, elapsed_time):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f"Total Sales Cost: ${total_cost:.2f}\n")
        file.write(f"Execution Time: {elapsed_time:.4f} seconds\n")
        if errors:
            file.write("\nErrors:\n")
            for error in errors:
                file.write(f"{error}\n")

def main():
    start_time = time.time()

    products = load_json(PRICE_FILE)
    sales = load_json(SALES_FILE)

    if products is None or sales is None:
        print("Error: Could not load JSON data. Exiting.")
        return

    total_cost, errors = compute_total_sales(products, sales)

    elapsed_time = time.time() - start_time

    print(f"Total Sales Cost: ${total_cost:.2f}")
    print(f"Execution Time: {elapsed_time:.4f} seconds")
    if errors:
        print("\nErrors:")
        for error in errors:
            print(error)

    save_results(OUTPUT_FILE, total_cost, errors, elapsed_time)
    print(f"Results saved to {OUTPUT_FILE}")

main()

pip install flake8

CHECK_FILE = "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/computeSales.ipynb"

!python "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/computeSales.ipynb" "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/TC1.ProductList.json" "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/TC1.Sales.json"

!flake8 "/content/drive/MyDrive/Colab Notebooks/Pruebas de SW y Calidad/Tarea 5.2/computeSales.ipynb"