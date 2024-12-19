 cursor.execute('CREATE DATABASE IF NOT EXISTS inventory_system') 
cursor.execute('USE inventory_system')

# Make sure the indentation is correct for the 'CREATE TABLE' statement.
cursor.execute('''CREATE TABLE IF NOT EXISTS emp_data (
    empid INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    gender VARCHAR(50),
    dob VARCHAR(30),
    contact VARCHAR(30),
    employement_type VARCHAR(50),
    work_shift VARCHAR(50),
    address VARCHAR(100),
    doj VARCHAR(30),
    salary VARCHAR(50),
    usertype VARCHAR(50),
    password VARCHAR(50),
    education VARCHAR(50)
)''')

return cursor, connection
