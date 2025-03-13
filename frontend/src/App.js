import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import ForumPage from "./pages/ForumPage";
import NotFoundPage from "./pages/NotFoundPage"; // Добавим страницу 404
import { AuthProvider, useAuth } from "./context/AuthContext"; // Контекст авторизации
import "./styles.css";

/**
 * Компонент защищенного маршрута, который проверяет, авторизован ли пользователь.
 * Если нет — перенаправляет на страницу входа.
 */
function ProtectedRoute({ children }) {
    const { user } = useAuth(); // Получаем текущего пользователя из контекста

    if (!user) {
        return <Navigate to="/login" replace />;
    }

    return children;
}

function App() {
    return (
        <AuthProvider>
            <Router>
                <Routes>
                    <Route path="/" element={<HomePage />} />
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/register" element={<RegisterPage />} />
                    <Route
                        path="/forum"
                        element={
                            <ProtectedRoute>
                                <ForumPage />
                            </ProtectedRoute>
                        }
                    />
                    <Route path="*" element={<NotFoundPage />} /> {/* 404-страница */}
                </Routes>
            </Router>
        </AuthProvider>
    );
}

export default App;
