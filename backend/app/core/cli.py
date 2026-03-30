import typer
import asyncio

app = typer.Typer()

@app.command()
def import_data(
    resource: str = typer.Argument(...),
    mode: str = typer.Option("full"),
    start: int = typer.Option(None),
    end: int = typer.Option(None),
    page: int = typer.Option(None),
):
    """
    Import data (characters, episode, location)
    """

    async def _run():
        from app.workflows.rick_morty import import_orchestrator
        await import_orchestrator.run_one(
            name=resource,
            mode=mode,
            start=start,
            end=end,
            page=page,
        )

    asyncio.run(_run())

@app.command()
def import_all():
    async def _run():
        from app.workflows.rick_morty import import_orchestrator

        print("ЙОУ")

        await import_orchestrator.run_all()
    
    asyncio.run(_run())

if __name__ == "__main__":
    app()