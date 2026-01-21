#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
# !uv add tqdm
#!uv add sqlalchemy psycopg2-binary


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
] 


# print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))

def run():
        year = 2021
        month = 1

        pg_user = 'root'
        pg_password = 'root'
        pg_host = 'localhost'
        pg_db = 'ny_taxi'
        pg_port = 5432
        
        chunksize=100000
        target_table = 'yellow_taxi_data'

        # Read a sample of the data
        prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
        url = f'{prefix}/yellow_tripdata_{year:04d}-{month:02d}.csv.gz'

        engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}')

        print(f"Downloading from: {url}")
        print("Testing database connection...")
        try:
            with engine.connect() as conn:
                print("✓ Database connection successful!")
        except Exception as e:
            print(f"✗ Database connection failed: {e}")
            return
        
        df_iter = pd.read_csv(
            url,
            dtype=dtype,
            parse_dates=parse_dates,
            iterator=True,
            chunksize=chunksize
        )

        print("Starting data ingestion...")
        first = True
        for df_chunk in tqdm(df_iter):
            if first:
                print(f"Creating table with {len(df_chunk)} columns")
                df_chunk.head(n=0).to_sql(
                    name=target_table, 
                    con=engine,
                    if_exists='replace'
                )
                first = False
                print("Table created")

            df_chunk.to_sql(
                name=target_table, 
                con=engine,
                if_exists='append'
            )
            print(f"Inserted: {len(df_chunk)} rows")
if __name__ == '__main__':
    run()