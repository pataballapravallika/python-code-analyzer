# 🧠 Python Code Analyzer

A **web-based static code analyzer** built using **Python and Flask** that analyzes Python source code to evaluate code quality, complexity, and structure, and provides improvement suggestions.

---

## 🚀 Live Demo
🔗 Deployed on Render (Cloud Platform)  
👉 https://<your-render-app-name>.onrender.com

---

## 📌 Features
- Analyze Python source code without executing it
- Count:
  - Number of functions
  - Loops
  - Variables
- Calculate cyclomatic complexity
- Generate refactoring suggestions
- Simple and user-friendly web interface
- Cloud deployed and publicly accessible

---

## 🛠️ Technologies Used
- **Language:** Python
- **Framework:** Flask
- **Static Analysis:** AST, Radon
- **Frontend:** HTML, CSS
- **Deployment:** Render (Gunicorn)

---

## 📂 Project Structure
python-code-analyzer/
│
├── app.py
├── analyzer.py
├── metrics.py
├── suggestions.py
├── requirements.txt
├── runtime.txt
│
└── templates/
├── index.html
└── result.html

---

## ⚙️ How It Works
1. User pastes Python code into the web interface
2. Code is parsed using Python’s AST module
3. Metrics and complexity are calculated
4. Suggestions are generated based on thresholds
5. Results are displayed on a separate results page

---

## ▶️ Run Locally

### 1️⃣ Clone the repository

  git clone https://github.com/pataballapravallika/python-code-analyzer.git
  cd python-code-analyzer

### 2️⃣ Install dependencies
  pip install -r requirements.txt
 
### 3️⃣ Run the application
  python app.py

### 4️⃣ Open browser
  http://127.0.0.1:5000/

## ☁️ Deployment

  This application is deployed on Render, a free cloud hosting platform.

  Build Command:
    pip install -r requirements.txt
  Start Command:
    gunicorn app:app

 ## 🎓 Use Case

  Students learning clean coding practices
  Beginners understanding code complexity
  Academic mini / final-year projects
  Code quality demonstrations

## 📄 Resume Description
  Developed and deployed a Python-based static code analyzer using Flask and AST to evaluate code quality, complexity, and provide refactoring suggestions.

## 👩‍💻 Author

Pravallika Pataballa

GitHub: https://github.com/pataballapravallika

LinkedIn: https://linkedin.com/in/pravallika-pataballa-923572286

## 📜 License

This project is for educational purposes.


---

## ✅ What to do next
1️⃣ Create a file named **`README.md`**  
2️⃣ Paste the above content  
3️⃣ Replace `<your-render-app-name>` with your actual URL  
4️⃣ Commit & push to GitHub  

```bash
git add README.md
git commit -m "Add project README"
git push

--- 
