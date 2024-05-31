import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import App from "./App.jsx";
import "./index.css";
import { NoPage } from "./pages/NoPage.jsx";
import { DownloadPage } from "./pages/Downloads.jsx";
import { DevelopersPage } from "./pages/Developers.jsx";
import { AboutPage } from "./pages/About.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/downloads" element={<DownloadPage />} />
        <Route path="/dev" element={<DevelopersPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="*" element={<NoPage />} />
      </Routes>
    </Router>
  </React.StrictMode>
);
