from langchain_core.tools import tool
import json

@tool
def add(x: float, y: float) -> float:
    """Add two numbers together."""
    return x + y

@tool
def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x - y

@tool
def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

@tool
def exponentiate(x: float, y: float) -> float:
    """Raise x to the power of y."""
    return x ** y

# print(add)
# print(add.args_schema.model_json_schema())

# llm_output_string = "{\"x\": 2, \"y\": 3}"
# llm_output_dict = json.loads(llm_output_string)
# print(llm_output_dict)

# exponentiate_result = exponentiate.func(**llm_output_dict)
# print(exponentiate_result)