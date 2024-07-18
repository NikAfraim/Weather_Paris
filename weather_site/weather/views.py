import requests
from django.conf import settings
from django.http import JsonResponse
from django.views import View


class WeatherView(View):
    """View-класс для получения информации о погоде в Париже"""

    def get(self, request):
        api_key = settings.OPENWEATHER_API_KEY
        url = f'http://api.openweathermap.org/data/2.5/weather?q=Paris&appid={api_key}&units=metric'

        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_direction': data['wind']['deg'],
                'wind_speed': data['wind']['speed']
            }
            return JsonResponse(weather_data)
        else:
            return JsonResponse({'error': 'Could not retrieve weather data'},
                                status=response.status_code)
