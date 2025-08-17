from dbt import version as dbt_version
from packaging import version as pkg_version


class DbtVersion:

    def __init__(self):
        dbt_ver = self.parse(dbt_version.__version__)
        if dbt_ver.is_prerelease:
            dbt_ver = self.parse(dbt_ver.base_version)
        self.dbt_version = dbt_ver

    @staticmethod
    def parse(version: str):
        return pkg_version.parse(version)

    def as_version(self, other):
        from packaging.version import Version

        if isinstance(other, Version):
            return other
        if isinstance(other, str):
            return self.parse(other)
        return self.parse(str(other))

    def __ge__(self, other):
        return self.dbt_version >= self.as_version(other)

    def __gt__(self, other):
        return self.dbt_version > self.as_version(other)

    def __lt__(self, other):
        return self.dbt_version < self.as_version(other)

    def __le__(self, other):
        return self.dbt_version <= self.as_version(other)

    def __eq__(self, other):
        return self.dbt_version.release[:2] == self.as_version(other).release[:2]

    def __str__(self):
        return ".".join([str(x) for x in list(self.dbt_version.release)])
