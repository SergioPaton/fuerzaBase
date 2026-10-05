import React from 'react';
import { Routes, Route } from 'react-router-dom';
import TrainerDashboard from './pages/TrainerDashboard';
import ClientDashboard from './pages/ClientDashboard';
import IndependentUserDashboard from './pages/IndependentUserDashboard';

export default function App() {
  return (
    <Routes>
      <Route path="/trainer" element={<TrainerDashboard />} />
      <Route path="/client" element={<ClientDashboard />} />
      <Route path="/independent" element={<IndependentUserDashboard />} />
    </Routes>
  );
}
