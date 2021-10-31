from pymongo import MongoClient
import dns
import pandas as pd


def get_dataframe() :
    client = MongoClient("mongodb+srv://bdat:bdat1004@cluster0-xu6kh.mongodb.net/test")
    db = client.mdata
    collection = db['mbase']
    cursor = collection.find({})

    df = pd.DataFrame()
    for document in cursor:
        tmp_se = pd.Series( [document['name '],
                            document[' ratings '],
                            document[' Duration']]
                           )
        df = df.append( tmp_se, ignore_index=True )
    df.columns = ['Movie name', 'Ratings', 'Duration' ]
    return df

data = get_dataframe()
print ("The top 10 movies")
data = data.sort_values('Ratings', ascending=False)
top10= data[0:10]
#print(top10)
#print ("Top longest movies")
#data["Duration"].map(lambda x: x[1:] if x != None)

col_values=list(data["Duration"])
new_value = list()
for val in col_values :
    if val != None :
        val = val.split()
        new_value.append(int(val[0]))
    else:
        new_value.append(0)
data["Time"] = new_value
data_longest= data.sort_values('Time', ascending=False)
longest10= data_longest[0:10]
#longest10
#for bar chart of top 10 movies


from flask import Flask, request,render_template
app = Flask(__name__)
labels = list(top10["Movie name"])
values= list(top10["Ratings"])

@app.route('/home')
def bar():
    bar_labels=labels
    bar_values=values
    return render_template('homepage.html', title='Top 10 movies', max=10, labels=bar_labels, values=bar_values)
if __name__ == '__main__':
    app.run()