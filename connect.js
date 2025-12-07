const {MongoClient} = require('mongodb');
const uri = process.env.MONGODB_URI;

let client;
let db;
const connectDB = async() => {
    if (db) return db;
    try {
        client = new MongoClient(uri);
        await client.connect();
        db = client.db('test');
        console.log('Connected to MongoDB successfully');
        return db;
    } catch (error) {
        console.error('Error connecting to MongoDB:', error);
        throw error;
    }
}

module.exports = connectDB;