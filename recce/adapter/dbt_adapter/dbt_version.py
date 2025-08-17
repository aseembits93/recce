from dbt import version as dbt_version
from packaging.version import Version, parse


class DbtVersion:

    def __init__(self):
        dbt_ver = parse(dbt_version.__version__)
        if dbt_ver.is_prerelease:
            dbt_ver = parse(dbt_ver.base_version)
        self.dbt_version = dbt_ver

    @staticmethod
    def parse(version: str):
        from packaging import version as v

        return v.parse(version)

    def as_version(self, other):
        if isinstance(other, Version):
            return other
        if isinstance(other, str):
            return parse(other)
        return parse(str(other))

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
