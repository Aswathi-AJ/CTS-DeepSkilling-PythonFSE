import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  enrolledCourses: []
};

const enrollmentSlice = createSlice({
  name: 'enrollment',
  initialState,
  reducers: {
    enroll: (state, action) => {
      // Immer handles immutable updates automatically
      const exists = state.enrolledCourses.some(c => c.id === action.payload.id);
      if (!exists) {
        state.enrolledCourses.push(action.payload);
      }
    },
    unenroll: (state, action) => {
      state.enrolledCourses = state.enrolledCourses.filter(c => c.id !== action.payload);
    }
  }
});

export const { enroll, unenroll } = enrollmentSlice.actions;
export default enrollmentSlice.reducer;
