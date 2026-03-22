import sys
import os
import numpy as np
import pandas as pd

TARGET_COLUMN="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFICAT_DIR:str="Artifacts"
FILE_NAME:str="phisingData.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"



"""
Data ingestion related to constant start with Data_ingestion var Name
"""

DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="VidyaAI"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RADIATION:float=0.2


