import datetime
import pathlib
import pandas
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        return conn
    except Error as e:
        print(e)
    return conn


def execute_sql(conn, sql, data):
    try:
        c = conn.cursor()

        if data is None:
            c.execute(sql)
        else:
            c.executemany(sql, data)

        conn.commit()
    except Error as e:
        print(e)
    finally:
        c.close()


def get_index(df, col, value):
    for r, row in df.iterrows():
        if row[col] == value:
            return r+1


def main():
    database_file = r'\\sdvfs1\home1\jthomas\Eigene Dateien\Python Scripts\PANTER\db.sqlite3'
    excel_file = r"C:\Users\jthomas\Downloads\Preisdaten_Beispieltabelle.xlsx"

    sql_create_currency_table = """ CREATE TABLE IF NOT EXISTS currency (
                                        id integer PRIMARY KEY,
                                        code char(3) NOT NULL,
                                        name varchar(100) NOT NULL
                                    ); """

    sql_create_feescope_table = """ CREATE TABLE IF NOT EXISTS fee_scope (
                                        id integer PRIMARY KEY,
                                        name varchar(50) NOT NULL
                                    ); """

    sql_create_limittype_table = """ CREATE TABLE IF NOT EXISTS limit_type (
                                        id integer PRIMARY KEY,
                                        name varchar(50) NOT NULL
                                    ); """

    sql_create_publisher_table = """ CREATE TABLE IF NOT EXISTS publisher (
                                        id integer PRIMARY KEY,
                                        imprint varchar(100) NOT NULL,
                                        main_publisher varchar(50)
                                    ); """

    sql_create_journal_table = """ CREATE TABLE IF NOT EXISTS journal (
                                        id integer PRIMARY KEY,
                                        name varchar(50) NOT NULL,
                                        pissn char(9),
                                        eissn char(9),
                                        publisher integer,
                                        remark varchar(1000),
                                        date_created datetime NOT NULL,
                                        FOREIGN KEY (publisher) REFERENCES publisher (id)
                                    ); """

    sql_create_fee_table = """ CREATE TABLE IF NOT EXISTS fee (
                                        id integer PRIMARY KEY,
                                        journal integer NOT NULL,
                                        article_type varchar(50),
                                        document_type varchar(10),
                                        membership varchar(10),
                                        foreign_author boolean,
                                        fee_scope integer,
                                        fee_type varchar(20),
                                        fee decimal(12,2) NOT NULL,
                                        factor integer,
                                        upper_limit integer,
                                        limit_type integer,
                                        currency integer NOT NULL,
                                        valid_from date,
                                        remark varchar(1000),
                                        date_created datetime NOT NULL,
                                        FOREIGN KEY (journal) REFERENCES journal (id),
                                        FOREIGN KEY (fee_scope) REFERENCES fee_scope (id),
                                        FOREIGN KEY (limit_type) REFERENCES limit_type (id),
                                        FOREIGN KEY (currency) REFERENCES currency (id)
                                    ); """

    sql_create_discountlevel_table = """ CREATE TABLE IF NOT EXISTS discount_level (
                                        id integer PRIMARY KEY,
                                        name varchar(50) NOT NULL
                                    ); """

    sql_create_discount_table = """ CREATE TABLE IF NOT EXISTS discount (
                                        id integer PRIMARY KEY,
                                        journal integer NOT NULL,
                                        discount_level integer NOT NULL,
                                        discount decimal(5,2) NOT NULL,
                                        remark varchar(1000),
                                        FOREIGN KEY (journal) REFERENCES journal (id),
                                        FOREIGN KEY (discount_level) REFERENCES discount_level (id)
                                    ); """

    database_path = pathlib.Path(database_file)

    # remove old database file, if it exists
    #if database_path.is_file():
    #    database_path.unlink()

    # create a database connection
    conn = create_connection(database_file)

    if conn is None:
        print("Error! cannot create the database connection.")
        exit(1)

    try:
        # create tables
        #execute_sql(conn, sql_create_currency_table, None)
        #execute_sql(conn, sql_create_feescope_table, None)
        #execute_sql(conn, sql_create_limittype_table, None)
        #execute_sql(conn, sql_create_publisher_table, None)
        #execute_sql(conn, sql_create_journal_table, None)
        #execute_sql(conn, sql_create_fee_table, None)
        #execute_sql(conn, sql_create_discountlevel_table, None)
        #execute_sql(conn, sql_create_discount_table, None)

        # delete Table data
        execute_sql(conn, 'DELETE FROM fee', None)
        execute_sql(conn, 'DELETE FROM discount', None)
        execute_sql(conn, 'DELETE FROM journal_to_publisher', None)
        execute_sql(conn, 'DELETE FROM journal_to_professional_society', None)
        execute_sql(conn, 'DELETE FROM journal_to_subject_area', None)
        execute_sql(conn, 'DELETE FROM journal_to_license_type', None)
        execute_sql(conn, 'DELETE FROM contract', None)
        execute_sql(conn, 'DELETE FROM journal', None)
        execute_sql(conn, 'DELETE FROM institution', None)
        execute_sql(conn, 'DELETE FROM publisher', None)
        execute_sql(conn, 'DELETE FROM professional_society', None)
        execute_sql(conn, 'DELETE FROM currency', None)
        execute_sql(conn, 'DELETE FROM country', None)
        execute_sql(conn, 'DELETE FROM fee_scope', None)
        execute_sql(conn, 'DELETE FROM limit_type', None)
        execute_sql(conn, 'DELETE FROM article_type', None)
        execute_sql(conn, 'DELETE FROM document_type', None)
        execute_sql(conn, 'DELETE FROM discount_level', None)
        execute_sql(conn, 'DELETE FROM subject_area', None)
        execute_sql(conn, 'DELETE FROM license_type', None)
                
        # read Excel file
        dict = pandas.read_excel(excel_file, sheet_name=None)

        # fill tables
        for table in dict:
            if table == 'Sheet1':
                continue
            
            sql = f'INSERT INTO {table} (id'
            
            if '_to_' not in table:
                sql += ',date_created,created_by'
            
            for col in dict[table].columns:
                sql += f',{col}'

            sql += ') VALUES (?'
            
            if '_to_' not in table:
                sql += ',?,?'

            for col in dict[table].columns:
                sql += ',?'

            sql += ');'
            
            data = []

            for r, row in dict[table].iterrows():
                values = [r+1]
                
                if '_to_' not in table:
                    values += [datetime.datetime.now(), 1]

                for col in dict[table].columns:
                    if table == 'journal' and col == 'country':
                        values.append(get_index(dict['country'], 'name', row[col]))
                    elif table == 'journal_to_publisher' and col == 'journal':
                        values.append(get_index(dict['journal'], 'name', row[col]))
                    elif table == 'journal_to_publisher' and col == 'publisher':
                        values.append(get_index(dict['publisher'], 'imprint', row[col]))
                    elif table == 'journal_to_subject_area' and col == 'journal':
                        values.append(get_index(dict['journal'], 'name', row[col]))
                    elif table == 'journal_to_subject_area' and col == 'subject_area':
                        values.append(get_index(dict['subject_area'], 'name', row[col]))
                    elif table == 'journal_to_professional_society' and col == 'journal':
                        values.append(get_index(dict['journal'], 'name', row[col]))
                    elif table == 'journal_to_professional_society' and col == 'professional_society':
                        values.append(get_index(dict['professional_society'], 'name', row[col]))
                    elif table == 'journal_to_license_type' and col == 'journal':
                        values.append(get_index(dict['journal'], 'name', row[col]))
                    elif table == 'journal_to_license_type' and col == 'license_type':
                        values.append(get_index(dict['license_type'], 'name', row[col]))
                    elif table == 'fee' and col == 'journal':
                        values.append(get_index(dict['journal'], 'name', row[col]))
                    elif table == 'fee' and col == 'article_type':
                        values.append(get_index(dict['article_type'], 'name', row[col]))
                    elif table == 'fee' and col == 'document_type':
                        values.append(get_index(dict['document_type'], 'name', row[col]))
                    elif table == 'fee' and col == 'license_type':
                        values.append(get_index(dict['license_type'], 'name', row[col]))
                    elif table == 'fee' and col == 'membership':
                        values.append(1 if row[col] == "yes" else 0 if row[col] == "no" else None)
                    elif table == 'fee' and col == 'with_contract':
                        values.append(1 if row[col] == "yes" else 0 if row[col] == "no" else None)
                    elif table == 'fee' and col == 'contract':
                        values.append(get_index(dict['contract'], 'number', row[col]))
                    elif table == 'fee' and col == 'foreign_author':
                        values.append(1 if row[col] == "yes" else 0 if row[col] == "no" else None)
                    elif table == 'fee' and col == 'fee_scope':
                        values.append(get_index(dict['fee_scope'], 'name', row[col]))
                    elif table == 'fee' and col == 'limit_type':
                        values.append(get_index(dict['limit_type'], 'name', row[col]))
                    elif table == 'fee' and col == 'currency':
                        values.append(get_index(dict['currency'], 'code', row[col]))
                    elif table == 'fee' and col == 'valid_from':
                        values.append(None if pandas.isnull(row[col]) else row[col].date())
                    elif table == 'discount' and col == 'journal':
                        values.append(get_index(dict['journal'], 'name', row[col]))
                    elif table == 'discount' and col == 'discount_level':
                        values.append(get_index(dict['discount_level'], 'name', row[col]))
                    else:
                        values.append(row[col])

                data.append(tuple(values))

            execute_sql(conn, sql, data)

    except Error as e:
        print(e)
    finally:
        # close database connection
        conn.close()

if __name__ == "__main__":
    main()