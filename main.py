import json

from fastapi import FastAPI

from classes.schedule_record_encoder import ScheduleRecordEncoder
from data_collector.parsing_data_collector import ParsingDataCollector

app = FastAPI()
data_collector = ParsingDataCollector()


@app.get("/departments_dict")
async def get_departments_dict():
    return data_collector.get_departments_dict()


@app.get("/departments_streams_dict")
async def get_departments_streams_dict(department_id: int):
    return data_collector.get_departments_streams_dict(department_id)


@app.get("/groups_dict")
async def get_groups_dict(department_id: int, stream_id: int):
    return data_collector.get_groups_dict(department_id, stream_id)


@app.get("/schedule")
async def get_schedule(group_id: int):
    return json.dumps(data_collector.get_schedule(group_id),
                      cls=ScheduleRecordEncoder,
                      ensure_ascii=False)
