const connectDB= require('../connect');

const createMatch = async(req, res) => {
    try {
        const db = await connectDB();
        const collection = db.collection('cricket');
        const matchData = req.body;

        const result = await collection.insertOne(matchData);

        res.status(201).json({ message: 'Match created successfully', matchId: result.insertedId });
    } catch (error) {
        console.error('Error creating match:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

module.exports = createMatch;