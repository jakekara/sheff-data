import pandas as pd


names = pd.read_csv("data/name_replace.csv")
names["School_16"] = names["School_16"].str.replace("*","")
names["School_16"] = names["School_16"].str.strip()

names


def get_lat(school_name):

    # Last-minute tweak, Jackie says Discovery has moved!
    # No longer at |41.73814668700004,|-72.67549714
    if school_name.title().strip() == "Discovery Academy":
        #return 41.7191977,-72.6753181
        #return 41.719254,-72.67509
        return 41.719276,-72.67492

    if school_name.title().strip() == "E. C. Goodwin Technical High School":
        return 41.687416,-72.80687
    
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