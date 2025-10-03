use university
switched to db university
db["teachers"].find()

db.teachers.insertMany([
  {
    name: "Alice Johnson",
    subject: "Mathematics",
    email: "alice.johnson@example.com",
    experience: 5
  },
  {
    name: "Bob Smith",
    subject: "Physics",
    email: "bob.smith@example.com",
    experience: 8
  }
]);
{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68dfb3c17a277f06c935017d'),
    '1': ObjectId('68dfb3c17a277f06c935017e')
  }
}
db.teachers.find();
{
  _id: ObjectId('68dfb3c17a277f06c935017d'),
  name: 'Alice Johnson',
  subject: 'Mathematics',
  email: 'alice.johnson@example.com',
  experience: 5
}
{
  _id: ObjectId('68dfb3c17a277f06c935017e'),
  name: 'Bob Smith',
  subject: 'Physics',
  email: 'bob.smith@example.com',
  experience: 8
}
db.teachers.findOne({ name: "Alice Johnson" });
{
  _id: ObjectId('68dfb3c17a277f06c935017d'),
  name: 'Alice Johnson',
  subject: 'Mathematics',
  email: 'alice.johnson@example.com',
  experience: 5
}
db.teachers.updateMany(
  {},
  { $set: { department: "Science" } }
);
{
  acknowledged: true,
  insertedId: null,
  matchedCount: 2,
  modifiedCount: 2,
  upsertedCount: 0
}
db.teachers.deleteMany({ experience: { $lt: 5 } });
{
  acknowledged: true,
  deletedCount: 0
}
 
university
Selection deleted

