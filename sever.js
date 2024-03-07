const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();

app.use(cors());

// MongoDB URL
const mongoDB = 'mongodb+srv://user_fyp:YxQNKAF8qYGSBHIT@cluster0.a5jdgea.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0';

mongoose.connect(mongoDB, { useNewUrlParser: true, useUnifiedTopology: true }).then(() => {
    console.log('Connected to database');
}).catch((error) => {
    console.error('Connection error', error.message);
});

// Define a simple schema for demand and demand_forecasting
const Schema = mongoose.Schema;
const DemandSchema = new Schema({
    date_time: String,
    demand: Number
});
const ForecastingSchema = new Schema({
    date_time: String,
    demand_forcasting: Number
});

// Create models
const Demand = mongoose.model('Demand', DemandSchema, 'demand');
const Forecasting = mongoose.model('Forecasting', ForecastingSchema, 'demand_forcasting');

// Routes
app.get('/api/demand', async (req, res) => {
    try {
        const demands = await Demand.find({});
        res.json(demands);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

app.get('/api/forecasting', async (req, res) => {
    try {
        const forecastings = await Forecasting.find({});
        res.json(forecastings);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
