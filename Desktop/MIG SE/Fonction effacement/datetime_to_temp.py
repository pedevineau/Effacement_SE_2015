def datetime_to_temperature(datetime1):
    str1 = str(datetime1.day) + '/' + str(datetime1.month) + '/' +str(datetime1.year) + ' '             +str(datetime1.hour) + ':' +str(datetime1.minute) + ":" + str(datetime1.second)
    Data_frame_temperature =    pd.read_csv("MIG_2015/DATA/SmartEnCo/antibes/direction_architecture_batiments/Temperatures",sep = ";",names=["date et heure","lieu","type1","type2","valeur","unité"],header=None)
    if str1 in Data_frame_temperature["date et heure"]:
        k = Data_frame_temperature["date et heure"].index(str1)
        return(Data_frame_temperature["valeur"][k])
    else:
        return("Date et heure non compatibles")