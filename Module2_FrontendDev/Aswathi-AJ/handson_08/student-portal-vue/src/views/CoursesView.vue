<template>
  <div class="courses-view">
    <h2>Course Catalog (Vue 3 Composition API)</h2>
    
    <div class="search-box">
      <!-- v-model binding to ref search term -->
      <input 
        type="text" 
        v-model="searchTerm" 
        placeholder="Filter courses using computed property..." 
      />
    </div>

    <div class="course-grid">
      <!-- v-for rendering with props binding -->
      <CourseCard 
        v-for="course in filteredCourses" 
        :key="course.id" 
        :name="course.name"
        :code="course.code"
        :credits="course.credits"
        :grade="course.grade"
        @enroll="handleEnroll(course)"
      />
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import CourseCard from '../components/CourseCard.vue';
import { useEnrollmentStore } from '../stores/enrollment';

const searchTerm = ref('');
const courses = ref([]);
const enrollmentStore = useEnrollmentStore();

onMounted(() => {
  // Initialise courses in onMounted hook
  courses.value = [
    { id: 1, name: 'Data Structures & Algorithms', code: 'CS101', credits: 4, grade: 'A' },
    { id: 2, name: 'Web Development Fundamentals', code: 'CS102', credits: 4, grade: 'A+' },
    { id: 3, name: 'Database Management Systems', code: 'CS201', credits: 3, grade: 'B+' },
    { id: 4, name: 'Operating Systems', code: 'CS202', credits: 4, grade: 'A' },
    { id: 5, name: 'Software Engineering Principles', code: 'CS301', credits: 3, grade: 'A' }
  ];
});

// Computed property for reactive filtering (cached)
const filteredCourses = computed(() => {
  return courses.value.filter(c => 
    c.name.toLowerCase().includes(searchTerm.value.toLowerCase())
  );
});

function handleEnroll(course) {
  enrollmentStore.enroll(course);
}
</script>

<style scoped>
.courses-view {
  padding: 1.5rem;
}
.search-box input {
  width: 100%;
  padding: 0.75rem;
  margin-bottom: 1.5rem;
  border-radius: 6px;
  border: 1px solid #cbd5e1;
}
.course-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}
</style>
