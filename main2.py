import json
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import pandas as pd
import requests
from sqlalchemy import create_engine
import sqlite3
import datetime
import psycopg2


engine = create_engine('postgresql://tqupkkom:ivFQarmVJxpKnp4LYCCZ5FKvU0kGxmV5@balarama.db.elephantsql.com/tqupkkom')
# Create a connection to the database
conn = engine.connect()
conn.autocommit = True
# Create a cursor object
connection = engine.raw_connection()
cursor = connection.cursor()

# QUERY
create_offers_table = """
    CREATE TABLE IF NOT EXISTS offers (
        slug VARCHAR(100) PRIMARY KEY,
        title VARCHAR(200),
        workplaceType VARCHAR(10),
        experienceLevel VARCHAR(10),
        workingTime VARCHAR(15),
        categoryId INTEGER,
        city VARCHAR(50),
        companyName VARCHAR(150),
        publishedAt TIMESTAMP
);
"""
cursor.execute(create_offers_table)
create_skills_table = """
CREATE TABLE IF NOT EXISTS skills (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(100) REFERENCES offers(slug),
    skill VARCHAR(50)
);
"""
cursor.execute(create_skills_table)
create_type_table = """
CREATE TABLE IF NOT EXISTS employmentTypes (
    id SERIAL PRIMARY KEY,
    to_ INTEGER,
    from_ INTEGER,
    type VARCHAR(10),
    currency VARCHAR(3),
    slug VARCHAR(100) REFERENCES offers(slug)
);
"""
cursor.execute(create_type_table)
create_multilocation_table = """
CREATE TABLE IF NOT EXISTS multilocation (
    id SERIAL PRIMARY KEY,
    city VARCHAR(40),
    location_slug VARCHAR(255),
    slug VARCHAR(100) REFERENCES offers(slug)
);
"""
cursor.execute(create_multilocation_table)
create_offers_life_table = """
CREATE TABLE IF NOT EXISTS offers_life (
    slug VARCHAR(100) REFERENCES offers(slug),
    publishedAt TIMESTAMP
);
"""
cursor.execute(create_offers_life_table)
exiting_offers_query = "SELECT * FROM offers;"
exiting_brands_query = "SELECT * FROM brands;"
exiting_office_query = "SELECT * FROM brands_office;"



#url = 'https://justjoin.it/v2/user-panel/offers?'
#r = requests.get(url)
#print(f'r_status: {r.status_code}')
#
#webpage = bs(r.text, 'html.parser')
#script_tag = webpage.find('script', id='__NEXT_DATA__')
#
#
#script_content = script_tag.contents[0]
#
#data = json.loads(script_content)
#json_filename = 'extracted_data.json'

#
#
#queries = data['props']['pageProps']["dehydratedState"]["queries"]#["state"]["data"]["pages"[0]]["data"]
#pages = queries[0]['state']['data']['pages']
#data_in_json = pages[0]['data']
#
#print(data_in_json)
#
## Save the data as JSON in a file
#with open(json_filename, 'w', encoding='utf-8') as json_file:
#    json.dump(data_in_json, json_file, ensure_ascii=False, indent=4)
#
#print(f'Data saved to {json_filename}')


# Specify the path to the JSON file
json_filename = 'extracted_data.json'
# Open the JSON file for reading
with open(json_filename, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Now, the data from the JSON file is stored in the 'data' variable
# You can access and manipulate the data as needed
#print(data)


slug = []
title = []
workplaceType = []
experienceLevel = []
workingTime = []
categoryId = []
city = []
companyName = []
publishedAt = []
for item in data:
    # table offers
    o_slug = item.get("slug")
    slug.append(o_slug)
    o_title = item.get("title")
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

    o_workplaceType = item.get("workplaceType")
    workplaceType.append(o_workplaceType)

    o_experienceLevel = item.get("experienceLevel")
    experienceLevel.append(o_experienceLevel)

    o_workingTime = item.get("workingTime")
    workingTime.append(o_workingTime)

    o_categoryId = item.get("categoryId")
    categoryId.append(o_categoryId)

    o_city = str(item["city"])
    city.append(item["city"])

    o_companyName = item.get("companyName")
    companyName.append(companyName)

    o_publishedAt = item["publishedAt"][:10]
    publishedAt.append(publishedAt)

    offers_dict = {
        'slug': slug,
        'title': title,
        'workplaceType': workplaceType,
        'experienceLevel': experienceLevel,
        'workingTime': workingTime,
        'categoryId': categoryId,
        'city': city,
        'companyName': companyName,
        'publishedAt': publishedAt
    }

    offers_df = pd.DataFrame(offers_dict, columns=['slug', 'title', 'workplaceType', 'experienceLevel', 'workingTime',
                                                    'categoryId', 'city', 'companyName', 'publishedAt'])


    try:
        exiting_offers = pd.read_sql_query(exiting_offers_query, engine)
        new_offers = offers_df[~offers_df()['slug'].isin(exiting_offers['slug'])]
        new_offers.to_sql("offers", engine, if_exists='append', index=False)  # engine,
    except:
        print("Data already exists in the table offers")


    #table requiredSkills
    #- slug from primary key
    skills = item["requiredSkills"]
    for skill in skills:
        skill



    #table employmentTypes
    employmentTypes = item["employmentTypes"]
    for types in employmentTypes:
        to = types["to"]
        from_ = types["from"]
        type = types["type"]
        currency = types["currency"]
        #- slug from primary key


    #table multilocation
    multilocation = item["multilocation"]
    for location in multilocation:
        m_city = location["city"]
        location_slug = location["slug"]
        #- slug from primary key

    #table offers_life
    #- slug
    #- publishedAt