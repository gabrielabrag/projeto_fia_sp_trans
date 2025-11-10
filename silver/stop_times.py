# Databricks notebook source
df = spark.table("sp_trans.raw.stop_times")

# COMMAND ----------

display(df)

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.trusted.stop_times")
