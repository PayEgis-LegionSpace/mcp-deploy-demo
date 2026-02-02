# MCP Hello World 示例

这是一个使用 Python 和 MCP 官方库开发的简单 MCP 服务器程序，支持 SSE（Server-Sent Events）传输方式。

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行程序

```bash
python mcp_server.py
```

服务器启动后，将在 `http://0.0.0.0:3000` 上监听 SSE 连接。

## 功能说明

该程序创建了一个 MCP 服务器，提供了一个 `hello` 工具函数，调用时会返回 "Hello World!" 字符串。

## SSE 访问

服务器通过 SSE 传输方式提供服务，可以通过以下方式访问：

- SSE 端点：`http://localhost:3000/sse`
- 服务器监听地址：`0.0.0.0:3000`

## 服务器配置文件

项目包含两个配置文件：

### 1. `mcp_config.json` - HTTP/SSE 传输配置

用于通过 HTTP/SSE 方式连接服务器：

```json
{
  "mcpServers": {
    "hello-world-app": {
      "url": "http://localhost:3000/sse",
      "name": "Hello World App",
      "description": "一个简单的 MCP 服务器，提供 hello 工具返回 Hello World!"
    }
  }
}
```

### 2. `mcp_settings.json` - STDIO 传输配置

用于通过标准输入输出方式启动服务器（如果客户端支持）：

```json
{
  "mcpServers": {
    "hello-world-app": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {},
      "cwd": ".",
      "timeout": 30000,
      "restart": true
    }
  }
}
```

**注意**：当前服务器使用 SSE 传输方式，主要使用 `mcp_config.json` 配置。

## 配置到 Dify

要将此 MCP 服务器配置到 Dify 中，请按照以下步骤操作：

1. **启动 MCP 服务器**：
   ```bash
   python mcp_server.py
   ```

2. **在 Dify 中添加 MCP 服务器**：
   - 登录 Dify，进入左侧导航栏的"工具" → "MCP"
   - 点击"添加 MCP 服务器（HTTP）"按钮
   - 填写配置信息：
     - **服务器 URL**：`http://localhost:3000/sse`
       - 如果 Dify 和 MCP 服务器在同一台机器上，使用 `http://localhost:3000/sse`
       - 如果 Dify 在远程访问，使用 `http://your-server-ip:3000/sse`（将 `your-server-ip` 替换为实际服务器 IP）
     - **名称**：Hello World App（或自定义名称）
     - **服务器标识符**：hello-world-app（小写字母、数字、下划线或连字符，最多 24 个字符）

3. **使用 MCP 工具**：
   - 在 Agent 应用中，MCP 工具会出现在工具列表中，按服务器分组
   - 在 Workflow 应用中，MCP 工具可以作为节点添加到工作流中

## 测试 SSE 连接

您可以使用以下 Python 代码测试 SSE 连接：

```python
import httpx
import asyncio

async def main():
    async with httpx.AsyncClient() as client:
        async with client.stream("GET", "http://localhost:3000/sse") as response:
            async for line in response.aiter_lines():
                if line.startswith("data:"):
                    print(line[5:].strip())

if __name__ == "__main__":
    asyncio.run(main())
```

或者使用 curl 命令：

```bash
curl -N http://localhost:3000/sse
```

