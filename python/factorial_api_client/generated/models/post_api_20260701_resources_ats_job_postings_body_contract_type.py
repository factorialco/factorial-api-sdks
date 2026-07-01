from enum import Enum


class PostApi20260701ResourcesAtsJobPostingsBodyContractType(str, Enum):
    ALTERNANT = "alternant"
    APPRENDISTATO = "apprendistato"
    APPRENTICESHIP = "apprenticeship"
    APPRENTISSAGE = "apprentissage"
    A_TEMPO_PARCIAL = "a_tempo_parcial"
    A_TERMO_CERTO = "a_termo_certo"
    A_TERMO_INCERTO = "a_termo_incerto"
    CLT = "clt"
    COM_PLURALIDADE_DE_EMPREGADORES = "com_pluralidade_de_empregadores"
    DE_CURTA_DURACAO = "de_curta_duracao"
    DE_MUITA_CURTA_DURACAO = "de_muita_curta_duracao"
    ESTAGIO = "estagio"
    FIXED_DISCONTINUED = "fixed_discontinued"
    FREELANCE = "freelance"
    INDEFINITE = "indefinite"
    INTERIM = "interim"
    INTERN = "intern"
    JOVEM_APRENDIZ = "jovem_aprendiz"
    MINIJOB = "minijob"
    OTHER = "other"
    PER_HOUR = "per_hour"
    PJ = "pj"
    PRE_REFORMA = "pre_reforma"
    PROMESSA_DE_TRABALHO = "promessa_de_trabalho"
    RECIBOS_VERDES = "recibos_verdes"
    SEM_TERMO = "sem_termo"
    TELETRABALHO = "teletrabalho"
    TEMPORARY = "temporary"
    TRAINING = "training"
    VENDOR_CONTRACTOR = "vendor_contractor"
    VOLUNTEER = "volunteer"
    WERKSTUDENT = "werkstudent"

    def __str__(self) -> str:
        return str(self.value)
