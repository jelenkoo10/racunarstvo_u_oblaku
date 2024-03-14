const mysql = require("mysql");

const conn = mysql.createConnection({
  // host: "172.18.0.2",
  host: "localhost",
  user: "root",
  password: "",
  database: "docker_books",
  port: 3306,
  connectTimeout: 20000,
});

conn.connect();

exports.createBook = (req, res) => {
  const { title, author, genre, publication_year } = req.body;
  const INSERT_BOOK_QUERY = `INSERT INTO books (title, author, genre, publication_year) VALUES ('${title}', '${author}', '${genre}', ${publication_year})`;
  conn.query(INSERT_BOOK_QUERY, (err, results) => {
    if (err) {
      return res.status(500).json({ error: "Error creating book..." });
    }
    return res.status(201).json({ message: "Book created successfully!" });
  });
};

exports.getAllBooks = (req, res) => {
  const SELECT_ALL_BOOKS_QUERY = "SELECT * FROM books";
  conn.query(SELECT_ALL_BOOKS_QUERY, (err, results) => {
    if (err) {
      return res.status(500).json({ error: "Error fetching books" });
    }
    return res.status(200).json(results);
  });
};

exports.getBookById = (req, res) => {
  const bookId = req.params.id;
  const SELECT_BOOK_QUERY = `SELECT * FROM books WHERE id = ${bookId}`;
  conn.query(SELECT_BOOK_QUERY, (err, results) => {
    if (err) {
      return res.status(500).json({ error: "Error fetching book..." });
    }
    if (results.length === 0) {
      return res.status(404).json({ error: "Book not found." });
    }
    return res.status(200).json(results[0]);
  });
};

exports.updateBook = (req, res) => {
  const bookId = req.params.id;
  const { title, author, genre, publication_year } = req.body;
  const UPDATE_BOOK_QUERY = `UPDATE books SET title = '${title}', author = '${author}', genre = '${genre}', publication_year = ${publication_year} WHERE id = ${bookId}`;
  conn.query(UPDATE_BOOK_QUERY, (err, results) => {
    if (err) {
      return res.status(500).json({ error: "Error updating book..." });
    }
    return res.status(200).json({ message: "Book updated successfully!" });
  });
};

exports.deleteBook = (req, res) => {
  const bookId = req.params.id;
  const DELETE_BOOK_QUERY = `DELETE FROM books WHERE id = ${bookId}`;
  conn.query(DELETE_BOOK_QUERY, (err, results) => {
    if (err) {
      return res.status(500).json({ error: "Error deleting book..." });
    }
    return res.status(200).json({ message: "Book deleted successfully!" });
  });
};
