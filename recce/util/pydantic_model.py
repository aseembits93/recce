import pydantic
from pydantic import BaseModel


def pydantic_model_json_dump(model: BaseModel):
    pydantic_version = pydantic.version.VERSION
    pydantic_major = pydantic_version.split(".")[0]

    if pydantic_major == "1":
        return model.json(exclude_none=True)
    else:
        return model.model_dump_json(exclude_none=True)


def pydantic_model_dump(model: BaseModel):
    if _PYDANTIC_V1:
        return model.dict()
    else:
        return model.model_dump()
def _dump(model: BaseModel):
    return model.dict()
def _dump(model: BaseModel):
    return model.model_dump()

pydantic_version = pydantic.version.VERSION

pydantic_major = pydantic_version.split(".")[0]

_pydantic_major = pydantic.version.VERSION.split(".")[0]

_pydantic_version = pydantic.version.VERSION

_PYDANTIC_V1 = pydantic.version.VERSION.startswith("1.")
