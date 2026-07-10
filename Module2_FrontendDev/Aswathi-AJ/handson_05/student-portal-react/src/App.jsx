import React, { useState, useEffect } from 'react';
import Header from './components/Header';
import Footer from './components/Footer';
import CourseCard from './components/CourseCard';
import StudentProfile from './components/StudentProfile';

export default function App() {
  const [courses, setCourses] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [enrolledCourses, setEnrolledCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('https://jsonplaceholder.typicode.com/posts?_limit=5')
      .then((res) => {
        if (!res.ok) throw new Error('Failed to fetch courses from server.');
        return res.json();
      })
      .then((data) => {
        // Map posts to course-like objects (Step 71)
        const mappedCourses = data.map((item, idx) => ({
          id: item.id,
          name: item.title.slice(0, 25),
          code: `CS${101 + idx}`,
          credits: (idx % 2 === 0) ? 4 : 3,
          grade: 'A'
        }));
        setCourses(mappedCourses);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  // Step 75: useEffect dependency array logging
  useEffect(() => {
    if (courses.length > 0) {
      console.log('Courses updated successfully.');
    }
  }, [courses]); // Dependency array ensures effect runs ONLY when 'courses' state updates

  // Step 69: Lift state up handler for enrollment
  const handleEnroll = (course) => {
    if (!enrolledCourses.some((c) => c.id === course.id)) {
      setEnrolledCourses([...enrolledCourses, course]);
    }
  };

  const filteredCourses = courses.filter((course) =>
    course.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="app-container">
      {/* Step 64 & 70: Pass siteName and enrolledCount props to Header */}
      <Header siteName="Student Portal (React)" enrolledCount={enrolledCourses.length} />

      <main className="main-content">
        <section className="search-section">
          <h2>Browse Enrolled Courses</h2>
          {/* Step 68: Search Input */}
          <input
            type="text"
            className="search-input"
            placeholder="Search courses by title..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </section>

        {/* Step 72: Render loading state */}
        {loading && <div className="spinner-box">Loading courses...</div>}
        {error && <div className="error-box">{error}</div>}

        {!loading && !error && (
          <div className="course-grid">
            {/* Step 67: Dynamic list rendering with key prop */}
            {filteredCourses.map((course) => (
              <CourseCard
                key={course.id}
                {...course}
                onEnroll={() => handleEnroll(course)}
                isEnrolled={enrolledCourses.some((c) => c.id === course.id)}
              />
            ))}
          </div>
        )}

        {/* Step 74: Student Profile Form */}
        <StudentProfile />
      </main>

      {/* Step 63 & 64: Footer Component */}
      <Footer />
    </div>
  );
}
