from fastapi import Request
from src.apps.blockchain.services import BlockchainService


async def get_chain(request: Request):
    """
    Handles a request to retrieve the blockchain.

    This function creates an instance of the BlockchainService, retrieves the current blockchain,
    and returns it.

    Args:
        request (Request): The request object

    Returns:
        list[BlockSchema]: The list of blocks in the blockchain.
    """
    service = BlockchainService()
    chain = service.chain
    return chain


async def mine_block(request: Request):
    """
    Handles a request to mine a new block in the blockchain.

    This function creates an instance of the BlockchainService, retrieves the previous block,
    performs the proof of work algorithm to find a new valid proof, creates a new block using
    the new proof and the hash of the previous block, and returns the newly created block.

    Args:
        request (Request): The request object

    Returns:
        BlockSchema: The newly created block in the blockchain.
    """
    service = BlockchainService()
    previous_block = service.get_previous_block()
    new_proof = service.proof_of_work(previous_proof=previous_block.proof)
    new_block = service.create_block(
        proof=new_proof, previous_hash=service.hash(previous_block)
    )
    return new_block
