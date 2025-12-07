const connectDB = require('../connect');

const deleteMatch = async (req, res) => {
    try {
        const { id } = req.params;

        const db = await connectDB();
        const collection = db.collection('cricket');

        const result = await collection.deleteOne({ _id: id });

        if (result.deletedCount === 0) {
            return res.status(404).json({ error: 'Match not found' });
        }

        res.status(200).json({ message: 'Match deleted successfully' });
    } catch (error) {
        console.error('Error deleting match:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}

module.exports = deleteMatch;