from fastmcp import FastMCP

mcp = FastMCP("Weather MCP")

@mcp.tool()
def get_weather(city: str) -> str:
    return f"The weather in {city} is lovely in {city} 🌤️"

if __name__ == "__main__":
    mcp.run()
