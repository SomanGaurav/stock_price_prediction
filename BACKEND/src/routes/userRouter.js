const { Router } = require("express");
const jwt = require("jsonwebtoken");
const { userModel } = require("../models/userDb.js");
const userRouter = Router();
const bcrypt = require("bcrypt");
const z = require("zod");
const JWT_SECRET = require("../../config.js");
const { userMiddleware } = require("../middleware/userMid.js");

userRouter.post("/signup", async function (req, res) {
  const requireBody = z.object({
    firstName: z.string().min(3).max(30),
    lastName: z.string().min(3).max(30),
    email: z.string().min(3).max(30).email(),
    password: z
      .string()
      .min(8)
      .max(30)
      .refine((password) => /[A-Z]/.test(password), {
        message: "uppercaseErrorMessage",
      })
      .refine((password) => /[a-z]/.test(password), {
        message: "lowercaseErrorMessage",
      })
      .refine((password) => /[0-9]/.test(password), {
        message: "numberErrorMessage",
      })
      .refine((password) => /[!@#$%^&*]/.test(password), {
        message: "specialCharacterErrorMessage",
      }),
  });
  const parsedData = requireBody.safeParse(req.body);
  if (!parsedData.success) {
    res.json({
      message: "incorrect format",
      error: parsedData.error,
    });
    return;
  }
  try {
    const { firstName, lastName, password, email } = req.body;
    const hashedPassword = await bcrypt.hash(password, 5);
    await userModel.create({
      email,
      password: hashedPassword,
      firstName,
      lastName,
    });
    res.json({
      message: "sucessful signup",
    });
  } catch (e) {
    throw new Error(e);
  }
});
userRouter.post("/signin", async function (req, res) {
  const { password, email } = req.body;
  const response = await userModel.findOne({
    email: email,
  });
  const passwordMatch = await bcrypt.compare(password, response.password);

  if (passwordMatch) {
    const token = jwt.sign({ id: response._id }, JWT_USER_PASSWORD);
    res.json({ token });
  } else {
    res.status(403).json({
      message: "wrong ID or Password",
    });
  }
});

module.exports = {
  userRouter,
};
