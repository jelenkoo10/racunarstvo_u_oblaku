const express = require("express");
const bodyParser = require("body-parser");
const swaggerUi = require("swagger-ui-express");
const swaggerDocument = require("./swagger.json"); // Putanja do swagger.json fajla
const booksRouter = require("./routes/books");

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Dodatni kod za definisanje ruta i ostalog u tvom Express serveru
app.use("/books", booksRouter);

// Koristi Swagger UI Express za prikaz Swagger dokumentacije
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerDocument));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
