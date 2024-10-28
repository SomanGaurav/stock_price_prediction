const express = require("express"); 
const router = express.Router(); 

const getData = require("../services/data.json")


router.route('/').get((req , res) => {
    res.send(getData)
})



module.exports = router ; 