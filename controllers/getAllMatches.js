const connectDB = require('../connect');

const getAlMatches = async(req, res) => {
    try {
        const db = await connectDB();
        const collection = db.collection('cricket');
        const matches = await collection.find({}).toArray();
        res.status(200).json(matches);
    } catch (error) {
        console.error('Error retrieving matches:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

module.exports = getAlMatches;