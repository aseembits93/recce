import os

import requests
from packaging.version import Version


def is_ci_env():
    # Check "must exist" vars first (fast, avoids lower-casing)
    environ = os.environ
    for env_var in _CI_ENV_VAR_EXIST:
        if env_var in environ:
            return True

    # Now check bool flags (case-insensitive compare to "true")
    for env_var in _CI_ENV_VAR_TRUE:
        env_value = environ.get(env_var)
        if env_value is not None and env_value.lower() == "true":
            return True

    return False


def get_runner():
    # GitHub Action
    if os.environ.get("GITHUB_ACTIONS", "false") == "true":
        return "github actions"

    # GitHub Codespace
    if os.environ.get("CODESPACES", "false") == "true":
        return "github codespaces"

    # CircleCI
    if os.environ.get("CIRCLECI", "false") == "true":
        return "circleci"

    return None


def get_version():
    version_file = os.path.normpath(os.path.join(os.path.dirname(__file__), "VERSION"))
    with open(version_file) as fh:
        version = fh.read().strip()
        return version


def fetch_latest_version():
    current_version = get_version()
    if "dev" in current_version:
        # Skip fetching latest version if it's a dev version
        return current_version

    try:
        url = "https://pypi.org/pypi/recce/json"
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        return data["info"]["version"]
    except Exception:
        return current_version


__version__ = get_version()
__latest_version__ = fetch_latest_version()
__is_recce_outdated__ = Version(__version__) < Version(__latest_version__)

_CI_ENV_VAR_EXIST = {
    "JENKINS_URL",
    "TEAMCITY_VERSION",
    "BITBUCKET_COMMIT",
    "CODEBUILD_BUILD_ID",
}

_CI_ENV_VAR_TRUE = {
    "CI",
    "CIRCLECI",
    "GITHUB_ACTIONS",
    "GITLAB_CI",
    "TRAVIS",
    "APPVEYOR",
    "DRONE",
    "BUILDKITE",
    "AZURE_PIPELINES",
}
