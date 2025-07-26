
# 🚀 FastAPI MySQL CRUD API

This is a simple FastAPI application to perform basic CRUD operations (Create, Read, Update, Delete) with MySQL.

---

## 🧾 Requirements

- Python 3.8+
- Mysqql running locally
- pip (Python package installer)

---

## 🛠️ Installation Steps

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd py-mysql
```

### 2. Set up a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- **On Windows**:
  ```bash
  venv\Scripts\activate
  ```

- **On Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### 4. Install Required Packages

```bash
pip install fastapi uvicorn pymysql
```

---

## 📂 Project Structure

```
py-mysql/
│
├── database.py 
├── model.py 
├── main.py                   # Main app entry point
└── README.md
```

---

## ▶️ Running the Project

Start the server with:

```bash
uvicorn index:app --reload
```

Visit the documentation at:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📬 Available Endpoints

| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| POST   | `/create`        | Create a new user |
| PUT    | `/update/{id}`   | Update user by ID |
| DELETE | `/delete/{id}`   | Delete user by ID |

> ⚠️ Make sure you use the correct HTTP method in tools like Postman to avoid `405 Method Not Allowed` errors.
