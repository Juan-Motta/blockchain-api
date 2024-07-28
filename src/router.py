from fastapi import APIRouter
from src.apps.healthcheck.controllers import healthcheck
from src.apps.blockchain.controllers import mine_block, get_chain

router = APIRouter(prefix="/api/v1")

router.get("/healthcheck")(healthcheck)
router.get("/block/chain")(get_chain)
router.get("/block/mine")(mine_block)
