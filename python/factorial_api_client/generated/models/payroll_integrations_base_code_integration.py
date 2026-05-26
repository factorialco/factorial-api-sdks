from enum import Enum


class PayrollIntegrationsBaseCodeIntegration(str, Enum):
    A3INNUVA = "a3innuva"
    A3NOM = "a3nom"
    DATEV = "datev"
    DATEV_API = "datev_api"
    DATEV_LAUDS = "datev_lauds"
    DATEV_LUG_API = "datev_lug_api"
    GISPAGHE = "gispaghe"
    PAIERH = "paierh"
    SILAE = "silae"
    YEAP_PAIERH = "yeap_paierh"
    ZUCCHETTI = "zucchetti"

    def __str__(self) -> str:
        return str(self.value)
