
# ShipWatch

**ShipWatch** is a cruise price tracking application designed to help users search for cruises, save searches, track price changes, and receive notifications when relevant deals are found. This project is in its infancy, and functionality is being developed incrementally.

---

## **Current Version**

- **Version:** 0.0.0.1
- **Status:** Pre-alpha (basic framework set up)

---

## **Core Features**

### Future Features (Planned)
- **User Authentication**
  - Users can register, log in, and log out securely.
  - Users will have profiles to set preferences and manage saved searches.

- **Cruise Search**
  - Integrate with external APIs to fetch cruise results in real-time.
  - Allow users to filter results by destination, price, cruise line, etc.

- **Save Searches**
  - Enable users to save search criteria for quick reuse.
  - Store search data in a PostgreSQL database.

- **Track Cruises**
  - Allow users to watch specific cruises for price changes.
  - Display historical price trends for tracked cruises.

- **Notifications**
  - Send email alerts when saved searches match new results.
  - Notify users of price changes for tracked cruises.

---

## **Current Functionality**

| Feature                   | Status         | Notes                              |
|---------------------------|----------------|------------------------------------|
| Basic Framework           | ✅ In place    | Flask API and placeholder route   |
| Cruise Search API         | 🚧 In progress | Returns hardcoded sample data     |
| User Authentication       | 🚧 Not started |                                    |
| Save Searches             | 🚧 Not started |                                    |
| Track Cruises             | 🚧 Not started |                                    |
| Notifications             | 🚧 Not started |                                    |
| Database Setup            | 🚧 Not started | PostgreSQL schema pending design  |

---

## **Development Setup**

### Prerequisites
- Python 3.9+
- PostgreSQL
- Flask

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/username/shipwatch.git
   cd shipwatch
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the server:
   ```bash
   python app.py
   ```
4. Access the app at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## **Roadmap**

### **Version 0.0.0.1**
- [x] Create Flask app with basic structure.
- [x] Add placeholder route for `/api/cruise_prices`.
- [ ] Define app functionality and database schema.

### **Version 0.1.0**
- [ ] Implement basic user authentication (log in, log out).
- [ ] Set up database with PostgreSQL.
- [ ] Connect `/api/cruise_prices` to fetch real cruise data via API.

### **Version 0.2.0**
- [ ] Enable saving searches and tracking specific cruises.
- [ ] Add notification system for saved searches.

### **Version 0.3.0**
- [ ] Refine UI for search and saved results.
- [ ] Add data visualization for price trends.

---

## **Contributing**

We welcome contributions! Please fork the repository and submit a pull request for review.

---

## **License**

This project is licensed under the MIT License.
