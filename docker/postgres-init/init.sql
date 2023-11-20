CREATE TABLE IF NOT EXISTS inventory_history (
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    item TEXT,
    amount INT,
    location TEXT,
    categories TEXT[]
);
CREATE INDEX IF NOT EXISTS idx_timestamp ON inventory_history (timestamp);
CREATE TABLE IF NOT EXISTS favourite_items (
    id SERIAL PRIMARY KEY,
    item TEXT UNIQUE
);
CREATE TABLE IF NOT EXISTS favourite_recipes (
    id SERIAL PRIMARY KEY,
    name TEXT,
    ingredients TEXT[],
    instructions TEXT,
    categories TEXT[]
);
