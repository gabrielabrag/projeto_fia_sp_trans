# Databricks notebook source
df = spark.table("sp_trans2.bronze.stop_times")

# COMMAND ----------

# display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans2.silver.stop_times")
