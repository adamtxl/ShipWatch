--Users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Saved Searches
CREATE TABLE saved_searches (
    search_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    destination VARCHAR(255),
    price_min DECIMAL(10, 2),
    price_max DECIMAL(10, 2),
    departure_date DATE,
    return_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Prices
CREATE TABLE prices (
    price_id SERIAL PRIMARY KEY,
    search_id INT REFERENCES saved_searches(search_id) ON DELETE CASCADE,
    price DECIMAL(10, 2) NOT NULL,
    detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

--Watched Cruises
CREATE TABLE watched_cruises (
    watch_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    cruise_name VARCHAR(255),
    departure_port VARCHAR(255),
    departure_date DATE,
    return_date DATE,
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- #notifications
CREATE TABLE notifications (
    notification_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id) ON DELETE CASCADE,
    search_id INT REFERENCES saved_searches(search_id),
    watch_id INT REFERENCES watched_cruises(watch_id),
    message TEXT NOT NULL,
    sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

