from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, greatest, when, array
from pyspark.sql.functions import levenshtein

# Initialize Spark session
spark = SparkSession.builder.appName("FuzzyMatching").getOrCreate()

# Sample DataFrame
data = [
    ("apple", "apple pie", "banana", "grapefruit"),
    ("banana", "banana split", "apple", "grape"),
    ("grape", "orange", "peach", "apple"),
    ("pear", "pineapple", "strawberry", "blueberry")
]

# Creating a DataFrame with one column to match and three other columns
df = spark.createDataFrame(data, ["col1", "col2", "col3", "col4"])
df.show(truncate=False)

# Calculate Levenshtein distances for fuzzy matching
df = df.withColumn("lev_col2", levenshtein(col("col1"), col("col2"))) \
       .withColumn("lev_col3", levenshtein(col("col1"), col("col3"))) \
       .withColumn("lev_col4", levenshtein(col("col1"), col("col4")))

# Show the calculated distances
df.show(truncate=False)

# Find the minimum distance across the three columns
df = df.withColumn("best_match", 
                   when(col("lev_col2") <= col("lev_col3"), 
                        when(col("lev_col2") <= col("lev_col4"), "col2", "col4"))
                   .otherwise(when(col("lev_col3") <= col("lev_col4"), "col3", "col4"))
                   )

# Show the DataFrame with the best match
df.select("col1", "col2", "col3", "col4", "best_match").show(truncate=False)

from pyspark.sql.functions import expr

# Calculate Jaro-Winkler similarities
df = df.withColumn("jw_col2", expr("jaro_winkler_similarity(col1, col2)")) \
       .withColumn("jw_col3", expr("jaro_winkler_similarity(col1, col3)")) \
       .withColumn("jw_col4", expr("jaro_winkler_similarity(col1, col4)"))

# Find the highest similarity score (closest match)
df = df.withColumn("best_match", greatest(col("jw_col2"), col("jw_col3"), col("jw_col4")))

df.select("col1", "col2", "col3", "col4", "best_match").show(truncate=False)

 

