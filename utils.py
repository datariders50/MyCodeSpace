#PySpark Code to Get Maximum Value from 4 Columns

from pyspark.sql import SparkSession
from pyspark.sql.functions import greatest

# Initialize Spark session
spark = SparkSession.builder.appName("MaxValueFromColumns").getOrCreate()

# Sample data with 4 columns
data = [(10, 20, 30, 40), (5, None, 25, 15), (None, None, 35, None), (7, 14, 21, 28)]
df = spark.createDataFrame(data, ["col1", "col2", "col3", "col4"])

# Get the maximum value from the 4 columns
df_max = df.withColumn("max_value", greatest("col1", "col2", "col3", "col4"))

# Show the result
df_max.show()

#PySpark Code to Convert Column Values to Uppercase and Handle Null Values
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, upper, when

# Initialize Spark session
spark = SparkSession.builder.appName("UpperCaseTransformation").getOrCreate()

# Sample data with some null values
data = [("John", "Doe", None), ("Jane", None, "New York"), (None, "Smith", "Los Angeles")]
df = spark.createDataFrame(data, ["first_name", "last_name", "city"])

# Apply upper transformation and handle nulls for each column
df_transformed = df.select([when(col(c).isNotNull(), upper(col(c))).otherwise(None).alias(c) for c in df.columns])

# Show the result
df_transformed.show()
