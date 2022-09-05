import pymongo #mengimport library pymongo      
import datetime
from flask import Flask, request 

app = Flask(__name__)


client = pymongo.MongoClient("mongodb+srv://maulananurbait:maul@cluster0.d8q1mpa.mongodb.net/?retryWrites=true&w=majority")
db = client['maulana']
my_collections = db['week8']
timestamp = datetime.datetime.now()

@app.route('/location',methods=['GET','POST'])
def location():
    kecepatan = request.args.get('kecepatan')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    
    if request.method == 'POST':
    
       results = my_collections.insert_one({"kecepatan":kecepatan,"latitude":latitude,"longitude":longitude, "timestamp":timestamp})
       print(results)
       return {
            "kecepatan":kecepatan,
            "latitude":latitude,
            "longitude":longitude,
            "timestamp":timestamp
                }

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 8001, debug = True)