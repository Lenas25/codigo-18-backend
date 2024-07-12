import express from "express";
import { getBooks, createBook, getBookById, deleteBook, updateBook, uploadFile } from "../controller/bookController";
import upload from "../config/upload"

const router = express.Router();

router.get("/books", getBooks);
router.get("/books/:id", getBookById);
router.post("/books", createBook);
router.put("/books/:id", updateBook);
router.delete("/books/:id", deleteBook);
// subir imagen
router.post('/upload', upload.single('file'), uploadFile);

export default router;