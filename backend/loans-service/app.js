const express = require("express");

const app = express();
const PORT = 3003;

app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    service: "loans-service",
    status: "running"
  });
});

app.listen(PORT, () => {
  console.log(`Loans service running on port ${PORT}`);
});