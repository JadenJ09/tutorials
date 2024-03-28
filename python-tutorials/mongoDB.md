NoSQL: Non relational database for unstructured data: Graph, Documents, Columns focused data

Mongo DB

Data modeling: Since NoSQL is not following schema-oriented data structure, it is needed to model data structure.
    Modeling relationships in MongoDB:
        Embedded documents:
        - this type of data model where we find related data lumped together into a single collection is known as a denormalized data model.
          - one-to-one relationship: one entity contains another
          - one-to-many relationship: one entity contains many sub-entities
        References:
        - This type of data model where we find related data via a link is known as a normalized data model and typically mimics how a relational database creates relationships between data.
          - many-to-many relationship: one entity can be mapped to many instances of another entity
            - //Car Document
              {
              car_id: 48273
              model_name: "Corvette",
              engine_id: 2165
              }

              // Engine Document
              {
              id: 2165
              engine_power: 490,
              engine_type: "V8",
              acceleration: "High"
              }

    Examples:
    Case A: A time management application that stores one user per task. We want to store details about the task, such as the task name, the task due date, and the user assigned to the task (and their associated details). There can only be one person assigned to each task.

        {
            task: "Review Rough Outline",
            due: "2022/09/03 09:00",
            assignee: {
                name: "Alex",
                role: "SME",
                contact: "alex@example.com"
            }
        }

    Case B: A contact information management application that can store multiple addresses per user. The application would store important details for the person such as their name, as well as their associated addresses.

        {
            first_name: "Alex",
            last_name: "Smith",
            addresses: [
                { label: "home", value: { address: "123 4th Street", city: "Toronto", region: "ON", country: "Canada", postcode: "M1S 2J8" } },
                { label: "work", value: { address: "1633 Broadway 38th floor", city: "New York", region: "NY", country: "USA", postcode: "10019" } },
                "
            ]
        }

        if the addresses are duplicated too many times, we may consider using references instead.\

        // Addresses Collection
        {
            _id: 123456789
            address: {    
                street: "123 4th Street", 
                city: "Toronto", 
                region: "ON", 
                country: "Canada", 
                postcode: "M1S 2J8" 
            }
            },
            { 
            _id: 9292944,
            address: { 
                street: "1633 Broadway 38th floor",
                city: "New York", 
                region: "NY", 
                country: "USA", 
                postcode: "10019" 
            } 
        }

        // User Collection 
        {
            first_name: "Alex",
            last_name: "Smith"
            addresses: [ 123456789, 9292944 ] 
            },
            {
            first_name: "Josh",
            last_name: "Gold",
            addresses: [ 123456789 ] 
            },
            {
            first_name: "Timbo",
            last_name: "Gray",
            addresses: [ 123456789 ]
        }


    Case C: A school registration application that manages multiple students. Each student can be in multiple classes. Each class record can easily identify which students are registered and each student record can quickly find any associated classes. -> Many-to-many: refer to Case B's last part

## MongoDB CRUD 1.
### Finding Documents
#### Browsing and Selecting Collections

show dbs
db: show current db
use [database name]
show collections

