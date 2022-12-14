from guizero import App, TextBox, Text, PushButton
import datetime as dt
from fmiopendata.wfs import download_stored_query

def weatherData():

    end_time = dt.datetime.utcnow()
    start_time = end_time - dt.timedelta(hours=1)
    start_time = start_time.isoformat(timespec="seconds") + "Z"
    end_time = end_time.isoformat(timespec="seconds") + "Z"

    location = myLocationData.value

    obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                                args=["place=" + location,
                                      "starttime=" + start_time,
                                      "endtime=" + end_time])

    latest_tstep = max(obs.data.keys())
    station_id = list(obs.data[latest_tstep].keys())

    temperature = obs.data[latest_tstep][station_id[0]]["Air temperature"]["value"]
    temperature_message.value = "Lämpötila on: " + temperature + "m/s")

app = App(title="Jussi Kunnas")
