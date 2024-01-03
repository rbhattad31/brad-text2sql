# main_app.py

import streamlit as st
import sqlite3
import pandas as pd
import sql_db
from prompts.prompts import SYSTEM_MESSAGE
from azure_openai import get_completion_from_messages
import json

def query_database(query):
    """ Run SQL query and return results in a dataframe """
    return pd.read_sql_query(query, conn)

# Create or connect to SQLite database
conn = sql_db.create_connection()

# Schema Representation for finances table
schemas = sql_db.get_schema_representation()
print(schemas['company'])

# Format the system message with the schema
formatted_system_message = SYSTEM_MESSAGE.format(schema=schemas)

# Generate the SQL query from the user message
user_message = "Show me companies in Mumbai"

# Use GPT-4 to generate the SQL query
response = get_completion_from_messages(formatted_system_message, user_message)
print(response)
json_response = json.loads(response)
query = json_response['query']
print(query)

# Run the SQL query
sql_results = query_database(query)
print(sql_results)