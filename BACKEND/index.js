const express = require("express");
const mongoose = require("mongoose");
const app = express();
const cors = require("cors");
const Router = express.Router;
const dotenv = require("dotenv");
const { userRouter } = require("./routes/userRouter");

dotenv.config();

app.use(cors());
app.use(express.json());
app.use("/user", userRouter);

async function init() {
  await mongoose.connect(process.env.DB_CONNECT.toString());
  app.listen(3000);
  console.log("connect and listening on port 3000");
}
init();
