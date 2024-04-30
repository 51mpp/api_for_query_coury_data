from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def api_data(country):
    url = "https://restcountries.com/v3.1/name/"+country
    response = requests.get(url, verify = False)
    data = response.json()
    return data

@app.route('/country/<Name>',methods= ['GET'])
def country(Name):
    try:
        data = api_data(Name)
        languages = data[0]['languages']
        language = next(iter(languages))
        name = data[0]['name']['common']
        official = data[0]['name']['official']
        map = data[0]['maps']['googleMaps']
        return jsonify({'name':name,'languages': language,'official':official,'map':map})
    except ValueError:
        return jsonify({'message':'Invalid Input'}),400
    return jsonify({'result':result}),200



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
