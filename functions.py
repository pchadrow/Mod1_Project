import locale
def int_to_dollar(x):
    return locale.currency(x, grouping=True)
    
def dollar_to_int(dollar):
    #x = dollar.replace('$', "").replace(',', "")
    return float(dollar.replace('$', "").replace(',', ""))

def add_columns(x, y):
    if (x > 0) & (y > 0):
        return x + y
    else:
        return 0
    
def splitNewCol(dfName, columnName):
    newColumn = []
    for val in dfName[columnName]:
        newColumn.append(val.split(","))
    return(newColumn)
    
def countNewCol(dfName, columnName):
    newCount = []
    for val in dfName[columnName]:
        newCount.append(len(val))
    return(newCount)

def gross(keyword, df):
    gross = 0
    for i in df.index:
        if any(keyword in g for g in df['genresList'][i]):
            gross += (df['domestic_gross'][i])
    return(gross)

def count(keyword, df):
    count = 0
    for i in df.index:
        if any(keyword in g for g in df['genresList'][i]):
            count += 1
    return(count)

def meanGross(keyword, df):
    genreGross = gross(keyword)
    genreCount = count(keyword)
    mean = genreGross/genreCount
    return mean

def budget(keyword, df):
    budget = 0
    for i in df.index:
        if any(keyword in g for g in df['genresList'][i]):
            budget += (df['production_budget'][i])
    return(budget)

def meanBudget(keyword, df):
    genreBudget = budget(keyword)
    genreCount = count(keyword)
    mean = genreBudget/genreCount
    return mean

def returnRate(keyword, df):
    gross = meanGross(keyword)
    budget = meanBudget(keyword)
    increase = gross - budget
    returnRate = (increase/budget) * 100
    return returnRate

def getGenreInfo(keyword, df):    
    allInfo = {}
    title = []
    genre = []
    domestic_gross = []
    foreign_gross = []
    worldwide_gross = []
    production_budget = []
    for i in df.index:
        
        if any(keyword in g for g in df['genresList'][i]):
            genre.append(keyword)
            title.append(df['movie_name'][i])
            domestic_gross.append(df['domestic_gross'][i])
            foreign_gross.append(df['foreign_gross'][i])
            worldwide_gross.append(df['worldwide_gross'][i])
            production_budget.append(df['production_budget'][i])
        allInfo.update({'Title' : title,
                        'Genre' : genre,
                        'Domestic Gross' : domestic_gross,
                        'Foreign Gross' : foreign_gross,
                        'Worldwide Gross' : worldwide_gross,
                        'Production Budget' : production_budget})
    return allInfo