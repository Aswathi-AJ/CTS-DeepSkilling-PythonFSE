import React from 'react';
export default function CourseCard({ name, code, credits, grade, onEnroll, isEnrolled }) {
  return (
    <div className="course-card">
      <h3>{name}</h3>
      <p><strong>Code:</strong> {code}</p>
      <p><strong>Credits:</strong> {credits} | <strong>Grade:</strong> {grade}</p>
      <button 
        className={`btn-enroll ${isEnrolled ? 'enrolled' : ''}`} 
        onClick={onEnroll} 
        disabled={isEnrolled}
      >
        {isEnrolled ? 'Enrolled ✓' : 'Enroll Now'}
      </button>
    </div>
  );
}
