import uvicorn
import pytz

from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI()


class TimezoneMSG(BaseModel):
    timezone: str


@app.get('/time')
def get_datetime():
    t_now = datetime.now()
    return {
        "datetime": t_now.isoformat()
    }


@app.post('/time/by_timezone')
def get_datetime_by_timezone(timezone: TimezoneMSG):
    name = timezone.timezone
    timezone = pytz.timezone(name)
    t_now = datetime.now(timezone)
    return{
         "datetime": t_now.isoformat(),
         "timezone": name
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5555)