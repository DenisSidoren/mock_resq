import sqlite3
import conf


def update_presentation_table(db: str):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    print("Connection is created")

    # Remove outdated table if exists (in SQLite there is no option for updating data as an MView)
    cursor.execute(conf.REMOVE_TABLE_QUERY)

    cursor.execute(conf.CREATE_TABLE_QUERY)
    print("Empty table is created")

    cursor.execute(conf.TRANSFORM_QUERY)
    transformed_data = cursor.fetchall()
    print("Data is prepared")

    # Insert data to the table
    cursor.executemany(conf.INSERT_QUERY, transformed_data)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

    print('TABLE presentation succesfully updated')


if __name__ == "__main__":
    update_presentation_table(conf.DB_NAME)
