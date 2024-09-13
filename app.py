from flask import Flask, render_template, request, jsonify
import requests


app = Flask(__name__)




@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/forecast', methods = ['POST','GET'])
def forecast():
    location = request.form.get('location')

    api_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q' : location,
        'appid' : '1614b5da5099844a8e791922c11b84ce'
    }
    
    response = requests.get(api_url, params=params)


    if response.status_code == 200:
        api_data = response.json()
    else:
        return 'some error occured!'
    
    state_name = api_data['name']
    
    temperature = format(api_data['main']['temp'] - 273.13,'.2f')
    latitude, longitude, region, time_zone = api_data['coord']['lat'], api_data['coord']['lon'], api_data['sys']['country'], api_data['timezone']
    humidity, visibility, Weather_condition, sea_level= api_data['main']['humidity'], int(api_data['visibility']/1000), api_data['weather'][0]['description'], api_data['main']['sea_level']


    utc_timezone = f'{time_zone // 3600}:{(time_zone% 3600) // 60}'
    
    return render_template('index.html',temp=f'{temperature} °C', state_name = state_name, region = region, lattitude = latitude, longitude = longitude,
                            time_zone = f'UTC {utc_timezone}', humidity=f'{humidity} %', Visibility = f'{visibility} Km', Weather_Condition= Weather_condition, sea_level= f'{sea_level} hPa')


@app.route('/api')
def api():

    location = request.form.get('location')

    api_url = "https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q' : 'delhi',
        'appid' : '1614b5da5099844a8e791922c11b84ce'
    }
    
    response = requests.get(api_url, params=params)


    if response.status_code == 200:
        api_data = response.json()
    else:
        return 'some error occured!'

    return api_data


if __name__ == '__main__':
    app.run(debug=True)