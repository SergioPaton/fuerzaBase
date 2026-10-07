export const validateFirstName = (value) => {
  const trimmed = (value || '').trim();
  if (!trimmed) return 'El nombre es obligatorio';
  if (trimmed.length < 2) return 'El nombre debe tener al menos 2 caracteres';
  if (trimmed.length > 50) return 'El nombre no debe exceder 50 caracteres';
  if (!/^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ\s]+$/.test(trimmed)) return 'El nombre solo debe contener letras y espacios';
  if (!/^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ]/.test(trimmed)) return 'El nombre debe comenzar con una letra';
  return '';
};

export const validateLastName = (value) => {
  const trimmed = (value || '').trim();
  if (!trimmed) return 'El apellido es obligatorio';
  if (trimmed.length < 2) return 'El apellido debe tener al menos 2 caracteres';
  if (trimmed.length > 50) return 'El apellido no debe exceder 50 caracteres';
  if (!/^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ\s]+$/.test(trimmed)) return 'El apellido solo debe contener letras y espacios';
  if (!/^[A-Za-zÁáÉéÍíÓóÚúÜüÑñ]/.test(trimmed)) return 'El apellido debe comenzar con una letra';
  return '';
};

export const validateEmail = (value) => {
  const trimmed = (value || '').trim();
  if (!trimmed) return 'El email es obligatorio';
  if (trimmed.length > 100) return 'El email no debe exceder 100 caracteres';
  if (trimmed.includes(' ')) return 'El email no debe contener espacios';
  const regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!regex.test(trimmed)) return 'El email no es válido';
  return '';
};

export const validatePassword = (value) => {
  const trimmed = (value || '').trim();
  if (!trimmed) return 'La contraseña es obligatoria';
  if (trimmed.length < 8) return 'La contraseña debe tener al menos 8 caracteres';
  if (trimmed.length > 128) return 'La contraseña no debe exceder 128 caracteres';
  if (!/[A-Z]/.test(trimmed)) return 'Debe incluir al menos una mayúscula';
  if (!/[a-z]/.test(trimmed)) return 'Debe incluir al menos una minúscula';
  if (!/\d/.test(trimmed)) return 'Debe incluir al menos un número';
  if (!/[!@#$%^&*(),.?":{}|<>]/.test(trimmed)) return 'Debe incluir al menos un carácter especial';
  return '';
};

export const validateRole = (value) => {
  const trimmed = (value || '').trim();
  const validRoles = ['client', 'trainer', 'independent'];
  if (!trimmed) return 'El rol es obligatorio';
  if (!validRoles.includes(trimmed)) return 'Selecciona un rol válido: client, trainer o independent';
  return '';
};

export const validateForm = (formData) => {
  const errors = {};
  errors.first_name = validateFirstName(formData?.first_name);
  errors.last_name = validateLastName(formData?.last_name);
  errors.email = validateEmail(formData?.email);
  errors.password = validatePassword(formData?.password);
  errors.role = validateRole(formData?.role);
  return errors;
};

export const isFormValid = (formData) => {
  const errors = validateForm(formData);
  return Object.values(errors).every(msg => msg === '');
};

export const getFeedbackMessages = (errors) => {
  return Object.entries(errors)
    .filter(([, msg]) => msg !== '')
    .map(([field, msg]) => `${field}: ${msg}`);
};
