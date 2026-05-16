from pyspark.sql.session import SparkSession
spark = SparkSession.builder.getOrCreate()
sc = spark.sparkContext
lst_fruit = ["apple", "banana", "cherry"]
fruit_rdd =sc.parallelize(lst_fruit)
print(fruit_rdd.collect())