import kopf

from .samba import *
from .application import *
from .__version__ import __version__

PREFIX = "controllers.illallangi.enterprises"


@kopf.on.startup()
def configure(
    settings: kopf.OperatorSettings,
    **_,
):
    settings.persistence.progress_storage = kopf.AnnotationsProgressStorage(
        prefix=PREFIX
    )
    settings.persistence.diffbase_storage = kopf.AnnotationsDiffBaseStorage(
        prefix=PREFIX
    )


@kopf.on.probe(
    id="version",
)
async def version_probe(
    **_,
):
    return __version__
