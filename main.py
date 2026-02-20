from agents import agent_meters, agent_temp
from langchain.tools import tool
from langchain.agents import create_agent
from pydantic import BaseModel, Field
from agents import model

class ConverterInput(BaseModel):
    user_input: str = Field(description="Texto original do usuário contendo a conversão")

@tool(args_schema=ConverterInput)
def temperature_converter(user_input: str) -> str:
    """Função para converter temperaturas usando o agente de temperatura."""
    result = agent_temp.invoke({
        "messages": [{"role": "user", "content": user_input}]
    })

    return result["messages"][-1].text

@tool(args_schema=ConverterInput)
def distance_converter(user_input: str) -> str:
    """Função para converter distâncias usando o agente de metros."""
    result = agent_meters.invoke({
        "messages": [{"role": "user", "content": user_input}]
    })

    return result["messages"][-1].text

supervisor_prompt = (
    "Você é um roteador de ferramentas."
    " REGRAS CRÍTICAS: Você NÃO extrai parâmetros, Você NÃO cria JSON, Você NÃO interpreta números,Você NÃO modifica a frase do usuário"
    " Você apenas repassa exatamente a mensagem original para a ferramenta correta no campo `user_input`."
    " Se for temperatura → temperature_converter, Se for distância → distance_converter"
    " Passe o texto original integralmente. Nunca altere a string. Nunca crie campos adicionais."
)

supervisor_agent = create_agent(
    model=model,
    tools=[temperature_converter, distance_converter],
    system_prompt=supervisor_prompt
)

query = "Converta 100 km para metros"

for step in supervisor_agent.stream(
    {"messages": [{"role": "user", "content": query}]}
):
    for update in step.values():
        for message in update.get("messages", []):
            message.pretty_print()