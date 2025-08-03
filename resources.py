from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resources")


@mcp.resource("inventory://overview")
def get_inventory_overview()-> str:
    """
    Returns overview of memory.
    """
    overview = """
        Menu:
            Coffee,
            Tea,
            Cookies,
            Pizza,
            Burgers
        """
    return overview.strip()

if __name__ == "__main__":
    mcp.run()


    