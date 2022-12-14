from guizero import App, TextBox, Text, PushButton
import datetime as dt
from fmiopendata.wfs import download_stored_query

def weatherData():
    # Retrieve the latest hour of data from a place
    end_time = dt.datetime.utcnow()
    start_time = end_time - dt.timedelta(hours=1)
    # Convert times to properly formatted strings
    start_time = start_time.isoformat(timespec="seconds") + "Z"
    # -> 2020-07-07T12:00:00Z
    end_time = end_time.isoformat(timespec="seconds") + "Z"
    # -> 2020-07-07T13:00:00Z


    location = myLocationData.value

    obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                                args=["place=" + location,
                                      "starttime=" + start_time,
                                      "endtime=" + end_time])


    latest_tstep = max(obs.data.keys())
    station_id = list(obs.data[latest_tstep].keys())

    location_message.value = myLocationData.value

    date_now.value = "Aika: " + str(latest_tstep + dt.timedelta(hours=2))
    date_now.repeat(5000, weatherData)

    temperature = obs.data[latest_tstep][station_id[0]]["Air temperature"]["value"]
    temperature_message.value = "Lämpötila on: " + str(temperature) + " C"
    temperature_message.repeat(5000, weatherData)

    wind_speed = obs.data[latest_tstep][station_id[0]]["Wind speed"]["value"]
    wind_speed_message.value = "Tuulen nopeus on: " + str(wind_speed) + " m/s"
    wind_speed_message.repeat(5000, weatherData)

    humidity = obs.data[latest_tstep][station_id[0]]["Relative humidity"]["value"]
    humidity_message.value = "Ilman kosteus on: " + str(humidity) + "%"
    humidity_message.repeat(5000, weatherData)

    pressure = obs.data[latest_tstep][station_id[0]]["Pressure (msl)"]["value"]
    pressure_message.value = "Ilmanpaine on: " + str(pressure) + " hPa"
    pressure_message.repeat(5000, weatherData)

app = App(title="Jussi Kunnas")

message = Text(app, "Tervetuloa Säätieto appiin")

message2 = Text(app, "Anna paikkakunta")

myLocationData = TextBox(app)

button = PushButton(app, text="Hae tiedot", command=weatherData)

location_message = Text(app)
date_now = Text(app)
temperature_message = Text(app)
wind_speed_message = Text(app)
humidity_message = Text(app)
pressure_message = Text(app)

app.display()