import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Fájl Beolvasás
file_path ='C:\Egyetem\stadat-ara0042-1.2.1.4-hu.xlsx'
df = pd.read_excel(file_path)
numpy_array = df.to_numpy()

#Tömbök Létrehozása
date=[]
sum=[]
sub1=[]
sub2=[]

#Adatbekérés
ui=int(input('Adj meg azt az évszámot 2019-2023-ig amelynek az adatait látni szeretnéd:\n'))
sheet_plot=int(input('Adj meg egy számot 1-3 között, hogy melyik táblázatból a PLOT diagram készüljön:\n'))
sheet_line1=int(input('Adj meg egy számot 1-3 között, hogy melyik legyen az ELSŐ táblázat amiből a lineáris regresszió készüljön:\n'))
sheet_line2=int(input('Adj meg egy számot 1-3 között, hogy melyik legyen a MÁSODIK táblázat amiből a lineáris regresszió készüljön:\n'))

#Évszám Ellenőrzés
def YearCheck(x):
    while x <2019 or x >2023:
        if x < 2019:
            x=int(input('Az évszám korábbi mint 2019.\nAdj meg azt az évszámot 2019-2023\n'))
        elif x > 2023:
            x=int(input('Az évszám későbbi mint 2023.\nAdj meg azt az évszámot 2019-2023\n'))
    return x

#Sorválasztó Évszám alapján      
def Yearsorter(x):
    y=0
    if x==2019:
        y=13
    elif x==2020:
        y=2*13
    elif x==2021:
        y=3*13
    elif x==2022:
        y=4*13
    elif x==2023:
        y=5*13       
    return y

#Tábla Létezésének Ellenőrzése(PLOT)
def SheetSelectorPlot(x):
    while x<1 or x>3:
        if x <1:
            x=int(input('0. Tábla nem létezik\nAdj meg egy számot 1 és 3 között:\n'))
        elif x>3:
            x=int(input('Ebben az Ecelben csak 3 táblázat szerepel\nAdj meg egy számot 1 és 3 között:\n'))      
    return x

#Sorválasztó Kiválasztott Táblázat Alapján
def SheetSorter(x):
    y=0
    if x==1:
        y=14
    elif x==2:
        y=2*14
    elif x==3:
        y=3*14 
    return y

#Tábla Létezésének Ellenőrzése És Azonosság Ellenőrzés(linear_reg)
def SheetsorterAndEqualtyCheck(x,y):
    while x==y:
        y = int(input('A első tábla megegyezik a második táblával!\nKérlek adj meg egy számot ami különbözik az elsőtől:\n'))
        while y<1 or y>3:
            if y<1:
                y=(input('0. Tábla nem létezik\nAdj meg egy számot 1 és 3 között:\n'))        
            elif y>3:
                y=(input('Ebben az Ecelben csak 3 táblázat szerepel\nAdj meg egy számot 1 és 3 között:\n'))
    return y

#Adatok kinyerése Plot regresszióhoz
def DataReadingForPlotRegression(numpy_array):
    for i, sor in enumerate(numpy_array):
        if i==0:
            for j, elem in enumerate(sor):
                if j !=1 and j != 0 and (j<Yearsorter(ui)and j>Yearsorter(ui)-13):
                    date.append(elem)
        if i!=0 and i == SheetSorter(sheet_plot):
            for j, elem in enumerate(sor):
                if j!=0 and j!=1 and (j<Yearsorter(ui)and j>Yearsorter(ui)-13):
                    sum.append(elem)



#Adatok kinyerése Lineáris regresszióhoz
def DataReadingForLinearRegression(numpy_array):
        for i, sor in enumerate(numpy_array):
            if i!=0 and i == SheetSorter(sheet_line1):
                for j, elem in enumerate(sor):
                    if j !=1 and (j<Yearsorter(ui)and j>Yearsorter(ui)-13):
                        sub1.append(elem)
            if i==SheetSorter(sheet_line2):
                for j, elem in enumerate(sor):
                    if j !=1 and (j<Yearsorter(ui)and j>Yearsorter(ui)-13):
                        sub2.append(elem)
        return sub1,sub2              

#Plot Diagram létrehozása
def CreateScatterPlot(x, y, title="Scatter Plot"):
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('Mért hónapok')
    plt.ylabel('Összérték')
    plt.xticks(rotation='vertical')
    plt.show()

# Lineáris regresszió model létrehozása
def CreateLinearRegressionPlot(x, y, title="Linear Regression"):
    d1=np.array(x)
    d2=np.array(y)
    nan1=np.isnan(d1)
    nan2=np.isnan(d2)
    sub1a= np.delete(d1, np.where(nan1))
    sub2a= np.delete(d2, np.where(nan2))
    model = LinearRegression()
    model.fit(sub1a.reshape(-1, 1), sub2a)
        
    # Regressziós egyenes adatainak kiszámolása
    x_line = np.linspace(min(sub1a), max(sub1a), 100)
    y_line = model.predict(x_line.reshape(-1, 1))
        
    # Lineáris regressziós diagram létrehozása
    plt.scatter(sub1a, sub2a, label='Data Points')
    plt.plot(x_line, y_line, color='red', label='Linear Regression Line')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.xticks(rotation='vertical')
    plt.show()

#Függvények meghívása
YearCheck(ui)
sheet_line2=SheetsorterAndEqualtyCheck(sheet_line1,sheet_line2)
sheet_line1=SheetsorterAndEqualtyCheck(sheet_line2,sheet_line1)
DataReadingForPlotRegression(numpy_array)
CreateScatterPlot(date,sum,  title="Scatter Plot")
DataReadingForLinearRegression(numpy_array)
CreateLinearRegressionPlot(sub1,sub2, title="Linear Regression") 