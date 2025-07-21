import asyncio
import subprocess
from fastmcp.client.transports.stdio import StdioTransport
from fastmcp import Client

async def main():
    # ✅ Start the server manually
    proc = await asyncio.create_subprocess_exec(
        "python", "weather_server.py",
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE
    )

    # ✅ Wire the process pipes into StdioTransport
    transport = StdioTransport(proc.stdout, proc.stdin)

    # ✅ Use explicit transport with Client
    async with Client(transport) as mcp_client:
        tools = await mcp_client.get_tools()
        print("🛠 Available Tools:")
        print(tools)

if __name__ == "__main__":
    asyncio.run(main())
