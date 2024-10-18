const express = require("express");
const mongoose = require("mongoose");
const app = express();
const cors = require("cors");
const Router = express.Router;
const dotenv = require("dotenv");

const { userRouter } = require("./Routes/user");

dotenv.config();

app.use(cors());
app.use(express.json());
app.use("/user", userRouter);

async function main() {
  await mongoose.connect(process.env.DB_CONNECT.toString());
  app.listen(3000);
}
main();
