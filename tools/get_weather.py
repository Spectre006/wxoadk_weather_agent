import requests
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.agent_builder.connections import ConnectionType
from ibm_watsonx_orchestrate.run import connections

# This must match the app_id you used when running 'orchestrate connections add'
MY_APP_ID = 'weather_agent'

@tool(
    permission=ToolPermission.READ_ONLY,
    expected_credentials=[
        {"app_id": MY_APP_ID, "type": ConnectionType.API_KEY_AUTH}
    ]
)
def get_weather(city_name: str) -> str:
    """
    Fetches the current weather for a given city using an external API.
    
    Args:
        city_name: The name of the city (e.g., 'London' or 'New York').
        
    Returns:
        A summary string of the current weather and temperature.
    """
    # 1. Retrieve the connection credentials from WxO
    conn = connections.api_key_auth(MY_APP_ID)
    api_key = conn.api_key
    
    # 2. Make the API request
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        return {
            "city": city_name,
            "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],
            "humidity": data['main']['humidity'],
            "description": data['weather'][0]['description'],
            "wind_speed": data['wind']['speed']
        }
    
    except Exception as e:
        return f"Error fetching weather: {str(e)}"