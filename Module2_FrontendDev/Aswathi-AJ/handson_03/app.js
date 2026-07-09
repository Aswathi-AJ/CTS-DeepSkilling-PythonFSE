import { courses } from "./data.js";

courses.forEach(course => {
    const { name, credits } = course;
    console.log(`${name} - ${credits} credits`);
});

const courseList = courses.map(course =>
    `${course.code} — ${course.name} (${course.credits} credits)`
);
console.log(courseList);

const filteredCourses = courses.filter(course => course.credits >= 4);
console.log("Courses with credits >= 4:", filteredCourses.length);

const totalCredits = courses.reduce(
    (total, course) => total + course.credits,
    0
);
console.log("Total Credits:", totalCredits);

const courseGrid = document.querySelector(".course-grid");
const totalCreditsText = document.getElementById("total-credits");
const searchInput = document.getElementById("search-courses");
const sortButton = document.getElementById("sort-btn");
const selectedCourse = document.getElementById("selected-course");

const renderCourses = (courseArray) => {

    courseGrid.innerHTML = "";

    courseArray.forEach(course => {

        const article = document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p><strong>Code:</strong> ${course.code}</p>
            <p><strong>Credits:</strong> ${course.credits}</p>
        `;

        courseGrid.appendChild(article);

    });

    const total = courseArray.reduce(
        (sum, course) => sum + course.credits,
        0
    );

    totalCreditsText.textContent = `Total Credits: ${total}`;
};

renderCourses(courses);

searchInput.addEventListener("input", () => {
    const keyword = searchInput.value.toLowerCase();
    const result = courses.filter(course =>
        course.name.toLowerCase().includes(keyword)
    );
    renderCourses(result);
});

sortButton.addEventListener("click", () => {
    const sorted = [...courses].sort(
        (a, b) => b.credits - a.credits
    );
    renderCourses(sorted);
});


courseGrid.addEventListener("click", (event) => {
    const card = event.target.closest(".course-card");
    if (!card) return;
    const id = Number(card.dataset.id);
    const selected = courses.find(course => course.id === id);
    selectedCourse.textContent =
        `Selected Course: ${selected.name} | Grade: ${selected.grade}`;

});