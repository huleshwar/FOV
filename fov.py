import pandas as pd
from sqlalchemy import create_engine

education = pd.read_csv("education/API_SE.XPD.TOTL.GD.ZS_DS2_en_v2.csv", skiprows=4)
education.drop(education.columns[[-1, 0, 2, 3]], axis=1, inplace=True)

cashSurplusDeficit = pd.read_csv("cash surplus/deficit/API_GC.BAL.CASH.GD.ZS_DS2_en_v2.csv", skiprows=4)
cashSurplusDeficit.drop(cashSurplusDeficit.columns[[-1, 0, 2, 3]], axis=1, inplace=True)

taxRevenue = pd.read_excel("tax revenue/API_GC.TAX.TOTL.GD.ZS_DS2_en_v2.xls", skiprows = 3)
taxRevenue.drop(taxRevenue.columns[[-1, 0, 2, 3]], axis=1, inplace=True)

health = pd.read_excel("health/API_SH.XPD.TOTL.ZS_DS2_en_v2.xls", skiprows=3)
health.drop(health.columns[[-1, 0, 2, 3]], axis=1, inplace=True)

education.rename(columns = {"Country Code": "country_code"}, inplace = True)
health.rename(columns = {"Country Code": "country_code"}, inplace=True)
taxRevenue.rename(columns = {"Country Code": "country_code"}, inplace=True)
cashSurplusDeficit.rename(columns = {"Country Code": "country_code"}, inplace=True)

education.to_sql(name='education', con=cnx, if_exists = 'append', index=False, flavor="mysql")
cashSurplusDeficit.to_sql(name='cashSurplusDeficit', con=cnx, if_exists = 'append', index=False, flavor="mysql")
health.to_sql(name='health', con=cnx, if_exists = 'append', index=False, flavor="mysql")
taxRevenue.to_sql(name='taxRevenue', con=cnx, if_exists = 'append', index=False, flavor="mysql")
