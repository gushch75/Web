import data_provider as prov
import logger as log

def temperature_view(senson):
    data=prov.get_temperature(senson)
    log.temperature_logger(data)
    return data

def pressure_view(senson):
    data=prov.get_pressure(senson)
    log.pressure_logger(data)
    return data    

def wind_speed_view(senson):
    data=prov.get_wind_speed(senson)
    log.get_wind_logger(data)
    return data        