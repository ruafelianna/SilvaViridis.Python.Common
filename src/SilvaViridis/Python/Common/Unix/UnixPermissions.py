from functools import reduce
from pydantic import BaseModel, ConfigDict, validate_call

from .PermissionLevel import PermissionLevel

class UnixPermissions(BaseModel):
    owner : PermissionLevel
    group : PermissionLevel
    other : PermissionLevel

    model_config = ConfigDict(frozen = True)

    @validate_call
    def as_octal(
        self,
    ) -> str:
        return f"{self.owner.value}{self.group.value}{self.other.value}"

    @validate_call
    def as_chmod(
        self,
        turn_on : bool = True,
    ) -> str:
        result = reduce(
            self._sum,
            (
                self._get_permission("u", self.owner),
                self._get_permission("g", self.group),
                self._get_permission("o", self.other),
            ),
            ("", PermissionLevel.none),
        )
        sign = "+" if turn_on else "-"
        return f"{result[0]}{sign}{result[1].name}"

    @staticmethod
    @validate_call
    def _get_permission(
        user_group : str,
        permission : PermissionLevel,
    ) -> tuple[str, PermissionLevel]:
        if permission == PermissionLevel.none:
            return ("", PermissionLevel.none)
        return (user_group, permission)

    @staticmethod
    @validate_call
    def _sum(
        acc : tuple[str, PermissionLevel],
        elem : tuple[str, PermissionLevel],
    ) -> tuple[str, PermissionLevel]:
        return (
            acc[0] + elem[0],
            PermissionLevel(acc[1].value | elem[1].value)
        )
