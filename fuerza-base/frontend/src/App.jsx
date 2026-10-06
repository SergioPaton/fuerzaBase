import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import TrainerDashboard from './pages/TrainerDashboard';
import ClientDashboard from './pages/ClientDashboard';
import IndependentUserDashboard from './pages/IndependentUserDashboard';
import UserForm from './components/UserForm';

export default function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-gray-100 flex flex-col">
      <header className="bg-gray-800 border-b border-gray-700 p-4">
        <div className="max-w-7xl mx-auto flex items-center justify-between">
          <h1 className="text-xl font-bold text-blue-400">Fuerza Base</h1>
          <nav className="flex space-x-4 text-sm font-medium">
            <Link to="/trainer" className="hover:text-blue-400 transition">Entrenador</Link>
            <Link to="/client" className="hover:text-blue-400 transition">Atleta / Cliente</Link>
            <Link to="/independent" className="hover:text-blue-400 transition">Independiente</Link>
            <Link to="/nuevo-usuario" className="bg-blue-600 hover:bg-blue-500 text-white px-3 py-1 rounded transition">Nuevo Usuario</Link>
          </nav>
        </div>
      </header>

      <main className="flex-1 max-w-7xl w-full mx-auto p-6">
        <Routes>
          <Route path="/" element={<TrainerDashboard />} />
          <Route path="/trainer" element={<TrainerDashboard />} />
          <Route path="/client" element={<ClientDashboard />} />
          <Route path="/independent" element={<IndependentUserDashboard />} />
          <Route path="/nuevo-usuario" element={<UserForm />} />
        </Routes>
      </main>

      <footer className="bg-gray-800 border-t border-gray-700 py-4 text-center text-xs text-gray-500">
        Fuerza Base © {new Date().getFullYear()} — Plataforma de Prescripción y Regulación de Cargas
      </footer>
    </div>
  );
}
