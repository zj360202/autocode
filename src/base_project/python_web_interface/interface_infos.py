interface_temp = """
import uvicorn
from fastapi import FastAPI

app = FastAPI()

{interface_list}

if __name__ == '__main__':
    uvicorn.run("interface:app", host="0.0.0.0", port={port}, reload=True)
"""

func_temp = """
@app.{method}("/{route}")
async def {func_name}({params_list}):
    {func_content}
"""