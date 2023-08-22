from pyspark.sql import SparkSession
import io
from contextlib import redirect_stdout

spark = SparkSession.builder.getOrCreate()

PATH_list = [
"file:/Users/kimdohoon/Desktop/data_scouter/39_leagueInfo.json",
"file:/Users/kimdohoon/Desktop/data_scouter/39_players.json",
"file:/Users/kimdohoon/Desktop/data_scouter/39_Tinfo.json",
"file:/Users/kimdohoon/Desktop/data_scouter/42_Psquad.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230423_events.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230423_fixture.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230423_h2h.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230423_lineUps.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230423_Pstatistics.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230423_Tstatistics.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230509_predictions.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230509_Ptopscorers.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230509_standing.json",
"file:/Users/kimdohoon/Desktop/data_scouter/230509_Tstats.json"
]

for PATH in PATH_list:
    dataframe = spark.read.option("multiline", "true").json(PATH)
    output = io.StringIO()
    with redirect_stdout(output):
        dataframe.printSchema()
    result = output.getvalue()
    filename = PATH.split("/")[-1].split(".")[0]
    schema_txt_path = f"/Users/kimdohoon/Desktop/data_scouter/{filename}.txt"
    with open(schema_txt_path, "w") as f:
        f.write(result)

# Print the schema as well
print("task is done")
