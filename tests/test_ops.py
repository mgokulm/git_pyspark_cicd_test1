from pathlib import Path
import pytest
import os
import sys
from jobs.ops import *
from jobs.gps import *
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('gps').getOrCreate()



def test_add():
    assert add(2,3) == 5

def test_subtract():
    assert subtract(2,3) == -2

def test_multiply():
    assert multiply(2,3) == 6

def test_divide():
    assert divide(12,3) == 4

def test_with_status():
    source_data = [("paula", "white", "paula.white@example.com"),
                   ("john", "blue", "john.blue@example")]

    source_df = spark.createDataFrame(source_data, ["first_name", "last_name", "email"])
    actual_df = with_status(source_df)

    expected_data = [("paula", "white", "paula.white@example.com", "checked"),
                   ("john", "blue", "john.blue@example", "checked")]

    expected_df = spark.createDataFrame(expected_data, ["first_name", "last_name", "email", "status"])

    assert (expected_df.collect() == actual_df.collect())
