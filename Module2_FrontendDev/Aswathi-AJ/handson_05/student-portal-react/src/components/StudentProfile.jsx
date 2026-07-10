import React, { useState } from 'react';

export default function StudentProfile() {
  const [profile, setProfile] = useState({
    name: 'Aswathi AJ',
    email: 'aswathi@example.com',
    semester: '6'
  });
  const handleChange = (e) => {
    setProfile({ ...profile, [e.target.name]: e.target.value });
  };

  return (
    <section id="profile" className="profile-section">
      <h2>Student Profile</h2>
      <form className="profile-form" onSubmit={(e) => e.preventDefault()}>
        <label>
          Full Name:
          <input type="text" name="name" value={profile.name} onChange={handleChange} />
        </label>
        <label>
          Email:
          <input type="email" name="email" value={profile.email} onChange={handleChange} />
        </label>
        <label>
          Semester:
          <input type="number" name="semester" value={profile.semester} onChange={handleChange} />
        </label>
      </form>
      <div className="profile-summary">
        <p><strong>Logged in as:</strong> {profile.name} ({profile.email}) - Semester {profile.semester}</p>
      </div>
    </section>
  );
}
