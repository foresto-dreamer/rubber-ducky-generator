# 🦆 Rubber Ducky Generator

![Backend](https://img.shields.io/badge/Backend-Flask-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Deploy](https://img.shields.io/badge/Deployed%20on-Render-black?style=for-the-badge)


---

## ⚡ What Is This?

Rubber Ducky Generator is a backend service that converts custom scripting commands into executable Rubber Ducky payload format.

It powers the live frontend and processes script → payload transformation using Python + Flask.

---

## 🌍 Live Demo

🖥 **Frontend:**  
https://rubber-ducky-frontend.vercel.app  

⚙ **Backend API:**  
https://rubber-ducky-generator.onrender.com  

---

## 🚀 Features

- 🔄 Script → Payload conversion  
- 🌐 JSON REST API  
- 📦 File download support  
- 🔐 CORS enabled for frontend integration  
- 🚀 Deployed with Gunicorn on Render  
- 🧠 Custom parsing engine  

---

## 🛠 Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github)

---

## 📂 Project Structure

```bash
rubber-ducky-generator/
│
├── app.py          # Flask app
├── parser.py       # Script parsing logic
├── requirements.txt
├── Procfile
└── README.md
```

---

## 🔗 API Endpoints

### POST `/generate`

Request:

```json
{
  "script": "type hello\nOPEN_CMD"
}
```

Response:

```json
{
  "output": "STRING hello\nGUI r\n..."
}
```

---

### POST `/download`

Returns a downloadable payload file.

---

## 🧪 Run Locally

```bash
git clone https://github.com/foresto-dreamer/rubber-ducky-generator.git
cd rubber-ducky-generator
pip install -r requirements.txt
python app.py
```

---

## 🧠 Why This Project?

- Full-stack integration practice  
- Backend API development  
- Production deployment experience  
- Real-world parsing logic implementation  

---

## 📈 Future Improvements

- Input validation  
- More command support  
- Logging system  
- Rate limiting  
- Authentication  
- Unit testing  

---

## 🤝 Related Project

Frontend repository:  
https://github.com/foresto-dreamer/rubber-ducky-frontend

---

## 🏁 Status

✔ Live  
✔ Connected to frontend  
✔ Production deployed  
✔ Actively improving  

---

### ⭐ If you like this project, consider giving it a star!
