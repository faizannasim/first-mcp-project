
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/aaec476c-5412-41f5-a6cb-6e86ec30c2bd" />
<br>

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/135fa031-205f-4b65-b0db-bcdf67172567" /># MCP Tools Server

A simple **MCP (Model Context Protocol)** server built with Python and **FastMCP**.

This project is beginner-friendly and demonstrates how to create MCP tools, run an MCP server over HTTP, and test the tools using MCP Inspector.

---

## ✨ Features

This server currently provides the following tools:

### 1. Add Number
**Tool:** `Add_number`

Adds two numbers and returns their sum.

**Example:**
```
a = 10
b = 20
Result = 30
```

### 2. Random Number
**Tool:** `random_no`

Generates a random integer between the provided minimum and maximum values.

**Default values:**
```
min_val = 1
max_val = 100
```

**Example:**
```
min_val = 1
max_val = 50
Result = 37
```

### 3. Todo Task Management
The server also includes a simple in-memory Todo system.

**Available tools:**
| Tool | Description |
|------|-------------|
| `add_task` | Add a new task |
| `list_task` | Get all tasks |
| `completed_task` | Mark a task as completed |
| `delete_task` | Delete a task |

**Example task:**
```json
{
  "id": 1,
  "title": "Learn MCP",
  "completed": false
}
```

> **Note:** Todo data is stored in memory using a Python list. Data will be lost when the server is restarted.

---

## 📦 MCP Resource

The server also exposes:

```
info://server
```

This resource returns basic server information such as server name, environment, host, port, operating system, runtime, and version.

---

## ✅ Requirements

- Python 3.10+
- `uv`
- FastMCP
- Node.js and `npx` (for MCP Inspector)

---

## 🚀 Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

Create and use the virtual environment with `uv`:

```bash
uv sync
```

If dependencies are not already defined, install FastMCP:

```bash
uv add fastmcp
```

---

## ▶️ Run the MCP Server

If your Python file is named `main.py`:

```bash
uv run main.py
```

The server runs using **Streamable HTTP** on:

```
http://127.0.0.1:8000/mcp
```

If you are using the Todo server example on port `8001`, use:

```
http://127.0.0.1:8001/mcp
```

---

## 🔍 Test with MCP Inspector

Start MCP Inspector in another terminal:

```bash
npx -y @modelcontextprotocol/inspector
```

Open the Inspector URL shown in the terminal, usually:

```
http://localhost:6274
```

Add the server manually with:

| Field | Value |
|-------|-------|
| Transport | Streamable HTTP |
| URL | `http://127.0.0.1:8000/mcp` |

Then connect to the server.

Go to the **Tools** tab to test:
- `Add_number`
- `random_no`
- `add_task`
- `list_task`
- `completed_task`
- `delete_task`

Go to the **Resources** tab to test:
- `info://server`

### 📸 MCP Inspector
*Example of the server connected to MCP Inspector.*

---

## 📁 Project Structure

A simple project can look like this:

```
MCP Server/
│
├── main.py
├── pyproject.toml
├── uv.lock
├── README.md
└── mcp-inspector.png
```

---

## ⚙️ How It Works

The basic flow is:

```
MCP Inspector
      |
      | Streamable HTTP
      v
FastMCP Server
      |
      +---- Add_number
      |
      +---- random_no
      |
      +---- add_task
      |
      +---- list_task
      |
      +---- completed_task
      |
      +---- delete_task
      |
      +---- info://server
```

---

## 🎯 Learning Goals

This project is useful for learning:

- What an MCP server is
- How to create MCP tools with `@mcp.tool`
- How tool arguments work
- How to expose resources with `@mcp.resource`
- How to run an MCP server using HTTP
- How to connect an MCP server to MCP Inspector
- How multiple tools can be exposed from one MCP server
- Basic CRUD-style application logic with an in-memory data store

---

## 👤 Author

Built as a learning project while exploring MCP and FastMCP.
