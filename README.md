# wxoadk_weather_agent
Weather AI Agent which provides Weather and Temperate details when user provide name of the city.

## Help Command to see all available Option
orchestrate --help

## Add Cloud Environment:
₹₹₹ orchestrate env add -n <environment-name> -u <service-instance-url> --type ibm_iam --activate ₹₹₹

## Activate Environment:
orchestrate env activate <<environment-name>>

## List all Environment Added:
orchestrate env list

## Remove environment:
orchestrate env remove -n <environment-name>

## Create Connection used by Tool for API Key:
orchestrate connections add -a weather_agent

orchestrate connections configure -a weather_agent --env draft --kind api_key --type team

orchestrate connections set-credentials -a weather_agent --env draft --api-key YOUR_OPENWEATHER_API_KEY

## Import Tool via YAML:
orchestrate agents import -f hello-world-agent.yaml

## Import Python Tool:
orchestrate tools import -k python -f /Users/prashantsharma/Documents/GitHub/wxoadk_weather_agent/tools/get_weather.py -r /Users/prashantsharma/Documents/GitHub/wxoadk_weather_agent/tools/requirements.txt -a weather_agent

## Import Agent:
orchestrate agents import -f /Users/prashantsharma/Documents/GitHub/wxoadk_weather_agent/agents/weather_agent.yaml

## List Connection:
orchestrate connections list

## List Tools:
orchestrate tools list

## List Agents:
orchestrate agents list



