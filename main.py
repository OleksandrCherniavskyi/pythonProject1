import pandas as pd
import requests
from sqlalchemy import create_engine
import sqlite3
import datetime
import psycopg2


engine = create_engine('postgresql://postgres:justjoin123@justjoin-1.cdg5aro86v8p.eu-north-1.rds.amazonaws.com:5432/just_init')

def check_if_valid_data(df: pd.DataFrame) -> bool:
    # Check if dataframe is empty
    if df.empty:
        print("No new offers")
        return False

        # Primary Key Check
    if pd.Series(df['id']).is_unique:
        pass
    else:
        raise Exception("Primary Key check is violated")
    return True


# if __name__ == '__main__':

def run_justjoin_etl():

    response = requests.get('https://justjoin.it/api/offers')
    data = response.json()
    data_in = []
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    yesterday_formatted = yesterday.strftime('%Y-%m-%d')

    for offer in data:
        if offer["published_at"][:10] == yesterday_formatted:
            if offer["display_offer"] == True:
                data_in.append(offer)

    # with open('offers.json', 'w') as f:
    #    json.dump(data_in, f)

    # with open('offers.json', 'r') as f:
    #    data_in = json.loads(f.read())

    def employment():
        type = []
        from_salary = []
        to_salary = []
        currency = []
        id = []
        for offer in data_in:
            o_id = offer['id']
            employment_types = offer["employment_types"]
            for employment_type in employment_types:
                o_type = employment_type["type"]
                type.append(o_type)
                salary = employment_type["salary"]
                if salary is not None:
                    o_from_salary = int(salary["from"])
                    o_to_salary = int(salary["to"])
                    o_currency = salary["currency"]
                else:
                    o_from_salary = None
                    o_to_salary = None
                    o_currency = None
                from_salary.append(o_from_salary)
                to_salary.append(o_to_salary)
                currency.append(o_currency)
                id.append(o_id)

        employment_types_dict = {
            'id': id,
            'type': type,
            'from_salary': from_salary,
            'to_salary': to_salary,
            'currency': currency
        }
        employment_types_df = pd.DataFrame(employment_types_dict, columns=[
            'id', 'type', 'from_salary', 'to_salary', 'currency'
        ])
        employment_types_df.fillna(0, inplace=True)
        return employment_types_df

    def skills():
        name = []
        level = []
        id = []
        for offer in data_in:

            o_id = offer['id']
            skills = offer["skills"]
            for skill in skills:
                o_name = skill["name"]
                o_level = int(skill["level"])
                name.append(o_name)
                level.append(o_level)
                id.append(o_id)
        skills_dict = {
            'id': id,
            'name': name,
            'level': level
        }
        skills_df = pd.DataFrame(skills_dict, columns=[
            'id', 'name', 'level'
        ])
        return skills_df

    def offers():
        company_name = []
        id = []
        title = []
        city = []
        country_code = []
        marker_icon = []
        experience_level = []
        workplace_type = []
        published_at = []
        remote = []
        for offer in data_in:

            o_id = offer['id']
            id.append(o_id)
            o_title = offer['title']
            o_title = o_title.replace(' - Remote ', '')
            o_title = o_title.replace('Remote', '')
            o_title = o_title.replace(' (REMOTE)', '')
            o_title = o_title.replace(' (Remote)', '')
            o_title = o_title.replace('Junior ', '')
            o_title = o_title.replace('Junior/ ', '')
            o_title = o_title.replace('(Junior) ', '')
            o_title = o_title.replace(' (Junior)', '')
            o_title = o_title.replace('Mid ', '')
            o_title = o_title.replace('Mid-', '')
            o_title = o_title.replace('Mid /', '')
            o_title = o_title.replace('Mid / ', '')
            o_title = o_title.replace('Mid/', '')
            o_title = o_title.replace('Middle ', '')
            o_title = o_title.replace('Middle/', '')
            o_title = o_title.replace('Senior ', '')
            o_title = o_title.replace('Senior / ', '')
            o_title = o_title.replace('Senior/ ', '')
            o_title = o_title.replace('(Senior) ', '')
            o_title = o_title.replace(' (Senior)', '')
            o_title = o_title.replace('Expert ', '')
            o_title = o_title.replace('Lead ', '')
            o_title = o_title.replace('Lead, ', '')
            o_title = o_title.replace(' Lead', '')
            o_title = o_title.replace(' (Automotive)', '')
            o_title = o_title.replace(' (Azure)', '')
            o_title = o_title.replace(' (GCP)', '')
            o_title = o_title.replace(' (m/f/d)', '')
            o_title = o_title.replace('👉 ', '')
            o_title = o_title.replace('👉', '')
            o_title = o_title.replace(' (Mid / Senior)', '')
            title.append(o_title)
            o_city = offer["city"]
            city.append(o_city)
            o_company_name = offer["company_name"]
            company_name.append(o_company_name)
            o_country_code = offer["country_code"]
            country_code.append(o_country_code)
            o_marker_icon = offer["marker_icon"]
            marker_icon.append(o_marker_icon)
            o_experience_level = offer["experience_level"]
            experience_level.append(o_experience_level)
            o_workplace_type = offer["workplace_type"]
            workplace_type.append(o_workplace_type)
            o_published_at = offer["published_at"][:10]
            published_at.append(o_published_at)
            o_remote = offer["remote"]
            remote.append(o_remote)

        offers_dict = {
            'id': id,
            'published_at': published_at,
            'title': title,
            'marker_icon': marker_icon,
            'experience_level': experience_level,
            'city': city,
            'country_code': country_code,
            'remote': remote,
            'workplace_type': workplace_type,
            'company_name': company_name
        }
        offers_df = pd.DataFrame(offers_dict, columns=[
            'id', 'published_at', 'title', 'marker_icon', 'experience_level',
            'city', 'country_code', 'remote', 'workplace_type', 'company_name'
        ])
        return offers_df

    def brands():
        company_name = []
        company_url = []
        company_size = []
        for offer in data_in:
            o_company_name = offer["company_name"]
            company_name.append(o_company_name)
            o_company_url = offer["company_url"]
            company_url.append(o_company_url)
            o_company_size = offer["company_size"]
            if o_company_size is not None:
                o_company_size = o_company_size.replace(' ', '')
                o_company_size = o_company_size.replace('.', '')
                o_company_size = o_company_size.replace(',', '')
                o_company_size = o_company_size.replace('+', '')
                o_company_size = o_company_size.replace('>', '')
                o_company_size = o_company_size.replace('<', '')
                if o_company_size == "-":
                    o_company_size = None
                else:
                    if '-' in o_company_size:
                        a, b = o_company_size.split("-")
                        o_company_size = int(b)
            else:
                o_company_size = None
            company_size.append(o_company_size)

        brands_dict = {
            'company_name': company_name,
            'company_size': company_size,
            'company_url': company_url
        }
        brands_df = pd.DataFrame(brands_dict, columns=[
            'company_name', 'company_size', 'company_url'
        ])
        brands_df.fillna(0, inplace=True)
        brands_df = brands_df.drop_duplicates('company_name')
        return brands_df

    def location():
        id = []
        office = []
        slug = []
        company_name = []
        for offer in data_in:
            multilocation = offer["multilocation"]
            for location in multilocation:
                o_office = location["city"]
                o_slug = location["slug"]
                slug.append(o_slug)
                office.append(o_office)
                o_id = offer['id']
                id.append(o_id)
                o_company_name = offer["company_name"]
                company_name.append(o_company_name)

        brands_office_dict = {
            'company_name': company_name,
            'slug': slug,
            'office': office,
            'id': id
        }
        brands_office_df = pd.DataFrame(brands_office_dict, columns=[
            'company_name', 'slug', 'office', 'id'
        ])
        return brands_office_df

    # Validate
    if check_if_valid_data(offers()):
        print("Data valid, proceed to Load stage Offers")
    ## Load
    #engine = create_engine('sqlite:///my_page/justjoin.sqlite3', echo=True)
    #conn = sqlite3.connect('my_page/justjoin.sqlite3')
    #cursor = conn.cursor()

    # Connect to PostgreSQL
    conn = psycopg2.connect(
        dbname='just_init',
        user='postgres',
        password='justjoin123',
        host='justjoin-1.cdg5aro86v8p.eu-north-1.rds.amazonaws.com',
        port='5432'
    )
    conn.autocommit = True
    # Create a cursor
    cursor = conn.cursor()
    brands_table_query = """
    CREATE TABLE IF NOT EXISTS brands (
        company_name VARCHAR(250) PRIMARY KEY,
        company_size INTEGER,
        company_url VARCHAR(500)
    );
    """
    offers_table_query = """
    CREATE TABLE IF NOT EXISTS offers (
        id VARCHAR(300) PRIMARY KEY,
        published_at DATE,
        title VARCHAR(100),
        marker_icon VARCHAR(30),
        experience_level VARCHAR(30),
        city VARCHAR(100),
        country_code VARCHAR(10),
        remote VARCHAR(50),
        workplace_type VARCHAR(50),
        company_name VARCHAR(250),
        FOREIGN KEY (company_name) REFERENCES brands(company_name)
    );
    """

    brands_office_table_query = """
    CREATE TABLE IF NOT EXISTS brands_office (
        slug VARCHAR(300) PRIMARY KEY,
        company_name VARCHAR(250),
        office VARCHAR(100),
        id VARCHAR(300),
        FOREIGN KEY (id) REFERENCES offers(id),
        FOREIGN KEY (company_name) REFERENCES brands(company_name)
    );
    """
    skills_table_query = """
    CREATE TABLE IF NOT EXISTS skills (
        id VARCHAR(300),
        name VARCHAR(150),
        level INT,
        FOREIGN KEY (id) REFERENCES offers(id)
    );
    """
    employment_types_query = """
    CREATE TABLE IF NOT EXISTS employment_types (
        id VARCHAR(300),
        type VARCHAR(100),
        from_salary INT,
        to_salary INT,
        currency VARCHAR(10),
        FOREIGN KEY (id) REFERENCES offers(id)
    );
    """
    exiting_offers_query = "SELECT * FROM offers;"
    exiting_brands_query = "SELECT * FROM brands;"
    exiting_office_query = "SELECT * FROM brands_office;"
