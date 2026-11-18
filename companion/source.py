"""Find the next continuous usable dry interval in an Open-Meteo hourly forecast."""
import json,time,urllib.parse,urllib.request
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
from serve import page
INTERVAL=900
def forecast(o):
    query=urllib.parse.urlencode(dict(latitude=o["latitude"],longitude=o["longitude"],hourly="precipitation,precipitation_probability",
           timezone="UTC",timeformat="unixtime",forecast_days=3))
    with urllib.request.urlopen("https://api.open-meteo.com/v1/forecast?"+query,timeout=9) as r:return json.load(r)["hourly"]
def next_window(h,now,minutes,prob):
    if not minutes>0 or not 0<=prob<=100:raise ValueError("Invalid duration or probability")
    start=end=None
    for t,mm,p in zip(h["time"],h["precipitation"],h["precipitation_probability"]):
        if t+3600<=now:continue
        if mm is None or p is None or mm>0 or p>prob:start=end=None;continue
        if start is None or t!=end:start=max(t,now)
        end=t+3600
        if end-start>=minutes*60:return start,start+minutes*60
    return None
def snapshot(o,m):
    h=forecast(o);now=time.time();minutes=float(o.get("minutes",45));prob=float(o.get("max_rain_percent",25))
    result=next_window(h,now,minutes,prob);zone=ZoneInfo(o.get("zone","UTC"))
    if result:
        a,b=result;f=lambda stamp:datetime.fromtimestamp(stamp,zone).strftime("%H:%M")
        value="Now" if a<=now+1 else f(a);detail=f(a)+" - "+f(b)
    else:value="No slot";detail="Within forecast horizon"
    hours=[]
    hourly=dict(zip(h["time"],zip(h["precipitation"],h["precipitation_probability"])))
    first=int(now//3600)*3600
    for t in range(first,min(first+8*3600,max(hourly,default=first-3600)+3600),3600):
        mm,chance=hourly.get(t,(None,None))
        if mm is None or chance is None:state="unknown"
        elif result and t<result[1] and t+3600>result[0]:state="slot"
        else:state="dry" if mm==0 and chance<=prob else "wet"
        hours.append(state)
    return dict(state="Open-Meteo hourly",key=str(result and int(result[0]//3600)),pages=[
        dict(page("DRY WINDOW",value,detail,f"Need {minutes:g} minutes"),hours=hours),page("RAIN LIMIT",f"{prob:g}%","Zero predicted rain volume","Forecast, not a guarantee")])
