from pyspark import pipelines as dp
from pyspark.sql.functions import col, sum, count, round, dense_rank
from pyspark.sql.window import Window

@dp.materialized_view(
    name="gold_payment_analysis",
    comment="Payment mode-wise delivered orders and revenue analysis"
)
def gold_payment_analysis():
    delivered_df = spark.read.table("gold_delivered_orders")

    payment_df = (
        delivered_df
        .groupBy("payment_mode")
        .agg(
            count("*").alias("total_delivered_orders"),
            sum(col("quantity") * col("unit_price")).alias("total_revenue"),
            round(
                sum(col("quantity") * col("unit_price")) / count("*"), 2
            ).alias("average_transaction_value")
        )
    )

    ranking_window = Window.orderBy(col("total_revenue").desc())

    return payment_df.withColumn(
        "revenue_rank",
        dense_rank().over(ranking_window)
    )
