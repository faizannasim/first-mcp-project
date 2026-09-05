from fastmcp import FastMCP
import random
import json

mcp  = FastMCP("MCP Servers")

tasks = []


@mcp.tool
def Add_number(a:int,b:int)->int:

    """ Add two Number togetHer.
    args:
        a:first Number
        b:second number

    returns:
         THe sum of a and b
    """
    return a + b



@mcp.tool
def random_no(min_val:int=1,max_val:int=100)->int:
    """generate a random number btw 1 to 100

    args:
       min_val:minimum value(default:1)
       max_val:maximum value(default:100)
    
    returns:
         a random intgers btw min_value and max_value        
     """
    return random.randint(min_val,max_val)


#########################TODOTASK#############

@mcp.tool
def add_task(title:str)->str:
    """Add a new task"""

    task={
        "id" :len(tasks) + 1,
        "title":title,
        "completed" : False
    }

    tasks.append(task)

    return f"task added successfully : {title} "


@mcp.tool
def list_task()->list:
    """Get all tasks."""
    return tasks


@mcp.tool
def completed_task(task_id : int) ->str:
    """get completed task done"""

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return f"Task {task_id} completed Successfully"
        
    return f" task {task_id} Not Found"
    



@mcp.tool
def delete_task(task_id:int) ->str:
    """delete a task"""

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return f"Task {task_id} deleted successfully" 

    return f" Task Id {task_id} Not Found"






@mcp.resource("info://server")
def server_info()->str:
    """server info"""
    info={
  "serverName": "MyServer",
  "serverType": "Application Server",
  "environment": "Development",
  "host": "localhost",
  "port": 8080,
  "protocol": "HTTP",
  "status": "Running",
  "ipAddress": "127.0.0.1",
  "operatingSystem": "Windows",
  "runtime": "Node.js",
  "version": "20.x" 
  }

    return json.dumps(info,indent=2)



if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000 )