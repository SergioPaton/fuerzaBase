export const validateFirstName = (value) => {
  if (!value) return 'El nombre es requerido';
  if (value.length < 2) return 'El nombre debe tener al menos 2 caracteres';
  return '';
};

export const validateLastName = (value) => {
  if (!value) return 'El apellido es requerido';
  if (value.length < 2) return 'El apellido debe tener al menos 2 caracteres';
  return '';
};

export const validateEmail = (value) => {
  if (!value) return 'El email es requerido';
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(value)) return 'El email no es válido';
  return '';
};

export const validatePassword = (value) => {
  if (!value) return 'La contraseña es requerida';
  if (value.length < 8) return 'La contraseña debe tener al menos 8 caracteres';
  if (!/[a-zA-Z]/.test(value)) return 'La contraseña debe contener al menos una letra';
  if (!/\d/.test(value)) return 'La contraseña debe contener al menos un número';
  return '';
};

export const validateRole = (value) => {
  const validRoles = ['client', 'trainer', 'independent'];
  if (!value) return 'El rol es requerido';
  if (!validRoles.includes(value)) return 'Rol no válido';
  return '';
};

export const validateForm = (formData) => {
  const errors = {};
  errors.first_name = validateFirstName(formData.first_name);
  errors.last_name = validateLastName(formData.last_name);
  errors.email = validateEmail(formData.email);
  errors.password = validatePassword(formData.password);
  errors.role = validateRole(formData.role);
  return errors;
};
