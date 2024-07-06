
const prisma = require("../utils/db")

const getBooks = async (req, res) => {
  const books = await prisma.book.findMany();

  return res.json({
    books,
  });
};

const createBook = async (req, res) => {
  const book = req.body;

  const newBook = await prisma.book.create({
    data: {
      title: book?.title,
      author: book?.author,
      summary: book?.summary,
      isbn: book?.isbn,
      is_published: book?.is_published,
      published_date: new Date(book?.published_date),
    },
  });

  return res.status(201).json({
    message: "Libro creado",
    book: newBook,
  });
};

const getBookById = async (req, res) => {
  const bookId = Number(req.params.id); // id de la url

  const bookSearched = await prisma.book.findUnique({
    where: {
      id: bookId,
    },
  });

  if (!bookSearched) {
    return res.json({
      message: "No existe el libro buscado",
    });
  }

  return res.json({
    book: bookSearched,
  });
};

const updateBook = async (req, res) => {
  const existingBook = await prisma.book.findUnique({
    where: { id: Number(req.params.id) },
  });

  if (!existingBook) {
    return res.status(404).send({ message: "No se encontro el libro" });
  }

  const bookUpdated = await prisma.book.update({
    where: {
      id: Number(req.params.id),
    },
    // es la informacion que vamos a actualizar -> req.body
    data: req.body,
  });

  return res.status(200).json({
    book: bookUpdated,
  });
};

const deleteBook = async (req, res) => {
  const existingBook = await prisma.book.findUnique({
    where: { id: Number(req.params.id) },
  });

  if (!existingBook) {
    return res.status(404).send({ message: "No se encontro el libro" });
  }

  const bookDeleted = await prisma.book.delete({
    where: {
      id: Number(req.params.id),
    },
  });

  return res.json({
    message: "Eliminado correctamente",
    book: bookDeleted,
  });
};

module.exports = { getBooks, createBook, getBookById, updateBook, deleteBook }