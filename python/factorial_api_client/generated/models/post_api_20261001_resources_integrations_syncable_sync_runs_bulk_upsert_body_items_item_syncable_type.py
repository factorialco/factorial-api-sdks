from enum import Enum


class PostApi20261001ResourcesIntegrationsSyncableSyncRunsBulkUpsertBodyItemsItemSyncableType(
    str, Enum
):
    COMPENSATIONSCOMPENSATION = "compensations/compensation"
    EMPLOYEE_UPDATESCONTRACT_CHANGE = "employee_updates/contract_change"
    EMPLOYEE_UPDATESLEAVE = "employee_updates/leave"
    EMPLOYEE_UPDATESNEW_HIRE = "employee_updates/new_hire"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_ACADEMIC_TITLE = (
        "employee_updates/personal_change_academic_title"
    )
    EMPLOYEE_UPDATESPERSONAL_CHANGE_ADDRESS = "employee_updates/personal_change_address"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_BANK = "employee_updates/personal_change_bank"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_BIRTH_NAME = "employee_updates/personal_change_birth_name"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_COUNTRY_OF_BIRTH = (
        "employee_updates/personal_change_country_of_birth"
    )
    EMPLOYEE_UPDATESPERSONAL_CHANGE_EMAIL = "employee_updates/personal_change_email"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_GENDER = "employee_updates/personal_change_gender"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_HEALTH_INSURANCE = (
        "employee_updates/personal_change_health_insurance"
    )
    EMPLOYEE_UPDATESPERSONAL_CHANGE_ID = "employee_updates/personal_change_id"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_IRPF = "employee_updates/personal_change_irpf"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_NAME = "employee_updates/personal_change_name"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_NATIONALITY = "employee_updates/personal_change_nationality"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_PERMITS_AND_CERTIFICATES = (
        "employee_updates/personal_change_permits_and_certificates"
    )
    EMPLOYEE_UPDATESPERSONAL_CHANGE_PHONE_NUMBER = "employee_updates/personal_change_phone_number"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_PLACE_OF_BIRTH = (
        "employee_updates/personal_change_place_of_birth"
    )
    EMPLOYEE_UPDATESPERSONAL_CHANGE_RESIDENCE = "employee_updates/personal_change_residence"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_TAXES_AND_DEDUCTIONS = (
        "employee_updates/personal_change_taxes_and_deductions"
    )
    EMPLOYEE_UPDATESPERSONAL_CHANGE_WORKPLACE = "employee_updates/personal_change_workplace"
    EMPLOYEE_UPDATESPERSONAL_CHANGE_WORK_ACTIVITY = "employee_updates/personal_change_work_activity"
    EMPLOYEE_UPDATESTERMINATION = "employee_updates/termination"
    EMPLOYEE_UPDATESWORKED_TIME = "employee_updates/worked_time"
    EXPENSESEXPENSE = "expenses/expense"
    FINANCEVENDOR = "finance/vendor"

    def __str__(self) -> str:
        return str(self.value)
