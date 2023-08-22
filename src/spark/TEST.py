# IMPORT MODULES
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, explode

# BUILD SPARK SESSION
spark = SparkSession.builder.getOrCreate()

# READ PARQUET
# DIRECTORY NEEDS TO BE FIXED *********************
PARQUET_PATH = 'file:/Users/kimdohoon/git/Spotify-Playground/spotify-API/Airflow/sample_hooniegit/datas/parquets/playlists/Hot Hits Korea/items/*'
dataframe = spark.read.parquet(PARQUET_PATH)


df_specification = dataframe.withColumn("album_type", expr("track.album.album_type")) \
                            .withColumn("album_images", expr("track.album.images")) \
                            .withColumn("album_name", expr("track.album.name")) \
                            .withColumn("album_artists", expr("track.album.artists.name")) \
                            .withColumn("popularity", expr("track.popularity")) \
                            .withColumn("track_name", expr("track.name")) \
                            .select("album_type", "album_images", "album_name", "album_artists", "popularity", "track_name")

# 
df_specification.show()