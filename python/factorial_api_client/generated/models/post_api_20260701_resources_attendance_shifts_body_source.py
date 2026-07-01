from enum import Enum


class PostApi20260701ResourcesAttendanceShiftsBodySource(str, Enum):
    API = "api"
    DESKTOP = "desktop"
    FACE_RECOGNITION = "face_recognition"
    MOBILE = "mobile"
    MOBILE_GEOLOCATION = "mobile_geolocation"
    QR_CODE = "qr_code"
    SHARED_DEVICE = "shared_device"
    SYSTEM = "system"

    def __str__(self) -> str:
        return str(self.value)
