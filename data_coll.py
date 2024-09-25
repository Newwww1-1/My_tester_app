import mysql.connector

# Establish connection to MySQL database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Huzaifa12345",
        database="mydb"
    )

# Function to insert values into the table
def check_cnic_exists(p_cnic):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        # Query to check if the CNIC exists
        query = "SELECT COUNT(*) FROM pts WHERE p_cnic = %s"
        cursor.execute(query, (p_cnic,))
        result = cursor.fetchone()

        # Check if CNIC exists
        if result[0] > 0:
            return 1  # CNIC exists
        else:
            return 0  # CNIC does not exist

    except Exception as e:
        print(f"An error occurred: {e}")
        return 1  # Consider CNIC exists in case of error
    finally:
        if connection:
            cursor.close()
            connection.close()



def insert_data(p_cnic, p_name, cell_, age_g, email, g_email, institute_name, c_name, t_name):
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = """
        INSERT INTO pts 
        (status, p_cnic, p_name, cell_, age_g, email, g_email, institute_name, c_name, t_name) 
        VALUES ('No Status', %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (p_cnic, p_name, cell_, age_g, email, g_email, institute_name, c_name, t_name)
        cursor.execute(query, values)
        connection.commit()

        print("Data inserted successfully.")

    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


def insert_data_if_cnic_not_exists(p_cnic, p_name, cell_, age_g, email, g_email,
                                   institute_name, c_name, t_name):
    if check_cnic_exists(p_cnic) == 0:
        # If CNIC does not exist, call insert_data function
        insert_data(p_cnic, p_name, cell_, age_g, email, g_email,
                    institute_name, c_name, t_name)



# Function to check for rows based on the last 4 digits of CNIC
def get_row_by_cnic_last_four(last_four_digits):
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)

        query = """
        SELECT * FROM pts 
        WHERE RIGHT(p_cnic, 4) = %s
        """
        cursor.execute(query, (last_four_digits,))
        result = cursor.fetchall()

        if result:
            return result
        else:
            return "No records found with these last four CNIC digits."

    except mysql.connector.Error as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

