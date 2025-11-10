# Databricks notebook source
df = spark.table("sp_trans2.bronze.shapes")

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans2.silver.shapes")
