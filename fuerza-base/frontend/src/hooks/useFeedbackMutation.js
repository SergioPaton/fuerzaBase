import { useMutation, useQueryClient } from '@tanstack/react-query';
import axios from 'axios';

export const useFeedbackMutation = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async (data) => {
      const response = await axios.post('/api/v1/feedback', data);
      return response.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['feedback'] });
    },
  });
};
