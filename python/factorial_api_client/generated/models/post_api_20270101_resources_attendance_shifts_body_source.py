from enum import Enum


class PostApi20270101ResourcesAttendanceShiftsBodySource(str, Enum):
    API = "api"
    DESKTOP = "desktop"
    DESKTOP_VIA_ONE_ASSISTANT = "desktop_via_one_assistant"
    FACE_RECOGNITION = "face_recognition"
    MOBILE = "mobile"
    MOBILE_GEOLOCATION = "mobile_geolocation"
    MOBILE_GEOLOCATION_VIA_ONE_ASSISTANT = "mobile_geolocation_via_one_assistant"
    MOBILE_VIA_ONE_ASSISTANT = "mobile_via_one_assistant"
    ONE_ASSISTANT = "one_assistant"
    QR_CODE = "qr_code"
    SHARED_DEVICE = "shared_device"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
