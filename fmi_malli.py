import datetime as dt
from fmiopendata.wfs import download_stored_query




# Retrieve the latest hour of data from a place
end_time = dt.datetime.utcnow()
start_time = end_time - dt.timedelta(hours=1)
# Convert times to properly formatted strings
start_time = start_time.isoformat(timespec="seconds") + "Z"
# -> 2020-07-07T12:00:00Z
end_time = end_time.isoformat(timespec="seconds") + "Z"
# -> 2020-07-07T13:00:00Z
location = input('Anna haettava paikkakunta\n')

obs = download_stored_query("fmi::observations::weather::multipointcoverage",
                            args=["place=" + location,
                                  "starttime=" + start_time,
                                  "endtime=" + end_time])

print(obs.data)
print(obs.data.keys())

latest_tstep = max(obs.data.keys())
station_id = list(obs.data[latest_tstep].keys())
print(station_id[0])


print(obs.data[latest_tstep][station_id[0]])
print(obs.data[latest_tstep][station_id[0]]["Air temperature"])
# -> {'value': 18.0, 'units': 'degC'}
# The observation times are the primary key
lampotila = obs.data[latest_tstep][station_id[0]]["Air temperature"]["value"]
print("Lämpötila on: " + str(lampotila))
print("Aika: " + str(latest_tstep + dt.timedelta(hours=2)))

