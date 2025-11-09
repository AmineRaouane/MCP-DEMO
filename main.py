from fastapi import FastAPI
# from fastapi_mcp import FastApiMCP
from starlette.responses import PlainTextResponse

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("mcp-server")

app = FastAPI()

# ------------------ MCP Tools ------------------

@app.post("/sum_two", operation_id="sum_two")
async def sum_two(a: int, b:int) -> int:
    logger.info(f"Fetching chat history for a={a}, b={b}")
    return a + b


# mcp = FastApiMCP(
#     app,
#     include_operations=["sum_two"]
# )
# mcp.mount_http()

# ------------------ Normal FastAPI Endpoints ------------------

@app.get("/app/live/")
async def mcp_liveness():
    return PlainTextResponse("OK", status_code=200)

@app.get("/app/ready/")
async def mcp_readyness():
    return PlainTextResponse("OK", status_code=200)

@app.post("/dummy_endpoint/")
async def dummy_endpoint():
    logger.info("Dummy endpoint was successfully reached.")
    return PlainTextResponse("Success", status_code=200)
