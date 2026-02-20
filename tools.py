from langchain.tools import tool

@tool
def celsius_to_fahrenheit(value: float) -> float:
    """Converte temperatura de Celsius para Fahrenheit."""
    return (value * 9/5) + 32

@tool
def fahrenheit_to_celsius(value: float) -> float:
    """Converte temperatura de Fahrenheit para Celsius."""
    return (value - 32) * 5/9

@tool
def celsius_to_kelvin(value: float) -> float:
    """Converte temperatura de Celsius para Kelvin."""
    return value + 273.15

@tool
def kelvin_to_celsius(value: float) -> float:
    """Converte temperatura de Kelvin para Celsius."""
    return value - 273.15


@tool 
def km_to_meters(value: float) -> float:
    """Converte distância de quilômetros para metros."""
    return value * 1000

@tool
def meters_to_km(value: float) -> float:
    """Converte distância de metros para quilômetros."""
    return value / 1000

@tool
def meters_to_centimeters(value: float) -> float:
    """Converte distância de metros para centímetros."""
    return value * 100

@tool
def centimeters_to_meters(value: float) -> float:
    """Converte distância de centímetros para metros."""
    return value / 100