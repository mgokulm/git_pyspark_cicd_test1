import pyspark.sql.functions as F
from pyspark.sql import SparkSession

def with_status(df):
    return df.withColumn("status", F.lit("checked"))


# if __name__ == '__main__':
#
#     print('gkl in pyspark test program')
#     spark = SparkSession.builder.appName('gps').getOrCreate()
#     df = (spark.createDataFrame(
#       schema = ["first_name", "last_name", "email"],
#       data = [("paula", "white", "paula.white@example.com"),("john", "baer", "john.baer@example.com")]
#     ))
#
#     print(df.show())
#     new_df = with_status(df)
#     print(new_df.show())