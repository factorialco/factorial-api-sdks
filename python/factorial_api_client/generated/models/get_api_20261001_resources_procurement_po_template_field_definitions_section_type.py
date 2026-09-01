from enum import Enum


class GetApi20261001ResourcesProcurementPoTemplateFieldDefinitionsSectionType(str, Enum):
    GENERAL_INFORMATION = "general_information"
    LINE_ITEM_COLUMNS = "line_item_columns"
    NOTES_AND_DELIVERY = "notes_and_delivery"
    VENDOR_CONTACT = "vendor_contact"

    def __str__(self) -> str:
        return str(self.value)
