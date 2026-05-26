from enum import Enum


class PostApi20251001ResourcesBankingBankAccountsCreateManualBodyAccountNumberType(str, Enum):
    BANK_NAME_AND_ACCOUNT_NUMBER = "bank_name_and_account_number"
    CLABE = "clabe"
    IBAN = "iban"
    OTHER = "other"
    ROUTING_NUMBER_AND_ACCOUNT_NUMBER = "routing_number_and_account_number"
    SORT_CODE_AND_ACCOUNT_NUMBER = "sort_code_and_account_number"

    def __str__(self) -> str:
        return str(self.value)
