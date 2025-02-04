# 📰 Article Management System

A full-stack web application for managing articles, built with **React (TypeScript)** on the frontend and **FastAPI + MongoDB** on the backend.

Here's the hosted link for SWaggerAPI and Frontend as well
 - https://kitco-news-assessment-2.onrender.com/docs  (SWAGGERAPI)  <br>
 - https://kitco-news-assessment-4.onrender.com/      (FRONTEND)

---

## 📌 Project Overview
This project provides a seamless way to create, read, update, and delete articles with proper validation, pagination, and error handling. The frontend is designed for a responsive and modern user experience, while the backend ensures efficient data handling and API management.

---

## 🚀 Features

### Frontend:-
- **React 18+** with functional components and hooks.
- **TypeScript** for type safety and better development experience.
- **State Management** using Context API/Zustand/Redux (if applicable).
- **Form Validation** using React Hook Form / Zod.
- **API Integration** with Axios and React Query.
- **Error Handling & Loading States** for a smooth user experience.
- **Responsive Design** ensuring usability across devices.

### Backend:-
- **FastAPI** as the web framework.
- **MongoDB** as the NoSQL database.
- **Pydantic** for data validation.
- **JWT Authentication** for secure access (if implemented).
- **Pagination & Filtering** for efficient article management.
- **Error Handling** with appropriate HTTP responses.

---

## 📁 Project Structure

### Frontend
```
├── src
│   ├── components       # Reusable UI components
│   ├── pages            # Page-level components
│   ├── types            # TypeScript types and interfaces
│   ├── utils            # Helper functions and utilities
│   ├── api              # API client code (Axios/React Query)
│   ├── hooks            # Custom React hooks
│   ├── context          # Global state management (if applicable)
│   ├── assets           # Static assets (icons, images, etc.)
│   ├── main.tsx         # Entry point
│   ├── App.tsx          # Root component
│   ├── router.tsx       # React Router configuration (if applicable)
│
├── public               # Static files (index.html, favicon, etc.)
├── .env                 # Environment variables
├── tsconfig.json        # TypeScript configuration
├── tailwind.config.js   # Tailwind CSS configuration
├── package.json         # Dependencies and scripts
```

### Backend
```
│── backend/
│   ├── api/
│   │   ├── routes/
│   │   │   ├── articles.py
│   │   │   ├── __init__.py
│   │   ├── middleware.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logging_config.py
│   ├── db/
│   │   ├── database.py
│   │   ├── models.py
│   ├── schemas/
│   │   ├── article.py
│   ├── main.py
│── .env
│── requirements.txt
│── README.md
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/abhi526691/Kitco_News_Assessment
cd Kitco_News_Assessment
```

### 2️⃣ Backend Setup
```sh
cd backend
python -m venv venv  # Create a virtual environment
source venv/bin/activate  # Activate the virtual environment (Mac/Linux)
venv\Scripts\activate  # Activate the virtual environment (Windows)

pip install -r requirements.txt  # Install dependencies
```

#### Configure Environment Variables
Create a `.env` file in the `backend` directory and add:
```sh
MONGODB_URL=mongodb://+srv
```

#### Run the Backend Server
```sh
uvicorn app.main:app --reload
```
The API will be available at **http://localhost:8000** with Swagger UI at **http://localhost:8000/docs**.

---

### 3️⃣ Frontend Setup
```sh
cd frontend
yarn install  # or npm install
```

#### Configure Environment Variables
Create a `.env` file in the `frontend` directory and add:
```sh
VITE_API_BASE_URL=http://localhost:8000
```

#### Run the Frontend Server
```sh
yarn dev  # or npm run dev
```
The app will be available at **http://localhost:5173** (default Vite port).

---

## 🔧 Build for Production

### Frontend
```sh
yarn build  # or npm run build
```
The production-ready files will be in the `dist/` directory.

### Backend
```sh
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

## 🧪 Testing
To run tests:
```sh
pytest  # For backend tests
yarn test  # or npm run test (for frontend tests)
```

---

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and extend as needed! 🚀

