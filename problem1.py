import sqlite3
import conf
import tools


def update_analytics_table(db: str, query: str):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    print("Connection is created")

    # Remove outdated table if exists (in SQLite there is no option for updating data as an MView)
    cursor.execute(conf.REMOVE_TABLE_QUERY)

    # Create new table
    cursor.execute(conf.CREATE_TABLE_QUERY)
    print("Empty table is created")

    # Transform data
    cursor.execute(query)
    result = cursor.fetchall()
    transformed_data = tools.calculate_favourite_food(result)
    print("Data is prepared")

    # Insert data to the table
    cursor.executemany(conf.INSERT_QUERY, transformed_data)

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

    return print('TABLE analytics succesfully updated')


if __name__ == "__main__":
    update_analytics_table(conf.DB_NAME, conf.TRANSFORM_QUERY)
