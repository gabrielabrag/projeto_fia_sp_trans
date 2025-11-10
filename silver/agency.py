# Databricks notebook source
df = spark.table("sp_trans.raw.agency")
display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.trusted.agency")
