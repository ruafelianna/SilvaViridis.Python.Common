from functools import reduce
from pydantic import BaseModel, ConfigDict, validate_call

from .Permission import Permission

class UnixPermission(BaseModel):
    owner : Permission
    group : Permission
    other : Permission

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
            ("", Permission.none),
        )
        sign = "+" if turn_on else "-"
        return f"{result[0]}{sign}{result[1].name}"

    @staticmethod
    @validate_call
    def _get_permission(
        user_group : str,
        permission : Permission,
    ) -> tuple[str, Permission]:
        if permission == Permission.none:
            return ("", Permission.none)
        return (user_group, permission)

    @staticmethod
    @validate_call
    def _sum(
        acc : tuple[str, Permission],
        elem : tuple[str, Permission],
    ) -> tuple[str, Permission]:
        return (
            acc[0] + elem[0],
            Permission(acc[1].value | elem[1].value)
        )
