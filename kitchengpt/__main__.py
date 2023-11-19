import click
import uvicorn
from fastapi import FastAPI

import kitchengpt
from kitchengpt.api.router import api_router

app = FastAPI(title="kitchenGPT")

app.include_router(api_router)


@click.command()
@click.version_option(
    version=kitchengpt.__version__,
    prog_name="kitchenGPT",
    message="%(prog)s %(version)s",
)
def main():
    """Console script for kitchengpt."""
    uvicorn.run(
        "kitchengpt.__main__:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        reload_dirs=[
            "kictchengpt",
        ],
        reload_includes=[
            "*.py",
        ],
    )


if __name__ == "__main__":
    main()
