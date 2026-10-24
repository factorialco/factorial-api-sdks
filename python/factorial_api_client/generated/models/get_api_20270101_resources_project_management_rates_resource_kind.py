from enum import Enum


class GetApi20270101ResourcesProjectManagementRatesResourceKind(str, Enum):
    EMPLOYEE = "employee"
    JOB_CATALOG_TREE_NODE = "job_catalog_tree_node"
    PROJECT = "project"
    PROJECT_WORKER = "project_worker"

    def __str__(self) -> str:
        return str(self.value)
