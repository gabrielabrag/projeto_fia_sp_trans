# Databricks notebook source
df = spark.table("sp_trans.raw.shapes")

# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.trusted.shapes")