#    offers_table_query = """
#    CREATE TABLE IF NOT EXISTS offers(
#        id VARCHAR(300) PRIMARY KEY,
#        published_at DATE,
#        title VARCHAR(100) ,
#        marker_icon VARCHAR(30),
#        experience_level VARCHAR(30),
#        city VARCHAR(100),
#        country_code VARCHAR(10),
#        remote VARCHAR(50),
#        workplace_type VARCHAR(50),
#        company_name VARCHAR(250)
#    );
#    """
#
#    brands_table_query = """
#    CREATE TABLE IF NOT EXISTS brands(
#        company_name VARCHAR(250) PRIMARY KEY,
#        company_size INT,
#        company_url VARCHAR(500)
#    );
#    """
#
#    brands_office_table_query = """
#        CREATE TABLE IF NOT EXISTS brands_office(
#            slug VARCHAR(300) PRIMARY KEY,
#            company_name VARCHAR(250),
#            office VARCHAR(100),
#            id VARCHAR(300)
#    );
#    """
#
#    skills_table_query = """
#        CREATE TABLE IF NOT EXISTS skills(
#            id VARCHAR(300),
#            name VARCHAR(50),
#            level INT,
#            FOREIGN KEY (id) REFERENCES offers(id)
#    );
#    """
#
#    employment_types_query = """
#        CREATE TABLE IF NOT EXISTS employment_types(
#            id VARCHAR(300),
#            type VARCHAR(100),
#            from_salary INT,
#            to_salary INT,
#            currency VARCHAR(10),
#            FOREIGN KEY (id) REFERENCES offers(id)
#    );
#    """
#
#    # Verificate primary key
#    exiting_offers_query = "SELECT * FROM offers"
#    exiting_brands_query = "SELECT * FROM brands"
#    exiting_office_query = "SELECT * FROM brands_office"




    cursor.execute(offers_table_query)
    try:
        exiting_offers = pd.read_sql_query(exiting_offers_query, engine)
        new_offers = offers()[~offers()['id'].isin(exiting_offers['id'])]
        new_offers.to_sql("offers", engine, if_exists='append', index=False) #engine,
    except:
        print("Data already exists in the table offers")
    cursor.execute(brands_table_query)

    try:
        exiting_brands = pd.read_sql_query(exiting_brands_query, engine)
        new_brands = brands()[~brands()['company_name'].isin(exiting_brands['company_name'])]
        new_brands.to_sql("brands", engine, index=False, if_exists='append') #engine,
    except:
        print("Data already exists in the table brands")
    cursor.execute(brands_office_table_query)
    try:
        exiting_office = pd.read_sql_query(exiting_office_query, engine)
        new_office = location()[~location()['slug'].isin(exiting_office['slug'])]
        new_office.to_sql("brands_office", engine, index=False, if_exists='append') #engine,
    except:
        print("Data already exists in the table brands_office")
    cursor.execute(skills_table_query)
    try:
        skills().to_sql("skills", engine, index=False, if_exists='append') #engine,
    except:
        print("Data already exists in the table skills")
    cursor.execute(employment_types_query)
    try:
        employment().to_sql('employment_types', engine, index=False, if_exists='append') # engine,
    except:
        print("Data already exists in the table employment_types")


    conn.close()
    print("Close database successfully")
run_justjoin_etl()
