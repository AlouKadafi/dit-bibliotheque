const express = require("express");

const app = express();
const PORT = 3001;
const pool = require("./db");

app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    service: "books-service",
    status: "running"
  });
});

pool.query("SELECT NOW()")
  .then(() => {
    console.log("Connected to PostgreSQL");
  })
  .catch((err) => {
    console.error("Database connection error:", err.message);
  });

app.listen(PORT, () => {
  console.log(`Books service running on port ${PORT}`);
});