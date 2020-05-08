from fastapi import FastAPI, Query, Path, Body
import uvicorn
from pydantic import BaseModel, Field, HttpUrl
from pydantic.color import Color
from typing import List, Set
from datetime import datetime, time, timedelta

# Init
app = FastAPI(debug=True)


# @app.post("/items/")
# async def update_item(*,
#             start_datetime: datetime = Body(None),
#             end_datetime: datetime = Body(None),
#             repeat_at: time = Body(None),
#             process_after: timedelta = Body(None)):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "repeat_at": repeat_at,
#         "process_after": process_after,
#         "start_process": start_process,
#         "duration": duration,
#         "process_after": process_after.seconds
#     }
@app.post("/items/")
async def update_item(*,
            setColor: Color):
    return {
        "item color": setColor,
        "Name": setColor.as_named(),
        "Hex": setColor.as_hex(),
        "RGB": setColor.as_rgb_tuple()
    }

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port="8000")