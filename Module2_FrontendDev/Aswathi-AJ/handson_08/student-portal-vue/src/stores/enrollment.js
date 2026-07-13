import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

export const useEnrollmentStore = defineStore('enrollment', () => {
  // Reactive state
  const enrolledCourses = ref([]);

  // Computed getter for total credits
  const totalCredits = computed(() => {
    return enrolledCourses.value.reduce((sum, course) => sum + course.credits, 0);
  });

  // Action: Enroll course
  function enroll(course) {
    const exists = enrolledCourses.value.some((c) => c.id === course.id);
    if (!exists) {
      enrolledCourses.value.push(course);
    }
  }

  // Action: Unenroll course
  function unenroll(courseId) {
    enrolledCourses.value = enrolledCourses.value.filter((c) => c.id !== courseId);
  }

  return { enrolledCourses, totalCredits, enroll, unenroll };
});
