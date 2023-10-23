import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('DataWarehouse.db')
cursor = conn.cursor()

# Drop and recreate the Customers dimension table
cursor.execute("""DROP TABLE IF EXISTS Customers;""")
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(100)
)
''')

# Insert 5 records into the Customers table
cursor.executemany("""
INSERT INTO Customers (CustomerID, FirstName, LastName, Email, Phone, Address)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 'Gb', 'sires', 'gbsire@local.com', '0721592468', '123 Main St'),
    (2, 'Maggy', 'Blues', 'mgblue@local.com', '0746709675', '456 Elm St'),
    (3, 'Shakes', 'Tush', 'tushshakes@local.com', '0789061427', '789 Oak St'),
    (4, 'Nesh', 'Nash', 'neshnash@local.com', '0736325144', '321 Pine St'),
    (5, 'Mooh', 'Rick', 'moohrick@local.com', '0785193627', '555 Maple St')
])

#  Product Sales
cursor.execute("""DROP TABLE IF EXISTS Sales;""")

# Create the Sales fact table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Sales (
    SaleID INT PRIMARY KEY,
    CustomerID INT,
    ProductID INT,
    TimeID INT,
    Quantity INT,
    Amount DECIMAL(10, 2),

    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID),
    FOREIGN KEY (TimeID) REFERENCES Times(TimeID)
)
''')
# Insert 5 records into the Sales table
cursor.executemany("""
INSERT INTO Sales (SaleID, CustomerID, ProductID, TimeID, Quantity, Amount)
VALUES (?, ?, ?, ?, ?, ?)
""", [
    (1, 1, 1, 1, 3, 59.97),
    (2, 2, 2, 2, 1, 49.99),
    (3, 3, 3, 3, 2, 159.98),
    (4, 4, 4, 4, 1, 59.99),
    (5, 5, 5, 5, 5, 149.95)
])

conn.commit()
conn.close()
print("Database created.")
