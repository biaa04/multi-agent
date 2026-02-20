from langchain.chat_models import init_chat_model
from langchain.agents import create_agent
from tools import (
    km_to_meters,
    meters_to_km,
    meters_to_centimeters,
    centimeters_to_meters,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
)

model = init_chat_model("ollama:llama3.2")

agent_meters_prompt = (
    "Você é um agente executor de conversões de distância." 
    " REGRAS OBRIGATÓRIAS: " 
    "Você deve chamar exatamente UMA ferramenta. " 
    "Após obter o resultado da ferramenta, você deve responder ao usuário e ENCERRAR. " 
    "Nunca faça uma segunda conversão. "   
    "Nunca valide a resposta novamente. " 
    "Nunca reconverta unidades. " 
    "Nunca explique o raciocínio interno. " 
    "Formato final obrigatório: " 
    "<valor convertido> <unidade>"
)

tools_agent_meters = [
    km_to_meters,
    meters_to_km,
    meters_to_centimeters,
    centimeters_to_meters
]

agent_meters = create_agent(
    model=model,
    tools=tools_agent_meters,
    system_prompt=agent_meters_prompt  
)

agent_temp_prompt = (
    "Você é um agente executor de conversões de temperatura." 
    " REGRAS OBRIGATÓRIAS: " 
    "Você deve chamar exatamente UMA ferramenta. " 
    "Após obter o resultado da ferramenta, você deve responder ao usuário e ENCERRAR. " 
    "Nunca faça uma segunda conversão. " 
    "Nunca valide a resposta novamente. " 
    "Nunca reconverta unidades. " 
    "Nunca explique o raciocínio interno. " 
    "Formato final obrigatório: " 
    "<valor convertido> <unidade>"
)

tools_agent_temp = [
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius
]

agent_temp = create_agent(
    model=model,
    tools=tools_agent_temp,
    system_prompt=agent_temp_prompt
)