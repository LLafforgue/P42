
class Archive():
    def __init__(self, name: str) -> None:
        """Initialize a new archive collection.

        Creates an internal structure used to store archived file contents
        and assigns a name to the archive.

        Args:
            name (str): Name of the archive collection.
        """
        self.__data = []
        self.name = name

    @staticmethod
    def clean(string: str, key="/") -> str:
        """
        Extracts the substring after the last occurrence of a given character.
        Used to clean the programme name (without folrders directorie)

        Args:
            string (str): The input string to process.
            key (str): A single character used as a separator.

        Returns:
            str: The substring after the last occurrence of `key`.
                If `key` is longer than one character,
                returns the original string.
        """
        if len(key) > 1:
            return string
        i = 0
        stop = 0
        while i < len(string):
            if string[i] == key:
                stop = i + 1
            i += 1
        return string[(stop):]

    def add_archive(self, arg: str) -> None:
        """Load a text file into the archive.

        If no file name is provided, a default file is used.
        The file content is read and stored in memory.

        Args:
            arg (str): Path or name of the file to archive.

        Handled Exceptions:
            OSError: Raised if the file cannot be opened or read.
        """
        f = None
        file = Archive.clean(arg)
        print(f"\nAccessing Storage Vault: {arg}")
        if not arg:
            arg = "./ancient_fragment.txt"
        if file != "ancient_fragment.txt":
            raise ValueError("use the filename : 'ancient_fragment.txt'")
        try:
            f = open(arg, 'r')
            print("Conection established...\n")
            self.__data.append({file: f.read()})
        except OSError as e:
            print(f"ERROR: Failed to read archive. {e}")
        finally:
            if f:
                f.close()

    def display_one_archive(self, arch: str) -> None:
        """Display the content of a specific archived file.

        If the archive is empty or if the specified file name
        does not exist, no content is displayed.

        Args:
            arch_name (str): Name of the archived file to display.
        """
        file = Archive.clean(arch)
        if len(self.__data) == 0:
            print("No data in archive\n")
        for arc in self.__data:
            if file in arc.keys():
                print(arc[file] + "\n")


if __name__ == "__main__":
    arg = "./ancient_fragment.txt"
    print("=== CYBER ARCHIVES - Preservation SYSTEM ===")
    print(f"file openned : {arg}\n")
    try:
        new_archive = Archive("Cyber_Archive_01")
        new_archive.add_archive(arg)
        print("\nRECOVERED DATA:\n")
        new_archive.display_one_archive(arg)
        print("Data recovery complete. Storage unit disconnected\n")
    except (ValueError, TypeError, OSError) as e:
        print(e)
