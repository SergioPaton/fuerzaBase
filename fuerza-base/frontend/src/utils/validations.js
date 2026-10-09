export const validateFirstName = (value) => {
  if (!value || value.trim().length < 2) {
    return 'El nombre debe tener al menos 2 caracteres.';
  }
  return null;
};

export const validateUserForm = (formData) => {
  const errors = {};
  const firstNameError = validateFirstName(formData.first_name);
  if (firstNameError) {
    errors.first_name = firstNameError;
  }
  return errors;
};
