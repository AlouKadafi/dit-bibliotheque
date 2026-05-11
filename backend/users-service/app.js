const express = require("express");

const app = express();
const PORT = 3002;

app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    service: "users-service",
    status: "running"
  });
});

app.listen(PORT, () => {
  console.log(`Users service running on port ${PORT}`);
});