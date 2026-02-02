from mcp.server.fastmcp import FastMCP

# 创建 MCP 服务器实例，指定主机和端口
mcp = FastMCP("Hello World App", host="0.0.0.0", port=3000)

# 定义一个工具函数，返回 "Hello World!"
@mcp.tool()
async def hello() -> str:
    """返回 'Hello World!' 字符串"""
    print("hello tool called")
    return "Hello World!"

if __name__ == "__main__":
    print("SSE server started on http://0.0.0.0:3000")
    # 使用 SSE 传输方式
    mcp.run(transport="sse")

