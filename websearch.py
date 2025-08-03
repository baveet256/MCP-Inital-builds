from mcp.server.fastmcp import FastMCP

mcp = FastMCP()

@mcp.tool()
def perform_websearch(query: str):
    ##funtion
    return "Search done"

mcp.run()