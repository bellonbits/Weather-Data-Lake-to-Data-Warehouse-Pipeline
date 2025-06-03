# scripts/transform_weather.py
import findspark
findspark.init()  # This should come before importing pyspark

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime

spark = SparkSession.builder \
    .appName("WeatherClean") \
    .config("spark.sql.adaptive.enabled", "true") \
    .config("spark.sql.adaptive.coalescePartitions.enabled", "true") \
    .getOrCreate()

df = spark.read.json("*.json")

df_clean = df.select(
    from_unixtime(col("dt")).alias("timestamp"),
    col("name").alias("city"),
    col("main.temp").alias("temperature"),
    col("main.humidity").alias("humidity"),
    col("weather")[0]["description"].alias("description")
)

df_clean.write.csv("weather.csv", header=True, mode="overwrite")

spark.stop()