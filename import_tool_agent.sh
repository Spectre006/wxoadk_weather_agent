#!/usr/bin/env bash
set -x

orchestrate env activate spectre_wxo
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )/../../.." &> /dev/null && pwd )

TOOL_PATH="src/spectre/weather_agent/tools"
AGENT_PATH="src/spectre/weather_agent/agents"

orchestrate tools import \
  -k python \
  -f "${SCRIPT_DIR}/${TOOL_PATH}/get_weather.py" \
  -r "${SCRIPT_DIR}/${TOOL_PATH}/requirements.txt" \
  -a weather_app

orchestrate agents import \
  -f "${SCRIPT_DIR}/${AGENT_PATH}/weather_agent.yaml"

