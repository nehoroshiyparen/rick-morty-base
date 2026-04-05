from .base_workflow import BaseWorkflow
import logging

class BaseWorkflowOrchestrator():
    def __init__(self, session_factory, workflows: dict[str, BaseWorkflow]):
        self.workflows = workflows
        self.session_factory = session_factory
        self.logger = logging.getLogger(self.__class__.__name__)

    async def run_all(self, mode="full", **kwargs):
        self.logger.warning(f"Start ALL workflows | mode={mode}")

        async with self.session_factory() as session:
            try:
                for name, workflow in self.workflows.items():
                    async with session.begin():
                        self.logger.warning(f"Running workflow: {name}")
                        await workflow.run(
                            session=session,
                            mode=mode,
                            **kwargs
                        )
                self.logger.warning("Finished ALL workflows")

            except Exception:
                self.logger.exception("Orchestrator failed")
                raise