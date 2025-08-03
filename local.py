from mcp.server.fastmcp import FastMCP


mcp = FastMCP("LocalNotes")

@mcp.tool()
def add_note_to_file(content:str) ->str:
    """
    appends the content to the local notes

    Args: The text to append
    """
    filename = 'notes.txt'

    try:
        with open(filename,"a",encoding="utf-8") as f:
            f.write(content + "\n")
        return f"content appended to {filename}"
    except Exception as e:
        return f"Error while appending to {filename}, with error : {e}"
    

@mcp.tool()
def read_notes() ->str:
    """ Reads and returns the content of the user's local notes"""
    filename = 'notes.txt'

    try:
        with open(filename,"r",encoding="utf-8") as f:
            notes = f.read()
        return f" local notes: {notes}"
    except FileNotFoundError:
        return "File not found."
    except Exception as e:
        return f"Error while reading from {filename}, with error : {e}"


if __name__ == "__main__":
    mcp.run()
