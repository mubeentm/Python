import matplotlib.pyplot as plt
import pandas as pd
"""
data = pd.read_csv("case.csv")
# print(data.columns)
# print(data.head(10))
# print(data[["province","confirmed"]])
fig,ax = plt.subplots(figsize = (6,3))
col_data=data.groupby("province")["confirmed"].sum().reset_index()
sort = col_data.sort_values(by="province")


print(col_data)
ax.bar(sort["province"],sort["confirmed"])
ax.set_ylabel("Accumulated Num Confirmed")
ax.set_xlabel("Province")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.1)
ax.set_title("Number of confirmed COVID-19 Cases in South Korea")
plt.show()
"""
df = pd.read_csv("PatientInfo.csv")
# print(df.head)
df = df.dropna(subset = ['age']) #drop the row where age has missing value
tp_agewise = df['age'].value_counts().rename_axis('age').reset_index(name = "patients_count")
# print(tp_agewise)
plt.figure(figsize= (10,10))
plt.pie(tp_agewise.patients_count,labels = tp_agewise.age,startangle = 90, autopct = '%.1f%%')
plt.title("The age of Patients")
plt.show()