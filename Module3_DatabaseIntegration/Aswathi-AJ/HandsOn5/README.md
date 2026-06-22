# Hands-On 5 - MongoDB Document Modelling, CRUD & Aggregation

## Task 1: Document Modelling

* Created the `college_nosql` database.
* Created the `feedback` collection.
* Inserted sample feedback documents using MongoDB.
* Demonstrated MongoDB's flexible schema by storing a document without the `attachments` field.
* Verified document insertion using `countDocuments()`.

## Task 2: CRUD Operations

* Retrieved documents using `find()`.
* Filtered feedback based on rating and tags.
* Used projection to display selected fields.
* Updated documents using `updateMany()` and `$set`.
* Modified array fields using `$push`.
* Deleted documents using `deleteMany()`.

## Task 3: Aggregation Pipeline

* Built aggregation pipelines using `aggregate()`.
* Filtered documents using `$match`.
* Grouped records using `$group`.
* Calculated average ratings using `$avg`.
* Counted feedback records using `$sum`.
* Sorted results using `$sort`.
* Formatted output using `$project`.
* Rounded values using `$round`.
* Used `$unwind` to analyze tag frequency.
* Created an index on `course_code`.
* Verified index usage using `explain()` and observed `IXSCAN`.

## Concepts Practiced

* MongoDB Database and Collection
* Documents and Fields
* Schema-less Data Modelling
* Arrays and Embedded Documents
* CRUD Operations
* Aggregation Pipeline
* $match, $group, $avg, $sum
* $project, $round, $sort
* $unwind
* Indexing
* Query Execution Analysis (IXSCAN)

## Status

Hands-On 5 Completed.
