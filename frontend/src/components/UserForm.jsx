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
  const [errors, setErrors] = useState({});

  const mutation = useUserMutation();

  const validateField = (name, value) => {
    let error = '';
    switch (name) {
      case 'first_name':
        if (value.length < 2) {
          error = 'El nombre debe tener al menos 2 caracteres';
        }
        break;
      case 'last_name':
        if (value.length < 2) {
          error = 'El apellido debe tener al menos 2 caracteres';
        }
        break;
      case 'email':
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
          error = 'El correo electrónico no es válido';
        }
        break;
      case 'password':
        if (value.length < 8) {
          error = 'La contraseña debe tener al menos 8 caracteres';
        } else if (!/[A-Z]/.test(value)) {
          error = 'La contraseña debe contener al menos una letra mayúscula';
        } else if (!/[a-z]/.test(value)) {
          error = 'La contraseña debe contener al menos una letra minúscula';
        } else if (!/\d/.test(value)) {
          error = 'La contraseña debe contener al menos un número';
        }
        break;
      default:
        break;
    }
    setErrors(prev => ({ ...prev, [name]: error }));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    validateField(name, value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(null);
    
    // Validación final antes de enviar
    const finalErrors = {};
    Object.keys(formData).forEach(key => {
      validateField(key, formData[key]);
      if (errors[key]) finalErrors[key] = errors[key];
    });

    if (Object.keys(finalErrors).length > 0) {
      setMessage({ type: 'error', text: 'Por favor corrige los errores en el formulario.' });
      return;
    }

    mutation.mutate(formData, {
      onSuccess: (data) => {
        setMessage({ type: 'success', text: `Usuario ${data.first_name} creado con éxito.` });
        setFormData({ first_name: '', last_name: '', email: '', password: '', role: 'client' });
        setErrors({});
      },
      onError: (error) => {
        const errorDetail = error.response?.data?.detail || error.message;
        setMessage({ type: 'error', text: `Error: ${errorDetail}` });
      }
    });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-6 bg-gray-800 rounded-xl shadow-lg border border-gray-700 mt-6">
      <h2 className="text-2xl font-bold mb-6 text-white text-center">Nuevo Usuario</h2>
      
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
        {errors.first_name && <p className="text-red-400 text-xs mt-1">{errors.first_name}</p>}
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
        {errors.last_name && <p className="text-red-400 text-xs mt-1">{errors.last_name}</p>}
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
        {errors.email && <p className="text-red-400 text-xs mt-1">{errors.email}</p>}
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
        {errors.password && <p className="text-red-400 text-xs mt-1">{errors.password}</p>}
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
        {mutation.isPending ? 'Guardando...' : '_crear Usuario'}
      </button>
    </form>
  );
};

export default UserForm;
