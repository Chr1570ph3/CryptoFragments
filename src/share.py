from shamir_mnemonic.share import Share
import shamir_mnemonic as shamir
from shamir_mnemonic import generate_mnemonics, combine_mnemonics

def create_shares(seed_phrase, total_shares, threshold):
    """
    Crée des parts pour une seed phrase en utilisant Shamir Mnemonic.

    :param seed_phrase: La seed phrase à partager.
    :param total_shares: Nombre total de parts à générer.
    :param threshold: Nombre minimum de parts nécessaires pour reconstituer la seed phrase.
    :return: Liste de parts générées.
    """
    # Encode la seed phrase en bytes
    seed_phrase_bytes = seed_phrase.encode('utf-8')

    # Génère les parts
    shares = generate_mnemonics(1, [(threshold, total_shares)], seed_phrase_bytes)[0]
    return shares

def recover_secret(shares):
    """
    Reconstitue une seed phrase à partir des parts.

    :param shares: Liste des parts nécessaires pour reconstituer la seed phrase.
    :return: La seed phrase reconstituée.
    """
    secret = combine_mnemonics(shares)
    return secret
