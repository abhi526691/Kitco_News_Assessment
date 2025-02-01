import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { Toaster } from "react-hot-toast";
import { ArticleProvider } from "./context/ArticleContext";
import HomePage from "./pages/HomePage";
import ArticleEditPage from "./pages/ArticleEditPage";

function App() {
  return (
    <Router>
      <ArticleProvider>
        <div className="App">
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/articles/:id/edit" element={<ArticleEditPage />} />
          </Routes>
          <Toaster
            position="bottom-right"
            toastOptions={{
              duration: 4000,
              style: {
                background: "#363636",
                color: "#fff",
              },
            }}
          />
        </div>
      </ArticleProvider>
    </Router>
  );
}

export default App;
