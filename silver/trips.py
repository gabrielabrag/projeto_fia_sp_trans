# Databricks notebook source
df = (spark.read
                .option("header", "true")      # força sem header
                .option("inferSchema", "true")
                .option("delimiter", ",")
                .csv("/Volumes/sp_trans/raw/carga_fria/trips.txt"))
display(df)


# COMMAND ----------

df.write.mode("overwrite").saveAsTable("sp_trans.raw.trips")
