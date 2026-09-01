from enum import Enum


class PostApi20261001ResourcesAtsJobPostingsBodyCategory(str, Enum):
    ADMINISTRATION_AND_SECRETARIAT = "administration_and_secretariat"
    DESIGN_AND_ARCHITECTURE = "design_and_architecture"
    EDUCATION_AND_SOCIAL_POLICY = "education_and_social_policy"
    ENGINEERING = "engineering"
    FINANCE = "finance"
    HR = "hr"
    IT = "it"
    LEGAL = "legal"
    MANAGEMENT_AND_CONSULTING = "management_and_consulting"
    MARKETING_AND_COMMUNICATION = "marketing_and_communication"
    NURSING_AND_THERAPY = "nursing_and_therapy"
    OTHER = "other"
    PHYSICIANS = "physicians"
    PUBLIC_SECTOR = "public_sector"
    PURCHASING_MATERIALS_ADMINISTRATION_AND_LOGISTICS = (
        "purchasing_materials_administration_and_logistics"
    )
    SALES = "sales"
    SCIENCES_AND_RESEARCH = "sciences_and_research"
    SERVICE_INDUSTRY_AND_MANUFACTURING = "service_industry_and_manufacturing"
    SPORTS_ART_AND_CREATIVE_JOBS = "sports_art_and_creative_jobs"

    def __str__(self) -> str:
        return str(self.value)
