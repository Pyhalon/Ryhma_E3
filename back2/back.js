// tarvittavat moduulit:
// npm install express
// npm install cors
// npm install node-fetch@2

// backin kaynnistys:
// node back.js

// voi testata curlilla jos asennettuna (linux):
// curl -i -X GET http://localhost:3001/api/price/2024-03-22/10

const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const cors = require('cors')
const fetch = require('node-fetch') 

app.use(bodyParser.json())
app.use(cors())

const PRICE_ENDPOINT = 'https://api.porssisahko.net/v1/price.json';

async function getPrice(date, hour) {
    // date: 2024-03-23
    // hour: 10
    const params = `date=${date}&hour=${hour}`;
    const response = await fetch(`${PRICE_ENDPOINT}?${params}`);
    const { price } = await response.json();
    return price;
}

app.get('/api/price/:date/:hour', (req, res) => {
    const date = String(req.params.date)
    const hour = String(req.params.hour)
    
    getPrice(date, hour).then(function(data){
        res.json(data);
    });
})

const PORT = process.env.PORT || 3001
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`)
})
