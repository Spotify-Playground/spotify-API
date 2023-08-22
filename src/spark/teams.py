from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, explode
# import glob

# spark session 빌드
spark = SparkSession.builder.getOrCreate()

# json 파일 읽기
PATH = 'file:/Users/kimdohoon/Desktop/TESTFOLDER/39_Tinfo.json'
dataframe = spark.read.option("multiline", "true").json(PATH)
print("===========================================================")
dataframe.show()

# df_specification = dataframe.select( *col , explode(col( col=dict )).alias( name1 , name2 , .. ))
df_specification = dataframe.withColumn("team", expr("data.team")) \
                            .withColumn("venue", expr("data.venue")) \
                            .select(explode("team").alias("code", "country", "founded", "team_id", "logo", "name", "national"),
                                    explode("venue").alias("venue_address", "venue_capacity", "venue_location", "venue_id", "venue_image", "venue_name", "venue_surface"))
# dataframe 확인
print("===========================================================")
df_specification.show()