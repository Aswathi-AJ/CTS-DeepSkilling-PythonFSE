import React from 'react';
export default function Header({ siteName, enrolledCount }) {
  return (
    <header className="header">
      <h1>{siteName}</h1>
      <nav>
        <ul>
          <li><a href="#courses">Courses</a></li>
          <li><a href="#profile">Profile</a></li>
          <li className="badge-nav">Enrolled: {enrolledCount}</li>
        </ul>
      </nav>
    </header>
  );
}
