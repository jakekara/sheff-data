import pandas as pd


names = pd.read_csv("data/name_replace.csv")
names["School_16"] = names["School_16"].str.replace("*","")
names["School_16"] = names["School_16"].str.strip()

names


def get_lat(school_name):
    
    #print "'" + school_name + "'"
    df = names[names["School_16"].replace(",","") == str(school_name).strip()]
    #print df
    if len(df.index) < 1:
        ret = -1,-1
    else:
        ret = float(df["lat"].replace(",","")), float(df["lng"])
    #print ret
    return ret

def add_location(df,sch_col,lat_col="lat",lng_col="lng"):

    ret = df.copy()

    ret[lat_col] = ret.apply(lambda x: get_lat(x[sch_col])[0],axis=1)
    ret[lng_col] = ret.apply(lambda x: get_lat(x[sch_col])[1],axis=1)

    return ret