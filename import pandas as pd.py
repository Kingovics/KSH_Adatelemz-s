import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

file_path ='C:\Egyetem\stadat-ara0042-1.2.1.4-hu.xlsx'
df = pd.read_excel(file_path)
numpy_array = df.to_numpy()

date=[]
sum=[]
sub1=[]
sub2=[]
ui=0
sheet_plot=0
sheet_line1=0
sheet_line2=0

def YearCheck(x):
    while x <2018 or x >2024:
        if x < 2019:
            x=int(input('Az évszám korábbi mint 2019.\nAdj meg azt az évszámot 2019-2023\n'))
        elif x > 2023:
            x=int(input('Az évszám későbbi mint 2023.\nAdj meg azt az évszámot 2019-2023\n'))
    return x
        
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


def SheetSelectorPlot(x):
    while x <1 or x >3 and sheet_line1!=sheet_line2:
        if x < 1:
            x=int(input('0. Tábla nem létezik\nAdj meg egy számot 1 és 3 között:\n'))
        elif x > 2023:
            x=int(input('Ebben az Ecelben csak 3 táblázat szerepel\nAdj meg egy számot 1 és 3 között:\n'))      
    return x

def SheetSorter(x):
    y=0
    if x==1:
        y=14
    elif x==2:
        y=2*14
    elif x==3:
        y=3*14 
    return y

def SheetSelectorLine(x):
    while x <1 or x >3 and sheet_line1!=sheet_line2:
        if x < 1:
            x=int(input('0. Tábla nem létezik\nAdj meg egy számot 1 és 3 között:\n'))        
        elif x > 2023:
            x=int(input('Ebben az Ecelben csak 3 táblázat szerepel\nAdj meg egy számot 1 és 3 között:\n'))
        elif sheet_line1!=sheet_line2:
            x=int(input('Ebben az Ecelben csak 3 táblázat szerepel\nAdj meg egy számot 1 és 3 között:\n'))
            z=x
            sheet_line2=z
    return x


# Adatok kinyerése Plot regresszióhoz
def DataReadingForPlotRegression(numpy_array):
    for i, sor in enumerate(numpy_array):
        if i==0:
            for j, elem in enumerate(sor):
                if j !=1 and j != 0 and j<=Yearsorter(ui):
                    date.append(elem)
        if i!=0 and i == SheetSorter(sheet_plot):
            for j, elem in enumerate(sor):
                if j!=0 and j!=1 and j<=Yearsorter(ui):
                    sum.append(elem)



# Adatok kinyerése Lineáris regresszióhoz
def DataReadingForLinearRegression(numpy_array):
        for i, sor in enumerate(numpy_array):
            if i!=0 and i == SheetSorter(sheet_line1):
                for j, elem in enumerate(sor):
                    if j !=1 and j<=Yearsorter(ui):
                        sub1.append(elem)
            if i==SheetSorter(sheet_line2):
                for j, elem in enumerate(sor):
                    if j !=1 and j<=Yearsorter(ui):
                            sub2.append(elem)
        return sub1,sub2              


def CreateScatterPlot(x, y, title="Scatter Plot"):
    # Pontdiagram létrehozása
    plt.plot(x, y, marker='o', linestyle='-')
    plt.title(title)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


def CreateLinearRegressionPlot(x, y, title="Linear Regression"):
    # Lineáris regresszió model létrehozása és illesztése az adatokra
    d1=np.array(x)
    d2=np.array(y)
    nan1=np.isnan(d1)
    nan2=np.isnan(d1)
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
    plt.show()

ui=20#nt(input('Adj meg azt az évszámot 2019-2023-ig amelynek az adatait látni szeretnéd:\n'))
sheet_plot=2
sheet_line1=1
sheet_line2=2

ui=YearCheck(ui)
sheet_line1=SheetSelectorLine(sheet_line1)
sheet_line2=SheetSelectorLine(sheet_line2)
DataReadingForPlotRegression(numpy_array)
CreateScatterPlot(date,sum,  title="Scatter Plot")
DataReadingForLinearRegression(numpy_array)
CreateLinearRegressionPlot(sub1,sub2, title="Linear Regression") 