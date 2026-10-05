import { useQuery } from '@tanstack/react-query';
import axios from 'axios';

export const useWorkoutQuery = (id) => {
  return useQuery({
    queryKey: ['workout', id],
    queryFn: async () => {
      const response = await axios.get(`/api/v1/workouts/${id}`);
      return response.data;
    },
  });
};
