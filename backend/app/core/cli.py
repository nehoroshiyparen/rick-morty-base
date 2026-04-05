import typer
import asyncio

app = typer.Typer()

@app.command()
def import_all():
    """
    Import all data from Rick and Morty API (locations → characters → episodes)
    """
    async def _run():
        from app.workflows.rick_morty import import_orchestrator
        await import_orchestrator.run_all()

    asyncio.run(_run())

if __name__ == "__main__":
    app()