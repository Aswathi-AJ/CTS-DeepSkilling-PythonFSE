import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import { getAllCourses } from '../api/courseApi';

// Step 143: Async Thunk using createAsyncThunk
export const fetchAllCoursesThunk = createAsyncThunk(
  'courses/fetchAll',
  async (_, { rejectWithValue }) => {
    try {
      const data = await getAllCourses();
      return data;
    } catch (error) {
      return rejectWithValue(error.message || 'Failed to fetch courses');
    }
  }
);

const initialState = {
  courses: [],
  loading: false,
  error: null
};

// Step 144: Handle the three thunk lifecycle actions in extraReducers
const coursesSlice = createSlice({
  name: 'courses',
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      // Pending
      .addCase(fetchAllCoursesThunk.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      // Fulfilled
      .addCase(fetchAllCoursesThunk.fulfilled, (state, action) => {
        state.loading = false;
        state.courses = action.payload.map((item, idx) => ({
          id: item.id,
          name: item.title.slice(0, 25),
          code: `CS${101 + idx}`,
          credits: 4
        }));
      })
      // Rejected
      .addCase(fetchAllCoursesThunk.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload || 'An error occurred while fetching courses.';
      });
  }
});

// Step 146: Selectors
export const selectCourses = (state) => state.courses.courses;
export const selectCoursesLoading = (state) => state.courses.loading;
export const selectCoursesError = (state) => state.courses.error;

export default coursesSlice.reducer;
