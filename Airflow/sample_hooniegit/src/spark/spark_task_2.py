# IMPORT MODULES
import sys, os
os.chdir('/Users/kimdohoon/git/Spotify-Playground/spotify-API')
lib_dir = f"{os.getcwd()}/Airflow/sample_hooniegit/lib"
sys.path.append(lib_dir)
import spark_modules as lib_spark
from pyspark.sql.functions import expr

# BUILD SPARK SESSION
spark = lib_spark.build_spark_session()

# READ PARQUET
# DIRECTORY NEEDS TO BE FIXED *********************
PARQUET_PATH = f'file:{os.getcwd()}/Airflow/sample_hooniegit/datas/parquets/playlists/Hot Hits Korea/items'
dataframe = spark.read.parquet(PARQUET_PATH)

df_specification = dataframe.withColumn("track_name", expr("track.name"))
df_specification = df_specification.select(
    "track.album",
    "track.artists",
    "track_name",
    "track.popularity"
)
print("---------------dataframe is made----------------------")

df_specification = df_specification.withColumn("album_type", expr("album.album_type"))
df_specification = df_specification.withColumn("album_images", expr("album.images"))
df_specification = df_specification.withColumn("album_name", expr("album.name"))
df_specification = df_specification.withColumn("album_artists", expr("album.artists"))
df_specification = df_specification.withColumn("album_artists", expr("album_artists.name"))
df_specification = df_specification.withColumn("artists_name", expr("artists.name"))

df_arranged = df_specification.select(
    "album_name",
    "album_artists",
    "album_type",
    "album_images",
    "track_name",
    "popularity",
    "artists_name"
)
df_arranged.show()
print("---------------arange is done----------------------")

# DIRECTORY NEEDS TO BE FIXED *********************
PATH = f"file:{os.getcwd()}/Airflow/sample_hooniegit/datas/parquets/playlists/Hot Hits Korea/table"
lib_spark.store_as_parquet(df_arranged, PATH, True)
print("---------------load is done----------------------")


'''
dataframe.printSchema()
root
 |-- added_at: string (nullable = true)
 |-- added_by: struct (nullable = true)
 |    |-- external_urls: struct (nullable = true)
 |    |    |-- spotify: string (nullable = true)
 |    |-- href: string (nullable = true)
 |    |-- id: string (nullable = true)
 |    |-- type: string (nullable = true)
 |    |-- uri: string (nullable = true)
 |-- is_local: boolean (nullable = true)
 |-- primary_color: string (nullable = true)
 |-- track: struct (nullable = true)
 |    |-- album: struct (nullable = true)
 |    |    |-- album_type: string (nullable = true)
 |    |    |-- artists: array (nullable = true)
 |    |    |    |-- element: struct (containsNull = true)
 |    |    |    |    |-- external_urls: struct (nullable = true)
 |    |    |    |    |    |-- spotify: string (nullable = true)
 |    |    |    |    |-- href: string (nullable = true)
 |    |    |    |    |-- id: string (nullable = true)
 |    |    |    |    |-- name: string (nullable = true)
 |    |    |    |    |-- type: string (nullable = true)
 |    |    |    |    |-- uri: string (nullable = true)
 |    |    |-- available_markets: array (nullable = true)
 |    |    |    |-- element: string (containsNull = true)
 |    |    |-- external_urls: struct (nullable = true)
 |    |    |    |-- spotify: string (nullable = true)
 |    |    |-- href: string (nullable = true)
 |    |    |-- id: string (nullable = true)
 |    |    |-- images: array (nullable = true)
 |    |    |    |-- element: struct (containsNull = true)
 |    |    |    |    |-- height: long (nullable = true)
 |    |    |    |    |-- url: string (nullable = true)
 |    |    |    |    |-- width: long (nullable = true)
 |    |    |-- name: string (nullable = true)
 |    |    |-- release_date: string (nullable = true)
 |    |    |-- release_date_precision: string (nullable = true)
 |    |    |-- total_tracks: long (nullable = true)
 |    |    |-- type: string (nullable = true)
 |    |    |-- uri: string (nullable = true)
 |    |-- artists: array (nullable = true)
 |    |    |-- element: struct (containsNull = true)
 |    |    |    |-- external_urls: struct (nullable = true)
 |    |    |    |    |-- spotify: string (nullable = true)
 |    |    |    |-- href: string (nullable = true)
 |    |    |    |-- id: string (nullable = true)
 |    |    |    |-- name: string (nullable = true)
 |    |    |    |-- type: string (nullable = true)
 |    |    |    |-- uri: string (nullable = true)
 |    |-- available_markets: array (nullable = true)
 |    |    |-- element: string (containsNull = true)
 |    |-- disc_number: long (nullable = true)
 |    |-- duration_ms: long (nullable = true)
 |    |-- episode: boolean (nullable = true)
 |    |-- explicit: boolean (nullable = true)
 |    |-- external_ids: struct (nullable = true)
 |    |    |-- isrc: string (nullable = true)
 |    |-- external_urls: struct (nullable = true)
 |    |    |-- spotify: string (nullable = true)
 |    |-- href: string (nullable = true)
 |    |-- id: string (nullable = true)
 |    |-- is_local: boolean (nullable = true)
 |    |-- name: string (nullable = true)
 |    |-- popularity: long (nullable = true)
 |    |-- preview_url: string (nullable = true)
 |    |-- track: boolean (nullable = true)
 |    |-- track_number: long (nullable = true)
 |    |-- type: string (nullable = true)
 |    |-- uri: string (nullable = true)
 |-- video_thumbnail: struct (nullable = true)
 |    |-- url: string (nullable = true)
'''