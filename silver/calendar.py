# Databricks notebook source
df = spark.table("sp_trans2.bronze.calendar")
display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans2.silver.calendar")
