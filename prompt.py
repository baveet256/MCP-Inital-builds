from mcp.server.fastmcp import FastMCP

mcp = FastMCP("prompter")

@mcp.prompt()
def get_prompt(topic:str)->str:
    """
    Returns a prompt that will do a detailed analysis on a topic
    Args:
        topic : The topic to do research on
    """
    return f"Do a very detailed analysis, optimized for better results on topic : {topic}"

if __name__ == "__main__":
    mcp.run()
