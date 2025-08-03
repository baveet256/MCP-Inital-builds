from mcp.server.fastmcp import FastMCP
import io
from mcp.server.fastmcp.utilities.types import Image

mcp = FastMCP("Screenshot-Demo")


@mcp.tool()
def capture_screenshot() -> Image:
    """
    Capture the current screen and return the image. Use this whenever the user requests a screenshot

    """
    import pyautogui
    buffer = io.BytesIO()

    ss = pyautogui.screenshot()
    ss.convert("RGB").save(buffer,format="JPEG",quality=60,optimize=True)

    return Image(data=buffer.getvalue(),format="jpeg")

if __name__ == "__main__":
    mcp.run()

