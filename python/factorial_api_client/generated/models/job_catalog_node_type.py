from enum import Enum


class JobCatalogNodeType(str, Enum):
    JOBCATALOG_TREEFAMILY = "jobcatalog_treefamily"
    JOBCATALOG_TREEFUNCTION = "jobcatalog_treefunction"
    JOBCATALOG_TREELEVEL = "jobcatalog_treelevel"
    JOBCATALOG_TREEROLE = "jobcatalog_treerole"
    JOBCATALOG_TREEROOT = "jobcatalog_treeroot"

    def __str__(self) -> str:
        return str(self.value)