db.[collections' name].find({key: "value"})
db.[collections' name].find({"key.inkey": "value"})
db.[collections' name].find({key: {$lt: "value"}})
db.listingsAndReviews.find({"address.street": {$lte:"C"}})
db.listingsAndReviews.find({borough: "Queens"}).sort({"address.zipcode": -1})

db.listingsAndReviews.find({borough: "Bronx"}, {_id: 1, name: 1, cuisine: 1}) # WHERE / SELECT
db.listingsAndReviews.find({ michelin_stars: [2019, 2020] }) # list
db.listingsAndReviews.find({ michelin_stars: { $all: [ 2018, 2019 ] } })
db.listingsAndReviews.find({michelin_stars: {$gt: 2015, $lt: 2010}})
db.listingsAndReviews.find({michelin_stars: {$elemMatch: {$gte: 2005, $lte: 2010}}})

db.listingsAndReviews.find({ grades: {date: ISODate("2014-07-11T00:00:00.000Z"), grade: 'A', score: 8} }) #multiple nested keys
db.listingsAndReviews.find({ "grades.grade": "C" }) #single nested key

db.articles.find({ tags: { $all: ["ssl", "security"] } }) #with find() to specify values
db.articles.find({ $and: [{ tags: ["ssl", "security"] }] }) #the both are same

db.channels.find({avg_views: {$gte: 10000}}, {streamer: 1, avg_views: 1}).sort({avg_views: -1})
db.channels.find({followers: {$elemMatch: {is_subscribed: true}}}).count()

- comparison operators: $gt $lt $gte $lte $e $ne
- $exists, $all, $elemMatch #at least one, $in, $nin, $size #with find()
- logical operators: $and $or $nor $not
- methods: .count() .limit() .find() .sort() .pretty()

## MongoDB CRUD 2.
### Inserting and Updating
db.listingsAndReviews.insertOne({name: "Elvins", cuisine: "American", restaurant_id: "40564243"})
db.listingsAndReviews.findOne({restaurant_id: "40564243"})
db.listingsAndReviews.insertMany([
  {
    name: "Boucherie", 
    borough: "Manhattan", 
    cuisine: "American", 
   restaurant_id: "49246215"
  }, 
  {
    name: "Carmines", 
    borough: "Manhattan", 
    cuisine: "Italian", 
    restaurant_id: "48259401"
  }
])

db.<collection>.updateOne(<filter>, <update>, <options>) // $set <-> $unset, $push
db.listingsAndReviews.updateOne({restaurant_id: "50014008"}, {$set: {cuisine: "American"}})
db.listingsAndReviews.updateOne({restaurant_id: "40561796"}, {$set: {"address.street": "58 street"}})
db.listingsAndReviews.updateOne({ name: "Cafe Bar" }, { $push: { grades: { date: new Date(), grade: "B", score: 81 } } })
db.<collection>.updateOne(<filter>, <update>, { upsert: <boolean> })
db.listingsAndReviews.updateOne({name: "Vinnys"}, {$set: {borough: "Queens", cuisine: "Italian"}}, {upsert: true})
db.employees.updateMany({ salary: 75000 }, { $set: { salary: 80000 }})

db.<collection>.findOneAndUpdate()
db.<collection>.renameCollection()
db.<collection>.bulkWrite()
db.<collection>.findAndModify({
  query: <document>,
  update: <document>,
  new: <boolean>,
  upsert: <boolean>,
  ...
});
db.listingsAndReviews.findAndModify({query: {name: "Jolie Cantina"}, update: {cuisine: "American"}, new: true})
{ _id: ObjectId("5eb3d669b31de5d588f45ddb"), cuisine: 'American' }
db.listingsAndReviews.findAndModify({query: {name: "Jacobs Bagels"}, update: {name: "Jacobs Bagels", cuisine: "Jewish/Kosher", borough: "Brooklyn"}, new: true, upsert: true})

### Deleting and Replacing
db.<collection>.deleteOne(<filter>, <options>)
db.listingsAndReviews.deleteMany({borough: "Rhode Island"})

db.<collection>.replaceOne(<filter>, <replacement>, <options>)
db.listingsAndReviews.replaceOne({name: "Tasty House"}, {name: "Tasty House", shut_down: true}) #replaceOne() replaces the whole document, so any unused fields will not populate. Different with updateOne

db.<collection>.findOneAndReplace(<filter>, <replacement>, <options>)
db.<collection>.findOneAndDelete(<filter>, <options>)


## Indexing
Single-field Index, Compound Index, Multikey Index

### Create Index
db.<collection>.createIndex({ <keys>, <options>, <commitQuorum>)} #single-field index #single multikey index is looking same but the index value is consist of arrays e.g. key: [v1, v2, v3], so mongoDB will capture and create automatically

db.<collection>.find(...).explain(<verbose>)
db.listingsAndReviews.find({name: "Osaka Japanese Fusion"}).explain("executionStats")

db.listingsAndReviews.createIndex({borough: 1, cuisine: -1}) #compound index #multikey index on compound fields is looking same but the index value is consist of arrays e.g. key: [v1, v2, v3], so mongoDB will capture and create automatically

### Delete Index
db.students.getIndexes();
db.students.dropIndex('sports_-1');


## Aggregation Pipeline
db.<collection>.aggregate()

db.movies.aggregate([
  {
    $match: {rating: "R"}
  }
])

db.students.aggregate([
  {
    // First stage
    $match: {grade_level: 6, average_test_score: {$gt: 97}}
  }
])

db.students.aggregate([
  {
    // First stage
    $match: {grade_level: 6, average_test_score: {$gt: 97}}
  },
  { 
    // Second Stage
    $sort: { first_name: 1} 
  }
])

db.students.aggregate([
  {
    // First stage
    $match: {grade_level: 6, average_test_score: {$gt: 97}}
  },
  { 
    // Second Stage
    $sort: { first_name: 1} 
  },
  { 
    // Third Stage
    $addFields:  {
      highest_score: { $max: "$test_scores" }  
    }
  }
])

db.students.aggregate([
  {
    // First stage
    $match: {grade_level: 6, average_test_score: {$gt: 97}}
  },
  { 
    // Second Stage
    $sort: { first_name: 1} 
  },
  { 
    // Third Stage
    $addFields:  {
      highest_score: { $max: "$test_scores" }  
    }
  },
  {
    // Fourth Stage
    $out : "candidates" #Creating a new collection #It can also output the result to a new db
  }
])

**In essence, consider using aggregation when:**
There are no CRUD methods (or a combination of methods) that accomplishes the query that needs to be performed easily.
We need to perform analysis on datasets such as grouping values from multiple documents, computations on data, and analyzing data changes over time.

