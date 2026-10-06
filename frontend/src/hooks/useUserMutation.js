import { useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';

const useUserMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (data) => {
      const response = await axios.post('/api/v1/users/', data);
      return response.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['users'] });
    },
    onError: (error) => {
      // Propagar el error para que el componente lo maneje
      throw error;
    }
  });
};

export default useUserMutation;
