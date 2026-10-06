import React, { useState } from 'react';
import useUserMutation from '../hooks/useUserMutation';

const UserForm = () => {
  const [formData, setFormData] = useState({
    first_name: '',
    last_name: '',
    email: '',
    password: '',
    role: 'client'
  });
  const [message, setMessage] = useState(null);

  const mutation = useUserMutation();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(null);
    mutation.mutate(formData, {
      onSuccess: (data) => {
        setMessage({ type: 'success', text: `Usuario ${data.first_name} creado con éxito.` });
        setFormData({ first_name: '', last_name: '', email: '', password: '', role: 'client' });
      },
      onError: (error) => {
        const errorDetail = error.response?.data?.detail || error.message;
        setMessage({ type: 'error', text: `Error: ${errorDetail}` });
      }
    });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-6 bg-gray-800 rounded-xl shadow-lg border border-gray-700 mt-6">
      <h2 className="text-2xl font-bold mb-6 text-white text-center">Crear Nuevo Usuario</h2>
      
      {message && (
        <div className={`p-3 mb-4 rounded text-sm ${message.type === 'success' ? 'bg-green-900/60 text-green-300 border border-green-700' : 'bg-red-900/60 text-red-300 border border-red-700'}`}>
          {message.text}
        </div>
      )}

      <div className="mb-4">
        <label htmlFor="first_name" className="block text-sm font-medium mb-1 text-gray-300">Nombre</label>
        <input
          type="text"
          id="first_name"
          name="first_name"
          value={formData.first_name}
          onChange={handleChange}
          required
          className="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white focus:outline-none focus:border-blue-500"
        />
      </div>

      <div className="mb-4">
        <label htmlFor="last_name" className="block text-sm font-medium mb-1 text-gray-300">Apellido</label>
        <input
          type="text"
          id="last_name"
          name="last_name"
          value={formData.last_name}
          onChange={handleChange}
          required
          className="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white focus:outline-none focus:border-blue-500"
        />
      </div>

      <div className="mb-4">
        <label htmlFor="email" className="block text-sm font-medium mb-1 text-gray-300">Correo Electrónico</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          required
          className="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white focus:outline-none focus:border-blue-500"
        />
      </div>

      <div className="mb-4">
        <label htmlFor="password" className="block text-sm font-medium mb-1 text-gray-300">Contraseña</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          required
          className="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white focus:outline-none focus:border-blue-500"
        />
      </div>

      <div className="mb-6">
        <label htmlFor="role" className="block text-sm font-medium mb-1 text-gray-300">Rol</label>
        <select
          id="role"
          name="role"
          value={formData.role}
          onChange={handleChange}
          className="w-full px-3 py-2 bg-gray-900 border border-gray-700 rounded text-white focus:outline-none focus:border-blue-500"
        >
          <option value="trainer">Entrenador</option>
          <option value="client">Cliente</option>
          <option value="independent">Independiente</option>
        </select>
      </div>

      <button
        type="submit"
        disabled={mutation.isPending}
        className="w-full bg-blue-600 hover:bg-blue-500 text-white font-semibold py-2 px-4 rounded transition duration-200 disabled:opacity-50"
      >
        {mutation.isPending ? 'Guardando...' : 'Crear Usuario'}
      </button>
    </form>
  );
};

export default UserForm;
