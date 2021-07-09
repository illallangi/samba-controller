import kopf

CRD_GROUP = "controllers.illallangi.enterprises"
CRD_VERSION = "v1"
CRD_SINGULAR = "samba"


@kopf.index(
    group=CRD_GROUP,
    version=CRD_VERSION,
    singular=CRD_SINGULAR,
)
async def samba_idx(
    namespace,
    body,
    **_,
):
    return {
        namespace: {k: body[k] for k in body},
    }


@kopf.on.probe(
    id=samba_idx.__name__,
)
async def samba_probe(
    samba_idx: kopf.Index,
    **_,
):
    return {
        namespace: [o for o in samba_idx[namespace]]
        for namespace in samba_idx
    }
