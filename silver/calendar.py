# Databricks notebook source
df = spark.table("sp_trans.raw.calendar")
display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.trusted.calendar")
