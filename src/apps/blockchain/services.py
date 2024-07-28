from .schemas import BlockSchema
from datetime import datetime
import hashlib


class BlockchainMeta(type):
    """
    A metaclass for ensuring a singleton instance of the BlockchainService class.

    This metaclass ensures that only one instance of the class it is applied to
    (typically BlockchainService) is created. If an instance already exists,
    it returns the existing instance instead of creating a new one.

    Attributes:
        _instances (dict): A dictionary to store the single instances of the classes.
    """

    _instances = {}  # type: ignore

    def __call__(cls, *args, **kwargs):
        """
        Ensures that only one instance of the class is created.

        If an instance of the class does not already exist, it creates a new instance
        and stores it in the _instances dictionary. If an instance already exists,
        it returns the existing instance.

        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            The singleton instance of the class.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class BlockchainService(metaclass=BlockchainMeta):
    """
    A service class for managing a simple blockchain.

    This class provides methods to create and manage a blockchain, including
    creating new blocks, validating the blockchain, and performing the proof
    of work algorithm.

    Attributes:
        chain (list[BlockSchema]): The list of blocks in the blockchain.
    """

    def __init__(self):
        """
        Initializes the BlockchainService with an empty chain and creates the genesis block.

        The genesis block is the first block in the blockchain with a proof of 1 and a previous hash of "0".
        """
        self.chain: list[BlockSchema] = []  # type: ignore
        self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof: int, previous_hash: str):
        """
        Creates a new block in the blockchain.

        Args:
            proof (int): The proof of work for the new block.
            previous_hash (str): The hash of the previous block in the chain.

        Returns:
            BlockSchema: The newly created block.
        """
        block = BlockSchema(
            index=len(self.chain) + 1,
            timestamp=datetime.now(),
            proof=proof,
            previous_hash=previous_hash,
            data=None,
        )
        self.chain.append(block)
        return block

    def get_previous_block(self):
        """
        Retrieves the last block in the blockchain.

        Returns:
            BlockSchema: The last block in the chain.
        """
        return self.chain[-1]

    def proof_of_work(self, previous_proof: int):
        """
        Performs the proof of work algorithm to find a valid proof.

        The proof of work algorithm is a computational process that finds a number
        that when hashed with the previous proof results in a hash with four leading zeros.

        Args:
            previous_proof (int): The proof of the previous block.

        Returns:
            int: The new proof that satisfies the proof of work criteria.
        """
        new_proof = 1
        is_valid_proof = False
        while is_valid_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] == "0000":
                is_valid_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block: BlockSchema):
        """
        Creates a SHA-256 hash of a block.

        Args:
            block (BlockSchema): The block to hash.

        Returns:
            str: The hash of the block.
        """
        encoded_block = block.model_dump_json().encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain: list[BlockSchema]):
        """
        Validates the blockchain by checking the hashes and proofs of all blocks.

        Args:
            chain (list[BlockSchema]): The blockchain to validate.

        Returns:
            bool: True if the blockchain is valid, False otherwise.
        """
        for index, current_block in enumerate(chain):
            if index == 0:
                continue
            previous_block = chain[index - 1]
            if current_block.previous_hash != self.hash(previous_block):
                return False
            previous_proof = previous_block.proof
            proof = current_block.proof
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] != "0000":
                return False
        return True
