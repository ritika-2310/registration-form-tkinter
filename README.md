# registration-form-tkinter
# CDS Entry Management System 🗂️
A desktop-based GUI application developed in Python using **Tkinter** that allows users to **register**, **view**, **search**, **update**, and **delete** records related to the CDS (Combined Defence Services) examination. All data is stored and managed through a connected **MySQL database**.
<br>
---
<br>
## 🔍 Overview
This project acts as a **registration and management tool** for CDS examination entries. It provides the following key functionalities through a friendly GUI:
- ✅ Add New Entry
- 📋 View All Entries
- 🔍 Search for an Entry by Entry Number
- ✏️ Update Any Field in an Entry
- 🗑️ Delete an Entry
Each form input includes **placeholder text** and **input validation**, and all feedback (success, failure, errors) is displayed using popup messages.
<br>
---
<br>
## 🧩 Features Breakdown
<br>
### 🖼️ GUI Interface
- Built using **Tkinter**, styled with custom colors, fonts, and a full-screen **background image (`CDSbg.jpg`)**.
- Buttons and frames dynamically appear/disappear to avoid screen clutter.
- Scrollbars and styled text fields enhance readability for long outputs.
<br>
### 🧾 Entry Fields
<br>
Each CDS candidate must fill in:
<br>
- Entry Number (integer)
- Name
- Age (integer)
- Gender
- Mother's Name
- Father's Name
- Nationality (Yes/No)
- Minority Status (Yes/No)
- Email Address
<br>
Validation ensures **no field is left empty or with placeholder**.
<br>
---
<br>
## ⚙️ Functional Components
<br>
### 🔹 1. Insert Entry
- `insert()` opens a form to enter new candidate data.
- `insertget()` validates inputs and inserts the entry into the database using:
<br>
```sql
INSERT INTO entries(entryno, name, age, gender, mother, father, nationality, minority, email)
<br>
```
All fields must be filled and valid. A popup confirms success or error.
---
<br>
### 🔹 2. Display All Entries
- `display()` fetches all rows from the `entries` table and shows them in a styled Text widget with a scrollbar (optional).
- Uses:
<br>
```sql
SELECT * FROM entries
```
<br>
Outputs are formatted with labels and separators for easy viewing.
<br>
---
<br>
### 🔹 3. Search for an Entry
- `search()` shows an input for entry number.
- `searchget()` performs the query using:
<br>
```sql
SELECT * FROM entries WHERE entryno = <input>
```
<br>
If a match is found, details are shown. If not, a message box notifies the user.
<br>
---
<br>
### 🔹 4. Update an Entry
- `update()` allows choosing a specific field to modify.
- Internally uses `UPDATE` queries like:
<br>
```sql
UPDATE entries SET name='New Name' WHERE entryno=101;
```
<br>
Each field has a dedicated function:
- `n()` → name
- `n1()` → age
- `n2()` → gender
- `n3()` → mother
- `n4()` → father
- `n5()` → nationality
- `n6()` → minority
- `n7()` → email
<br>
Each update is confirmed via popup.
<br>
---
<br>
### 🔹 5. Delete an Entry
- `delete()` shows an input field for entry number.
- `deleteget()` deletes the matching entry using:
<br>
```sql
DELETE FROM entries WHERE entryno = <input>
```
<br>
Confirmation is shown after successful deletion.
<br>
---
<br>
## 🛠️ Technologies Used
<br>
| Component        | Tech                  |
<br>
|------------------|------------------------|
<br>
| GUI              | Python `tkinter`, `ttk` |
<br>
| Database         | MySQL (`mysql.connector`) |
<br>
| Image Processing | `PIL` (Pillow) for background |
<br>
| Alerts & Prompts | `tkinter.messagebox` |
<br>
| Language         | Python 3.x             |
<br>
<br>
---
<br>
## 🖥️ UI Elements & Design
<br>
- **Main Buttons**: Large, color-coded buttons aligned to top-left:
  - Register for CDS examination
  - Display Entries
  - Search an Entry
  - Update an Entry
  - Delete an Entry
<br>
- **Background**: `CDSbg.jpg`, resized to window size (1530x1530)
- **Custom Styles**: Fonts, colors, padding, and scrollbars for better UX
<br>
---
<br>
## 🧱 Prerequisites
<br>
- Python 3.x installed
- MySQL server running with:
  - User: `root`
  - Password: `***`
  - Database: `CDS`
  - Table: `entries` with the following schema:
<br>
```sql
CREATE TABLE entries (
  entryno INT PRIMARY KEY,
  name VARCHAR(100),
  age INT,
  gender VARCHAR(10),
  mother VARCHAR(100),
  father VARCHAR(100),
  nationality VARCHAR(10),
  minority VARCHAR(10),
  email VARCHAR(100)
);
```
<br>
- Required Python packages:
<br>
```bash
pip install pillow mysql-connector-python
```
<br>
---
<br>
## 🚀 Running the Application
<br>
1. Place `main.py` and `CDSbg.jpg` in the same directory.
2. Ensure MySQL server is running and the `CDS` database + `entries` table exists.
3. Run the script:
<br>
```bash
python main.py
```
<br>
---
<br>
## 🧪 Example Workflows
<br>
### ➕ Adding an Entry
1. Click **"Register for CDS examination"**
2. Fill all fields
3. Click **Submit**
4. Success message appears.
<br>
### 🔍 Searching for Entry #101
1. Click **"Search an Entry"**
2. Enter `101`
3. See matching entry, or a “not found” message.
<br>
### 🔄 Updating Age of Entry #101
1. Click **"Update an Entry"**
2. Enter `101`
3. Choose **"Update Age"**, enter new age
4. Click Submit → confirmation shown.
<br>
### ❌ Deleting Entry
1. Click **"Delete an Entry"**
2. Enter entry number
3. Click Submit → deletes if exists.
<br>
---
<br>
## ⚠️ Error Handling
<br>
- Shows popup on:
  - Empty or invalid fields
  - Failed DB connection
  - Non-existent entry
  - Wrong data types
<br>
---
<br>
## 👩‍💻 Author
<br>
**Ritika Bhasin**  
Python Developer | GUI & Database Enthusiast  
_This project is part of a Tkinter + MySQL learning journey._
<br>
---
<br>
## 📝 License
<br>
IT License – Free to use, modify, and distribute.
<br>
---
