from .base_import_workflow import BaseImportWorkflow

class ImportOrchestrator:
    def __init__(self, workflows: dict[str, BaseImportWorkflow]):
        self.workflows = workflows

    def run_one(self, name: str, mode="full", **kwargs):
        workflow = self.workflows[name]
        return workflow.run(mode, **kwargs)

    def run_all(self, mode="full", **kwargs):
        for workflow in self.workflows.values():
            workflow.run(mode, **kwargs)