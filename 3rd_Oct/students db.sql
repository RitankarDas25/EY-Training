db["students"].find()
 
use university
switched to db university
// insert one student
db.students.insertOne({
  student_id:1,
  name:"Rahul",
  age : 21,
  city :"Mumbai",
  course : "AI",
  marks : 85
})
{
  acknowledged: true,
  insertedId: ObjectId('68dfa49ea1976a88b88df2ec')
}
db.students.insertMany([
  {student_id:2,  name:"Raj",  age : 21,  city :"Blr",  course : "AI",  marks :77},
  {student_id:1,  name:"Priya",  age : 25,  city :"Mumbai",  course : "AI",  marks : 55},
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfa69fa1976a88b88df2ed'),
    '1': ObjectId('68dfa69fa1976a88b88df2ee')
  }
}
db.students.insertMany([
  {student_id:3,  name:"Raju",  age : 21,  city :"Ccu",  course : "ML",  marks :77},
  {student_id:4,  name:"Sonali",  age : 25,  city :"goa",  course : "AI",  marks : 15},
])
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfa716a1976a88b88df2ef'),
    '1': ObjectId('68dfa716a1976a88b88df2f0')
  }
}
db.students.find()
{
  _id: ObjectId('68dfa49ea1976a88b88df2ec'),
  student_id: 1,
  name: 'Rahul',
  age: 21,
  city: 'Mumbai',
  course: 'AI',
  marks: 85
}
{
  _id: ObjectId('68dfa69fa1976a88b88df2ed'),
  student_id: 2,
  name: 'Raj',
  age: 21,
  city: 'Blr',
  course: 'AI',
  marks: 77
}
{
  _id: ObjectId('68dfa69fa1976a88b88df2ee'),
  student_id: 1,
  name: 'Priya',
  age: 25,
  city: 'Mumbai',
  course: 'AI',
  marks: 55
}
{
  _id: ObjectId('68dfa716a1976a88b88df2ef'),
  student_id: 3,
  name: 'Raju',
  age: 21,
  city: 'Ccu',
  course: 'ML',
  marks: 77
}
{
  _id: ObjectId('68dfa716a1976a88b88df2f0'),
  student_id: 4,
  name: 'Sonali',
  age: 25,
  city: 'goa',
  course: 'AI',
  marks: 15
}
db.students.findOne({name:"Rahul"})
{
  _id: ObjectId('68dfa49ea1976a88b88df2ec'),
  student_id: 1,
  name: 'Rahul',
  age: 21,
  city: 'Mumbai',
  course: 'AI',
  marks: 85
}
db.students.find({marks: {$gt: 50}})
{
  _id: ObjectId('68dfa49ea1976a88b88df2ec'),
  student_id: 1,
  name: 'Rahul',
  age: 21,
  city: 'Mumbai',
  course: 'AI',
  marks: 85
}
{
  _id: ObjectId('68dfa69fa1976a88b88df2ed'),
  student_id: 2,
  name: 'Raj',
  age: 21,
  city: 'Blr',
  course: 'AI',
  marks: 77
}
{
  _id: ObjectId('68dfa69fa1976a88b88df2ee'),
  student_id: 1,
  name: 'Priya',
  age: 25,
  city: 'Mumbai',
  course: 'AI',
  marks: 55
}
{
  _id: ObjectId('68dfa716a1976a88b88df2ef'),
  student_id: 3,
  name: 'Raju',
  age: 21,
  city: 'Ccu',
  course: 'ML',
  marks: 77
}
db.students.find({},{name:1,course:1,_id:0})
{
  name: 'Rahul',
  course: 'AI'
}
{
  name: 'Raj',
  course: 'AI'
}
{
  name: 'Priya',
  course: 'AI'
}
{
  name: 'Raju',
  course: 'ML'
}
{
  name: 'Sonali',
  course: 'AI'
}
db.students.updateOne(
  {name: "Raj"},
  { $set :{marks:92 ,course:"DL"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedCount: 0
}
 
db.students.updateMany(
  {course: "AI"},
  { $set :{grade:"A"}}
)
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 3,
  modifiedCount: 3,
  upsertedCount: 0
}
db.students.deleteOne({name :"Arjun"})
{
  acknowledged: true,
  deletedCount: 0
}
db.students.deleteMany({marks : $lt: 50})
SyntaxError: Unexpected token, expected "," (1:35)

[0m[31m[1m>[22m[39m[90m 1 |[39m db[33m.[39mstudents[33m.[39mdeleteMany({marks [33m:[39m $lt[33m:[39m [35m50[39m})
 [90m   |[39m                                    [31m[1m^[22m[39m[0m
db.students.deleteMany({marks : {$lt: 50}})
