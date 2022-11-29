def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours*3600) // 60
    seconds_reamining = (seconds -hours*3600 - minutes*60)
    return hours, minutes, seconds_reamining

hours, minutes, seconds = convert_seconds(7600)
print(hours, minutes, seconds)