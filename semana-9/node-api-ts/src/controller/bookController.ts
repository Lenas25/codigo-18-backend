import type { Request, Response } from 'express'
import prisma from "../utils/db";

const getBooks = async (_req: Request, res: Response) => {
  const books = await prisma.book.findMany();

  return res.json({
    books,
  });
};

const createBook = async (req: Request, res: Response) => {
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

const getBookById = async (req: Request, res: Response) => {
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

const updateBook = async (req: Request, res: Response) => {
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

const deleteBook = async (req: Request, res: Response) => {
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

const uploadFile = async (req: Request, res: Response) => {
  if(!req.file){
    return res.status(400).json({message: "No se encontro la imagen a subir"})
  }
  return res.json({message: "Imagen subida correctamente"})
}

export { getBooks, createBook, getBookById, updateBook, deleteBook, uploadFile };