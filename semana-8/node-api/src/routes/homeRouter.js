const express = require("express"); // -> acceso a get post put delete reemplazando la app
const { index } = require("../controller/homeController");

const router = express.Router();

router.get("/", index);

module.exports = router // -> export default