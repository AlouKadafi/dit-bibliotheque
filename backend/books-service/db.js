const { Pool } = require("pg");

const pool = new Pool({
  user: "dit_user",
  host: "localhost",
  database: "dit_bibliotheque",
  password: "dit_password",
  port: 5432,
});

module.exports = pool;