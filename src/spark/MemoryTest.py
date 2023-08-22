# IMPORT MODULES
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, explode

# BUILD SPARK SESSION
# MEM : 10.20 > 10.60 = 0.3G
spark = SparkSession.builder.getOrCreate()

# LOAD PARQUETS
# MEM : 10.30 > 11.50 = 1.2G
PARQUET_PATH = 'file:/Users/kimdohoon/git/Spotify-Playground/spotify-API/Airflow/sample_hooniegit/datas/parquets/playlists/Hot Hits Korea/items/*'
dataframe = spark.read.parquet(PARQUET_PATH)

# PARSE - 1 Step
# MEM : 10.30 > 11.50 = 1.2G
df_specification = dataframe.withColumn("album_type", expr("track.album.album_type")) \
                            .withColumn("album_images", expr("track.album.images")) \
                            .withColumn("album_name", expr("track.album.name")) \
                            .withColumn("album_artists", expr("track.album.artists.name")) \
                            .withColumn("popularity", expr("track.popularity")) \
                            .withColumn("track_name", expr("track.name")) \
                            .select("album_type", "album_images", "album_name", "album_artists", "popularity", "track_name")
df_specification.show() # > This does not take MEMORIES

# SAVE AS PARQUET
# MEM : 10.00 > 11.44 = 1.44G
df_specification.cache()
df_specification.coalesce(1).write.mode("overwrite").parquet('file:/Users/kimdohoon/Desktop/Spark')