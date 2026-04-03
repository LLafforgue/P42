class Archive():
    def __init__(self, name: str) -> None:
        """Initialize a new archive collection.

        Creates an internal structure used to store archived file contents
        and assigns a name to the archive.

        Args:
            name (str): Name of the archive collection.
        """
        self.__data = {}
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
        print(f"\nAccessing Storage Vault: {arg}")
        if not arg:
            arg = "ancient_fragment.txt"
        try:
            file = Archive.clean(arg)
            f = open(arg, 'r')
            print("Conection established...\n")
            self.__data[file] = f.read()
        except OSError as e:
            print(f"ERROR: Failed to read archive. {e}")
        finally:
            if f:
                f.close()

    def display_one_archive(self, arch_name: str) -> None:
        """Display the content of a specific archived file.

        If the archive is empty or if the specified file name
        does not exist, no content is displayed.

        Args:
            arch_name (str): Name of the archived file to display.
        """
        file = Archive.clean(arch_name)
        if len(self.__data) == 0:
            print("No data in archive\n")
        if file in self.__data.keys():
            print(f"Content of {file} is :")
            print(self.__data[file] + "\n")

    def append_file_ln(self, filename: str, content: str,
                       line=True) -> None:
        """Append content to the end of a file.

        The content is written to the file and synchronized with
        the in-memory archive. A newline can be optionally added
        before the appended content.

        Args:
            filename (str): Name of the file to update.
            content (str): Content to append to the file.
            line (bool, optional): To prepend a newline
                before the content. Defaults to True.

        Handled Exceptions:
            OSError: Raised if the file cannot be opened or written to.
        """
        f = None
        file = Archive.clean(filename)
        try:
            if line:
                ln = "\n"
            else:
                ln = ''
            f = open(filename, 'a', encoding="utf-8")
            f.write(content + "\n")
            if file in self.__data.keys():
                self.__data[file] += ln + content
            else:
                self.__data[file] = ln + content
        except OSError as e:
            print(f"Erreur avec {e}")
        finally:
            if f:
                f.close()

    def write_new_archive(self, filename: str, content: str) -> None:
        """Create a new archive file and write its initial content.

        If the file already exists, no writing is performed.
        The content is written to disk and stored in memory.

        Args:
            filename (str): Name of the file to create.
            content (str): Initial content of the file.

        Handled Exceptions:
            OSError: Raised if the file cannot be created or written.
        """
        f = None
        file = Archive.clean(filename)
        try:
            f = open(filename, 'r')
            f.close()
            print(f"{filename} already exist")
            return
        except OSError:
            print(f"{filename} file ready to be created")
        try:
            f = open(filename, 'w', encoding="utf-8")
            f.write(content + "\n")
            self.__data[file] = content
        except OSError as e:
            print(f"Erreur avec {e}")
        finally:
            if f:
                f.close()


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    archive = Archive("Demio")
    data = "[ENTRY 001] New quantum algorithm discovered\n"
    data += "[ENTRY 002] Efficiency increased by 347%\n"
    data += "[ENTRY 003] Archived by Data Archivist trainee"
    archive.write_new_archive('new_discovery.txt', data)
    archive.display_one_archive("new_discovery.txt")
    print("Data inscription complete. Storage unit sealed.")
    print("Archive 'new_discovery.txt' ready for long-term preservation.")
