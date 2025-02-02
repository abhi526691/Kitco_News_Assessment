# React + TypeScript Frontend

## 📌 Project Overview
This is a frontend application built using **React 18+** and **TypeScript**, styled with **Tailwind CSS**. The project follows a modular structure for maintainability and scalability.

## 🚀 Features
- **React 18+** with functional components and hooks.
- **TypeScript** for type safety and better development experience.
- **State Management** using Context API/Zustand/Redux (if applicable).
- **Form Validation** using React Hook Form / Zod.
- **API Integration** with Axios and React Query.
- **Error Handling & Loading States** for a smooth user experience.
- **Responsive Design** ensuring usability across devices.

## 📁 Project Structure
```
├── src
│   ├── components       # Reusable UI components
│   ├── pages            # Page-level components
│   ├── types            # TypeScript types and interfaces
│   ├── utils            # Helper functions and utilities
│   ├── api              # API client code (Axios/React Query)
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

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/abhi526691/Kitco_News_Assessment
cd your-repo-name
```

### 2️⃣ Install Dependencies
```sh
yarn install  # or npm install
```

### 3️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add:
```sh
VITE_API_BASE_URL=http://localhost:8000
```

### 4️⃣ Run the Development Server
```sh
yarn dev  # or npm run dev
```
The app will be available at **http://localhost:5173** (default Vite port).

## 🧪 Testing
To run tests, use:
```sh
yarn test  # or npm run test
```

## 🔧 Build for Production
```sh
yarn build  # or npm run build
```
The production-ready files will be in the `dist/` directory.

## 📜 License
This project is licensed under the [MIT License](LICENSE).

---

Feel free to modify and extend as needed! 🚀

