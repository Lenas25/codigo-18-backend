const express = require("express");
const { getBooks, createBook, getBookById, deleteBook, updateBook } = require("../controller/bookController")

const router = express.Router();

router.get("/books", getBooks);
router.get("/books/:id", getBookById);
router.post("/books", createBook);
router.put("/books/:id", updateBook);
router.delete("/books/:id", deleteBook);

module.exports = router