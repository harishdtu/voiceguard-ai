🎯 VoiceGuardAI – Deepfake Detection System

VoiceGuardAI is a full-stack deepfake detection web application that allows users to upload audio or video files and receive a real/fake classification with a confidence score.
The project demonstrates clean API design, secure authentication, frontend-backend integration, and real-world cloud deployment.

🚀 Live Demo

Frontend (Netlify): 👉 https://voiceguard-ai.netlify.app/

Backend API (Render): 👉 https://voiceguard-ai-1.onrender.com/

Testing: 👉 Postman
<img width="1920" height="1080" alt="Screenshot (426)" src="https://github.com/user-attachments/assets/a05d4d57-2a82-416d-bb51-15785a3a4715" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/1843d08c-7a75-4a97-a07c-16707c8eef67" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e0d45ed6-d7ed-43cb-b777-0ab9f71d6a2e" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/e862d50f-bd1a-42d9-a073-0c1a461848f5" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/fd5359fe-57f9-4967-be9c-da9d69067ac3" />
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/28d74f29-5c76-4525-81d1-2d34ee0d247a" />

🧠 Features

Secure JWT-based authentication

Upload audio/video files for analysis

Returns REAL / FAKE prediction + confidence score

Clean, responsive UI

Rate-limited and CORS-secured API

Fully deployed (frontend + backend)

🏗️ Tech Stack
🔹 Backend

FastAPI

Uvicorn

Pydantic

fastapi-jwt-auth

SlowAPI (rate limiting)

🔹 Frontend

React

Vite

Axios

CSS (custom styling)

🔹 Deployment

Render – Backend hosting

Netlify – Frontend hosting

📐 Architecture Overview
Frontend (React + Netlify)
        |
        |  HTTPS (JWT Auth)
        |
Backend (FastAPI + Render)
        |
        |  Inference Logic (Mock)
        |
    Detection Result

🔐 Authentication Flow

User logs in via /auth/login

Backend issues a JWT token

Token is required to access /detect/media

Unauthorized requests are rejected

📤 Media Detection Flow

User uploads audio/video file

Backend validates file

Mock inference logic runs

API returns:

Prediction (REAL / FAKE)

Confidence score

Frontend displays result instantly

📄 API Endpoints
🔹 Auth

POST /auth/login – User login (JWT token)

🔹 Detection

POST /detect/media – Upload media & get prediction

🔹 Health

GET / – API health check

🧪 Example API Response
{
  "filename": "sample.wav",
  "prediction": "FAKE",
  "confidence": 0.87,
  "model": "VoiceGuardAI-Mock-v1"
}

📊 Datasets Used

No external datasets were used in this submission.
As permitted by the task guidelines, mock inference logic was implemented to focus on system design, API quality, security, and deployment.
The system is designed to easily integrate real datasets such as ASVspoof or FaceForensics++ in the future.

⚙️ Local Setup (Optional)
Backend
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend
npm install
npm run dev

🚧 Key Challenges Faced

Frontend-backend CORS configuration

JWT authentication with file uploads

Debugging Render deployment issues

Python version incompatibility (resolved by pinning runtime)

Ensuring production-ready API behavior

🔮 Future Improvements

Integrate a real deepfake detection model

Add detection history & analytics

Dockerize the application

Improve UI with progress indicators

Add role-based access control

🌟 What I’m Most Proud Of

Successfully delivering a fully deployed, end-to-end system that works in production.
This project reflects real-world engineering practices, including debugging deployment issues, handling security concerns, and building a complete user flow.


📜 License

This project is created for evaluation and demonstration purposes as part of the VoiceGuardAI hiring task.
