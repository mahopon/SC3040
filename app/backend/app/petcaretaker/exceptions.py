class PetCareTakerNotFound(Exception):
    """
    Raised when attempting to access or update a PetCareTaker
    that does not exist in the database.
    """

    pass
