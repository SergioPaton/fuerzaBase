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
  const [touched, setTouched] = useState({});

  const mutation = useUserMutation();

  const validateField = (name, value) => {
    let error = '';
    switch (name) {
      case 'first_name':
        if (value.length < 2) error = 'Longitud insuficiente (mínimo 2 caracteres)';
        break;
      case 'last_name':
        if (value.length < 2) error = 'Longitud insuficiente (mínimo 2 caracteres)';
        break;
      case 'email':
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) error = 'Formato de correo inválido';
        break;
      case 'password':
        if (value.length < 8) error = 'Longitud insuficiente (mínimo 8 caracteres)';
        else if (!/[A-Z]/.test(value)) error = 'Debe contener al menos una letra mayúscula';
        else if (!/[a-z]/.test(value)) error = 'Debe contener al menos una letra minúscula';
        else if (!/\d/.test(value)) error = 'Debe contener al menos un número';
        break;
      default:
        break;
    }
    setErrors(prev => ({ ...prev, [name]: error }));
    return error;
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
    validateField(name, value);
  };

  const handleBlur = (e) => {
    const { name } = e.target;
    setTouched(prev => ({ ...prev, [name]: true }));
  };

  const isFormValid = () => {
    const fields = ['first_name', 'last_name', 'email', 'password'];
    return fields.every(f => !validateField(f, formData[f]));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage(null);
    setTouched({ first_name: true, last_name: true, email: true, password: true, role: true });

    if (!isFormValid()) {
      setMessage({ type: 'error', text: 'Por favor corrige los errores antes de continuar.' });
      return;
    }

    mutation.mutate(formData, {
      onSuccess: (data) => {
        setMessage({ type: 'success', text: `Usuario ${data.first_name} creado con éxito.` });
        setFormData({ first_name: '', last_name: '', email: '', password: '', role: 'client' });
        setErrors({});
        setTouched({});
      },
      onError: (error) => {
        const errorDetail = error.response?.data?.detail || error.message;
        setMessage({ type: 'error', text: `Error: ${errorDetail}` });
      }
    });
  };

  const getBorderClass = (field) => {
    if (!touched[field]) return 'border-gray-700 focus:border-blue-500';
    return errors[field] ? 'border-red-500' : 'border-green-500';
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-6 bg-gray-800 rounded-xl shadow-lg border border-gray-700 mt-6">
      <h2 className="text-2xl font-bold mb-2 text-white text-center">Nuevo Usuario</h2>
      <p className="text-sm text-gray-400 mb-6 text-center">
        Requisitos: nombre y apellido (mín. 2 letras), email real, contraseña (8+ caracteres, mayúscula, minúscula y número).
      </p>

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
          onBlur={handleBlur}
          className={`w-full px-3 py-2 bg-gray-900 rounded text-white focus:outline-none transition-colors border-2 ${getBorderClass('first_name')}`}
        />
        {touched.first_name && errors.first_name && <p className="text-red-400 text-xs mt-1">{errors.first_name}</p>}
      </div>

      <div className="mb-4">
        <label htmlFor="last_name" className="block text-sm font-medium mb-1 text-gray-300">Apellido</label>
        <input
          type="text"
          id="last_name"
          name="last_name"
          value={formData.last_name}
          onChange={handleChange}
          onBlur={handleBlur}
          className={`w-full px-3 py-2 bg-gray-900 rounded text-white focus:outline-none transition-colors border-2 ${getBorderClass('last_name')}`}
        />
        {touched.last_name && errors.last_name && <p className="text-red-400 text-xs mt-1">{errors.last_name}</p>}
      </div>

      <div className="mb-4">
        <label htmlFor="email" className="block text-sm font-medium mb-1 text-gray-300">Correo Electrónico</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          onBlur={handleBlur}
          className={`w-full px-3 py-2 bg-gray-900 rounded text-white focus:outline-none transition-colors border-2 ${getBorderClass('email')}`}
        />
        {touched.email && errors.email && <p className="text-red-400 text-xs mt-1">{errors.email}</p>}
      </div>

      <div className="mb-4">
        <label htmlFor="password" className="block text-sm font-medium mb-1 text-gray-300">Contraseña</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          onBlur={handleBlur}
          className={`w-full px-3 py-2 bg-gray-900 rounded text-white focus:outline-none transition-colors border-2 ${getBorderClass('password')}`}
        />
        <p className="text-xs text-gray-500 mt-1">Mínimo 8 caracteres, con mayúscula, minúscula y número.</p>
        {touched.password && errors.password && <p className="text-red-400 text-xs mt-1">{errors.password}</p>}
      </div>

      <div className="mb-6">
        <label htmlFor="role" className="block text-sm font-medium mb-1 text-gray-300">Rol</label>
        <select
          id="role"
          name="role"
          value={formData.role}
          onChange={handleChange}
          className="w-full px-3 py-2 bg-gray-900 border-2 border-gray-700 rounded text-white focus:outline-none focus:border-blue-500"
        >
          <option value="trainer">Entrenador</option>
          <option value="client">Cliente</option>
          <option value="independent">Independiente</option>
        </select>
      </div>

      <button
        type="submit"
        disabled={!isFormValid() || mutation.isPending}
        className="w-full bg-blue-600 hover:bg-blue-500 disabled:bg-gray-600 disabled:cursor-not-allowed text-white font-semibold py-2 px-4 rounded transition duration-200"
      >
        {mutation.isPending ? 'Guardando...' : 'Crear Usuario'}
      </button>
    </form>
  );
};

export default UserForm;
