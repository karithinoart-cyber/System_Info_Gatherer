"""
hash_generator.py
--------------------------------------
Generate cryptographic hashes for files.

Supported Algorithms:
✔ MD5
✔ SHA1
✔ SHA256

Author : I.P SINGH
Version: 2.0
"""

import hashlib
from pathlib import Path


class HashGenerator:

    BUFFER_SIZE = 65536

    @staticmethod
    def _calculate_hash(file_path, algorithm):
        """
        Calculate the hash of a file.

        Parameters
        ----------
        file_path : str | Path
            Path to the file.
        algorithm : str
            md5, sha1 or sha256.
        """

        file_path = Path(file_path)

        if not file_path.exists():
            raise FileNotFoundError(f"{file_path} does not exist.")

        hasher = hashlib.new(algorithm)

        with open(file_path, "rb") as file:

            while True:

                data = file.read(HashGenerator.BUFFER_SIZE)

                if not data:
                    break

                hasher.update(data)

        return hasher.hexdigest()

    @staticmethod
    def md5(file_path):

        return HashGenerator._calculate_hash(
            file_path,
            "md5"
        )

    @staticmethod
    def sha1(file_path):

        return HashGenerator._calculate_hash(
            file_path,
            "sha1"
        )

    @staticmethod
    def sha256(file_path):

        return HashGenerator._calculate_hash(
            file_path,
            "sha256"
        )

    @staticmethod
    def generate_all(file_path):
        """
        Generate all hashes.
        """

        return {

            "File": str(file_path),

            "MD5":
                HashGenerator.md5(file_path),

            "SHA1":
                HashGenerator.sha1(file_path),

            "SHA256":
                HashGenerator.sha256(file_path)

        }

    @staticmethod
    def save_hashes(file_path, output_file):
        """
        Save hashes to a text file.
        """

        hashes = HashGenerator.generate_all(file_path)

        with open(output_file, "w", encoding="utf-8") as file:

            file.write("=" * 60 + "\n")
            file.write("FILE HASH REPORT\n")
            file.write("=" * 60 + "\n\n")

            for key, value in hashes.items():
                file.write(f"{key}: {value}\n")

        return output_file