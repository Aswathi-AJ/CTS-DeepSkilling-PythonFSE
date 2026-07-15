import apiClient from './apiClient';

// Step 139: Exported API functions consuming centralized apiClient
export const getAllCourses = () => {
  return apiClient.get('/posts?_limit=5');
};

export const getCourseById = (id) => {
  return apiClient.get(`/posts/${id}`);
};

export const enrollStudent = (studentId, courseId) => {
  return apiClient.post('/posts', {
    userId: studentId,
    courseId: courseId,
    enrolledAt: new Date().toISOString()
  });
};
