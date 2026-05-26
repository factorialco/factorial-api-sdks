from enum import Enum


class PostApi20260401ResourcesPayrollIntegrationsBaseCodesBodyIntegration(str, Enum):
    A3INNUVA = "a3innuva"
    A3NOM = "a3nom"
    AGENDA = "agenda"
    DATEV = "datev"
    DATEV_API = "datev_api"
    DATEV_LAUDS = "datev_lauds"
    DATEV_LUG_API = "datev_lug_api"
    GISPAGHE = "gispaghe"
    JOB_SISTEMI = "job_sistemi"
    PAIERH = "paierh"
    SAGE100 = "sage100"
    SILAE = "silae"
    TEAM_SYSTEM = "team_system"
    YEAP_PAIERH = "yeap_paierh"
    ZUCCHETTI = "zucchetti"

    def __str__(self) -> str:
        return str(self.value)
