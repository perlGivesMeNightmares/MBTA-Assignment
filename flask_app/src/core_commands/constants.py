from __future__ import annotations
from enum import IntEnum


class TransportTypes(IntEnum):
    LIGHT_RAIL = 0
    HEAVY_RAIL = 1
    COMMUTER_RAIL = 2
    BUS = 3
    FERRY = 4

    @classmethod
    def SUBWAY(cls) -> set[int]:
        return {cls.LIGHT_RAIL.value, cls.HEAVY_RAIL.value}
