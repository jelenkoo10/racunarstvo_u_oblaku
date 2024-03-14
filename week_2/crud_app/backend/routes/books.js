const express = require("express");
const router = express.Router();

const BooksController = require("../controllers/booksController");

router.post("/", BooksController.createBook);
router.get("/", BooksController.getAllBooks);
router.get("/:id", BooksController.getBookById);
router.put("/:id", BooksController.updateBook);
router.delete("/:id", BooksController.deleteBook);

module.exports = router;
