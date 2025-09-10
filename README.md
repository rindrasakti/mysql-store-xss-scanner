---

# 🛡️ XSS Scanner CLI for MySQL Dump Files

This tool helps you detect potential Cross-Site Scripting (XSS) payloads inside large MySQL dump files. It's designed for security audits, forensic analysis, and input validation in web applications.

---

## 📦 Features

- ✅ Scans `.sql` dump files line-by-line (efficient for big sqldump)
- ✅ Supports built-in XSS patterns or custom pattern files
- ✅ Cross-platform CLI (Linux, Windows, macOS)
- ✅ Outputs flagged lines directly to the terminal

---

## 🐬 1. Dumping Your MySQL Database

Before scanning, export your MySQL database using `mysqldump`:

```bash
mysqldump -u <username> -p <database_name> > label_dump.sql
```

Example:

```bash
mysqldump -u root -p database_name > label_dump.sql
```

> You can add `--skip-comments --compact` for a cleaner output.

---

## 🐍 2. Installing the Scanner

### a. Clone or copy `scanner.py` and `requirement.txt`
git clone https://github.com/rindrasakti/mysql-store-xss-scanner.git
cd mysql-store-xss-scanner
### b. Install Python dependencies

```bash
pip install -r requirement.txt
```

> Only `tqdm` is required. Other libraries like `re` and `pathlib` are built-in.

---

## 🚀 3. Running the Scanner

### 🔹 Scan using default XSS patterns

```bash
python scanner.py --file-dump label_dump.sql
```

### 🔹 Scan using a custom pattern file

```bash
python scanner.py --file-dump label_dump.sql --pattern-file custom_patterns.txt
```

---

## 📄 Custom Pattern File Format

Your `custom_patterns.txt` should contain one regex pattern per line. Example:

```
<script>
onerror=
onload=
javascript:
<iframe
<img src= onerror=
eval(
```

> Use regex patterns that match the XSS payloads you want to detect.

---

## 📌 Usage Tips

- Ensure your dump file uses UTF-8 encoding to avoid regex issues.
- For large files, consider running the scan on a server or VM.
- You can combine this tool with cronjobs for scheduled audits.

---


## 👨‍💻 Author

Developed by Arindra (Momoci) — a DevSecOps enthusiast with a passion for scripting, digital defense, and creative tooling.  
Feel free to contribute, suggest improvements, or fork the project!



