//TASK 1

// Question 60
// Created database: college_nosql

// Question 61
// Created collection: feedback

// Question 62
// Inserted 10 feedback documents.

// Question 63
// Inserted a document without the attachments field.
// MongoDB accepted the document because it supports a flexible schema.

// Question 64
db.feedback.countDocuments()

//TASK 2

// Question 65
db.feedback.find({ rating: 5 })

// Question 66
db.feedback.find({
    course_code: "CS101",
    tags: "challenging"
})

// Question 67
db.feedback.find({},{student_id: 1,course_code: 1,rating: 1,_id: 0})

// Question 68
db.feedback.updateMany({ rating: { $lt: 3 } },{ $set: { needs_review: true } })
db.feedback.find({ needs_review: true })

// Question 69
db.feedback.updateMany({ needs_review: true },{ $push: { tags: "reviewed" } })
db.feedback.find({ needs_review: true })

// Question 70
db.feedback.deleteMany({ semester: "2021-EVEN" })
db.feedback.find({ semester: "2021-EVEN" })