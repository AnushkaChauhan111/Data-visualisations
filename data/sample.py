import csv
import matplotlib.pyplot as plt
from datetime import datetime

with open("data/GHCND_sample_csv (1)-1.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    TMAX = []
    TMIN = []
    DATE = []
    for row in reader:
        try:
            Tmax = int(row[6])
            Tmin = int(row[7])
            Date = datetime.strptime(row[5],'%Y%m%d')
            
        except:
            continue
            print("Error")

        else:
            TMAX.append(Tmax)
            TMIN.append(Tmin)
            DATE.append(Date)

    fig,ax = plt.subplots(figsize=(8,7))
    plt.title("Graph of max & min temp with dates")
    plt.xlabel("Dates")
    ax.tick_params(axis='x', labelsize=6)
    plt.ylabel("Tmin and Tmax")
    ax.plot(DATE,TMAX,c='blue',alpha = 0.5)
    ax.plot(DATE,TMIN,c='red',alpha = 0.5)
    plt.fill_between(DATE,TMIN,TMAX,alpha = 0.1)
    plt.show()