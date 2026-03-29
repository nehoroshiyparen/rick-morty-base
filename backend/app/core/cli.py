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
def sync(resource: str = typer.Argument(...)):
    """
    Sync relations (char-episodes, char-locations)
    """

    async def _run():
        from app.workflows.rick_morty import sync_orchestrator
        await sync_orchestrator.run_one(name=resource)

    asyncio.run(_run())

@app.command()
def import_all():
    async def _run():
        from app.workflows.rick_morty import import_orchestrator

        print("ORCH OBJECT:", import_orchestrator)
        print("HAS RUN_ALL:", hasattr(import_orchestrator, "run_all"))

        await import_orchestrator.run_all()
    
    asyncio.run(_run())


@app.command()
def sync_all():
    async def _run():
        from app.workflows.rick_morty import sync_orchestrator
        await sync_orchestrator.run_all()

    asyncio.run(_run())

if __name__ == "__main__":
    app()