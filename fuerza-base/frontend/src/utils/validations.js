export const validateFirstName = (value) => {
  if (!value || value.trim().length < 2) {
    return 'El nombre debe tener al menos 2 caracteres.';
  }
  return null;
};

export const validateLastName = (value) => {
  if (!value || value.trim().length < 2) {
    return 'El apellido debe tener al menos 2 caracteres.';
  }
  return null;
};

export const validateEmail = (value) => {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$/;
  if (!value || !emailRegex.test(value.trim())) {
    return 'Por favor, ingresa un correo electrónico válido.';
  }
  return null;
};

export const validatePassword = (value) => {
  const minLength = 8;
  const hasUpperCase = /[A-Z]/.test(value);
  const hasLowerCase = /[a-z]/.test(value);
  const hasNumber = /[0-9]/.test(value);
  const hasSpecialChar = /[!@#$%^&*(),.?":{}|<>]/.test(value);

  if (!value) {
    return 'La contraseña es requerida.';
  }
  if (value.length < minLength) {
    return `La contraseña debe tener al menos ${minLength} caracteres.`;
  }
  if (!hasUpperCase) {
    return 'La contraseña debe contener al menos una letra mayúscula.';
  }
  if (!hasLowerCase) {
    return 'La contraseña debe contener al menos una letra minúscula.';
  }
  if (!hasNumber) {
    return 'La contraseña debe contener al menos un número.';
  }
  if (!hasSpecialChar) {
    return 'La contraseña debe contener al menos un carácter especial (!@#$%^&*(),.?":{}|<>).';
  }
  return null;
};

export const validateUserForm = (formData) => {
  const errors = {};
  const firstNameError = validateFirstName(formData.first_name);
  if (firstNameError) {
    errors.first_name = firstNameError;
  }
  const lastNameError = validateLastName(formData.last_name);
  if (lastNameError) {
    errors.last_name = lastNameError;
  }
  const emailError = validateEmail(formData.email);
  if (emailError) {
    errors.email = emailError;
  }
  const passwordError = validatePassword(formData.password);
  if (passwordError) {
    errors.password = passwordError;
  }
  return errors;
};
