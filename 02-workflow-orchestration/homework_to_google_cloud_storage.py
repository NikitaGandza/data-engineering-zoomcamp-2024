import pyarrow as pa
import pyarrow.parquet as pq
import os

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/home/src/dtc-de-course-412521-90e7f73b134e.json"

bucket_name = 'dtc-zoomcamp-nikita'
project_id = 'dtc-de-course-412521'

table_name = "taxi_homework"

root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data(data, *args, **kwargs):
    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=["lpep_pickup_date"],
        filesystem=gcs
    )