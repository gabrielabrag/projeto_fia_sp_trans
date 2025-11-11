# Databricks notebook source
# display(df)

# COMMAND ----------

df = spark.table("sp_trans2.bronze.stop_times")

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans2.silver.stop_times")
