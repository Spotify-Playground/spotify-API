# IMPORT MODULES
import sys, os
os.chdir('/Users/kimdohoon/git/Spotify-Playground/spotify-API')
lib_dir = f"{os.getcwd()}/Airflow/sample_hooniegit/lib"
sys.path.append(lib_dir)
import spark_modules as lib_spark

# VARIABLES
PATH = f"file:{os.getcwd()}/Airflow/sample_hooniegit/datas/JSON/playlists/Hot Hits Korea.json"

# BUILD SPARK SESSION
spark = lib_spark.build_spark_session()

# READ JSON
dataframe = lib_spark.read_JSON(PATH)
playlist_name = dataframe.select('name').first()[0]

# PARSE JSON DATAS
df_tracks = lib_spark.explode_dict(dataframe, "tracks")
df_items = lib_spark.explode_list(df_tracks, "items")
print("---------------df_items is made----------------------")

# SAVE AS PARQUET
# DIRECTORY NEEDS TO BE FIXED *********************
PARQUET_PATH = f'file:{os.getcwd()}/Airflow/sample_hooniegit/datas/parquets/playlists/Hot Hits Korea/items'
# lib_spark.store_as_parquet(df_items, PARQUET_PATH)

# TEST
if __name__ == "__main__":
    print(playlist_name)
    dataframe.show()
    df_tracks.show()
    df_items.show()