# 🕵️‍♂️ Decode Message from HTML Table

A simple Python script that fetches and decodes a hidden message from an HTML table on a given webpage.  
Each table row is expected to contain three columns: the **X position**, **character**, and **Y position**.  
The script reconstructs the message based on these coordinates and prints it to the console.

---

## 📜 Features

- Automatically fetches an HTML page using `requests`  
- Parses HTML tables using `BeautifulSoup`  
- Extracts data and reconstructs a grid message  
- Handles missing tables, invalid rows, and HTTP errors gracefully  

---

## 🧠 How It Works

1. Fetches the given URL.  
2. Looks for a `<table>` element in the HTML.  
3. Reads each row containing:
   - **X** → horizontal coordinate  
   - **Character** → symbol to display  
   - **Y** → vertical coordinate  
4. Builds a 2D grid from the coordinates and prints the decoded message.

---

## 🛡️ Error Handling

- Table not found: Prints a message if the <table> element is missing.
- Invalid data rows: Skips rows that don’t have valid numeric coordinates.
- Network issues: Catches and displays any requests exceptions.
