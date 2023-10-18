import mysql.connector

#AWS RDS
#Master Username: admin
#Password: admin123
#Database Name: app_database
#Port: 3306


class DataManager:
    def __init__(self):
        self.connection = None
        self.cursor = None

    #return true if successful, false if it failed
    def createUser(self, email, username, password):
        if not self.cursor:
            return False

        try:
            if self.connection.is_connected():
                # SQL query to insert an entry into the "account" table
                insert_account_query = "INSERT INTO account (email, username, password) VALUES (%s, %s, %s)"
                entry_data = (email, username, password)

                # Execute the query
                self.cursor.execute(insert_account_query, entry_data)

                # Commit the changes to the database
                self.connection.commit()

                print("Entry inserted into the 'account' table successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error inserting into 'account' table: {e}")
            return False

    #return true if successful, false if it failed
    def createProfile(self, email, name, pronouns, about, lunchLoc):
        if not self.cursor:
            return False

        try:
            if self.connection.is_connected():
                # SQL query to insert an entry into the "profile" table
                insert_account_query = "INSERT INTO profile (email, name, pronoun, major, about, Lunch_Location) VALUES (%s, %s, %s, %s, %s, %s)"
                entry_data = (email, name, pronouns, about, lunchLoc)

                # Execute the query
                self.cursor.execute(insert_account_query, entry_data)

                # Commit the changes to the database
                self.connection.commit()

                print("Entry inserted into the 'profile' table successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error inserting into 'profile' table: {e}")
            return False
        
    #return true if successful, false if it failed
    def updateProfile(self, email, name, pronouns, about, lunchLoc):
        if not self.cursor:
            return False

        try:
            if self.connection.is_connected():
                update_profile_query = """
                    UPDATE profile
                    SET name = %s, pronoun = %s, major = %s, about = %s, Lunch_Location = %s
                    WHERE email = %s
                    """
                entry_data = (email, name, pronouns, about, lunchLoc)

                # Execute the query
                self.cursor.execute(update_profile_query, entry_data)

                # Commit the changes to the database
                self.connection.commit()

                print("Entry upated in the 'profile' table successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error updating in 'profile' table: {e}")
            return False
        
    #return true if successful, false if it failed
    def createUserAvailability(self, email, day, start_time, end_time):
        if not self.cursor:
            return False

        try:
            if self.connection.is_connected():
                # SQL query to insert an entry into the "account" table
                insert_account_query = "INSERT INTO days (email, day, timeStart, timeEnd) VALUES (%s, %s, %s, %s)"
                entry_data = (email, day, start_time, end_time)

                # Execute the query
                self.cursor.execute(insert_account_query, entry_data)

                # Commit the changes to the database
                self.connection.commit()

                print("Entry inserted into the 'day' table successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error inserting into 'day' table: {e}")
            return False

    #Return a list of emails with the same days and overlapping time availability in the same location
    def getEmailMatches(self, email):
        if self.connection.is_connected():

            # SQL query to find matching emails with the same days, overlapping time availability, and the same location
            find_matching_emails_query = """
            SELECT DISTINCT d2.email
            FROM days d1
            JOIN days d2 ON d1.email <> d2.email
            AND d1.day = d2.day
            AND NOT (d1.timeEnd <= d2.timeStart OR d1.timeStart >= d2.timeEnd)
            JOIN profile p1 ON d1.email = p1.email
            JOIN profile p2 ON d2.email = p2.email
            WHERE d1.email = %s
            AND p1.Lunch_Location = p2.Lunch_Location
            """

            # Execute the query with the provided email
            self.cursor.execute(find_matching_emails_query, (email,))

            # Fetch all the results
            results = self.cursor.fetchall()

            if results:
                return [result[0] for result in results]  # Return a list of matching emails

            else:
                return []  # Return an empty list if no matches found

    #Returns the password from the email provided, returns None if no email found
    def getPasswordFromEmail(self, email):
        try:
            if self.connection.is_connected():
                # Create a cursor object to execute SQL queries
                cursor = self.connection.cursor()

                # SQL query to get the password by email from the "account" table
                select_password_query = "SELECT password FROM account WHERE email = %s"
                
                # Execute the query with the provided email
                cursor.execute(select_password_query, (email,))
                
                # Fetch the result
                result = cursor.fetchone()

                if result:
                    return result[0]  # Return the password

                else:
                    return None  # Return None if no matching entry found

        except mysql.connector.Error as e:
            print(f"Error getting password by email: {e}")



    #Return all profile data from the email if found, return None if email not found
    def getProfileByEmail(self, email):
        if not self.cursor:
            return None

        try:
            if self.connection.is_connected():
                # Create a cursor object to execute SQL queries
                cursor = self.connection.cursor()

                # SQL query to get the profile by email from the "profile" table
                select_profile_data_query = "SELECT * FROM profile WHERE email = %s"
                
                # Execute the query with the provided email
                cursor.execute(select_profile_data_query, (email,))
                
                # Fetch the result
                result = cursor.fetchone()

                if result:
                    return result  # Return the profile data as a tuple
            else:
                return None  # Return None if no matching entry found

        except mysql.connector.Error as e:
            print(f"Error getting profile data by email: {e}")
            return None

    #def updatePronounByEmail(self, email, newPronoun):
        #pass 

    #def updateLocationByEmail(self, email, newPronoun):
        #pass 

    #def updateMajorByEmail(self, email, newPronoun):
        #pass 

    #return true if successful deletion, false otherwise
    def deleteAvailabilityByEmail(self, email, day):
        try:
            if self.connection.is_connected():
                # Create a cursor object to execute SQL queries
                cursor = self.connection.cursor()

                # SQL query to delete a specific day entry for a given email from the "Days" table
                delete_day_entry_query = "DELETE FROM days WHERE email = %s AND day = %s"

                # Execute the query with the provided email and day
                cursor.execute(delete_day_entry_query, (email, day))

                # Commit the changes to the database
                self.connection.commit()
                print(f"Day entry for {email} on {day} deleted successfully")
                return True
        except mysql.connector.Error as e:
            print(f"Error deleting day entry: {e}")
            return False

    def printAllEntries(self):

        if not self.cursor:
            return

        try:
            select_account_query = "SELECT * FROM account"
            self.cursor.execute(select_account_query)
            account_entries = self.cursor.fetchall()

            if account_entries:
                print("Entries in the 'account' table:")
                for entry in account_entries:
                    print(entry)
            else:
                print("No entries found in the 'account' table.")

            # SQL query to select all entries from the "profile" table
            select_profile_query = "SELECT * FROM profile"
            self.cursor.execute(select_profile_query)
            profile_entries = self.cursor.fetchall()

            if profile_entries:
                print("\nEntries in the 'profile' table:")
                for entry in profile_entries:
                    print(entry)
            else:
                print("No entries found in the 'profile' table.")

            # SQL query to select all entries from the "Days" table
            select_days_query = "SELECT * FROM days"
            self.cursor.execute(select_days_query)
            days_entries = self.cursor.fetchall()

            if days_entries:
                print("\nEntries in the 'days' table:")
                for entry in days_entries:
                    print(entry)
            else:
                print("No entries found in the 'days' table.")

        except mysql.connector.Error as e:
            print(f"Error retrieving entries: {e}")

    def printAllTables(self):
        if not self.cursor:
            return
        show_tables_query = "SHOW TABLES"
        self.cursor.execute(show_tables_query)
        # Fetch all the table names
        tables = self.cursor.fetchall()
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])  # The table name is in the first column
        else:
            print("No tables found in the database.")
        return
    
    #Sample data already created do not run
    def createSampleEntries(self):
        from datetime import time

        if not self.cursor:
            return

        try:
            if self.connection.is_connected():

                # Sample data for the "account" table
                account_data = [
                    ('joz@gmu.edu', 'joz_doe', 'password1234'),
                ]

                # Sample data for the "profile" table
                profile_data = [
                    ('joz@gmu.edu', 'Joz Doe', 'He/Him', 'Computer Engineering', 'I like food too', 'Southside'),
                ]

                # Sample data for the "Days" table
                days_data = [
                    ('joz@gmu.edu', 'Monday', time(10, 0), time(15, 0)),
                ]

                # Insert data into the "account" table
                insert_account_query = "INSERT INTO account (email, username, password) VALUES (%s, %s, %s)"
                self.cursor.executemany(insert_account_query, account_data)

                # Insert data into the "profile" table
                insert_profile_query = "INSERT INTO profile (email, name, pronoun, major, about, Lunch_Location) VALUES (%s, %s, %s, %s, %s, %s)"
                self.cursor.executemany(insert_profile_query, profile_data)

                # Insert data into the "Days" table
                insert_days_query = "INSERT INTO days (email, day, timeStart, timeEnd) VALUES (%s, %s, %s, %s)"
                self.cursor.executemany(insert_days_query, days_data)

                # Commit the changes to the database
                self.connection.commit()

                print("Sample data inserted successfully")
        except mysql.connector.Error as e:
            print(f"Error inserting sample data: {e}")
        return

    #Tables already created do not run
    def createTables(self):
        if not self.cursor:
            return

        # SQL query to create the "account" table
        create_table_query = """
        CREATE TABLE account (
            email VARCHAR(255) PRIMARY KEY,
            username VARCHAR(255),
            password VARCHAR(255)
        )
        """

        create_table_query1 = """
        CREATE TABLE profile (
            email VARCHAR(255) PRIMARY KEY,
            name VARCHAR(255),
            pronoun VARCHAR(255),
            major VARCHAR(255),
            about VARCHAR(255),
            Lunch_Location VARCHAR(255),
            FOREIGN KEY (email) REFERENCES account(email)
        )
        """

        create_table_query2 = """
        CREATE TABLE days (
            email VARCHAR(255),
            day VARCHAR(255),
            timeStart TIME,
            timeEnd TIME,
            PRIMARY KEY (email, day),
            FOREIGN KEY (email) REFERENCES profile(email)
        )
        """


        self.cursor.execute(create_table_query)
        self.cursor.execute(create_table_query1)
        self.cursor.execute(create_table_query2)
        return

    def deleteAllTables(self):
        drop_account_table_query = "DROP TABLE IF EXISTS account"
        drop_profile_table_query = "DROP TABLE IF EXISTS profile"
        drop_days_table_query = "DROP TABLE IF EXISTS days"

        # Execute the queries
        try:
            self.cursor.execute(drop_days_table_query)
            self.cursor.execute(drop_profile_table_query)
            self.cursor.execute(drop_account_table_query)      

            # Commit the changes to the database
            self.connection.commit()

            print("All tables dropped successfully")
        
        except mysql.connector.Error as e:
            print(f"Error dropping tables: {e}")



    def connect(self):
    # Connect to the database
        try:
            self.connection = mysql.connector.connect(
                user = "admin",
                password = "admin123",
                host = "appdatabase.czhtd8fz96v6.us-east-1.rds.amazonaws.com",
                database = "app_database",

            )
            
            if self.connection.is_connected():
                print("Connected to the database")

                # Create a cursor object to execute SQL queries
                self.cursor = self.connection.cursor()



        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

        finally:
            # Close the connection in the finally block to ensure it's always closed
            if 'connection' in locals() and self.connection.is_connected():
                self.connection.close()
                print("Connection closed")




