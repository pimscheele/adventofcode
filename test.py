sdf = spark.read.table("analytics_curated.online_pageview")
sdf = sdf.limit(1000)

sdf.toPandas().to_csv('mycsv.csv')

f = open("data.txt", "a")
f.write("Now the file has more content!")
f.close()