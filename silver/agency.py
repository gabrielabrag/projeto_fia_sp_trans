# Databricks notebook source
df = spark.table("sp_trans2.bronze.agency")
display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("ssp_trans2.silver.agency")
