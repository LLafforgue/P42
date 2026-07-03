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

    def add_archi(self, arg: str) -> None:
        """Load a text file into the archive.

        If no file name is provided, a default file is used.
        The file content is read and stored in memory.

        Args:
            arg (str): Path or name of the file to archive.

        Handled Exceptions:
            OSError: Raised if the file cannot be opened or read.
        """
        print(f"\nAccessing Storage Vault: {arg}")
        try:
            if arg is None:
                raise ValueError("RESPONSE: Unexpected system"
                                 + "anomaly detected")
            file = Archive.clean(arg)
            with open(arg, 'r') as f:
                if not f.closed:
                    print("---Access connection---")
                self.__data[file] = f.read()
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except ValueError as e:
            print(e)
            print("STATUS: Crisis contained, system stabilized")

    def display_archi(self, arch_name: str) -> None:
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
            print(f"Content of {arch_name} is :")
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
        try:
            if filename is None or content is None:
                raise ValueError("RESPONSE: Unexpected system"
                                 + "anomaly detected")
            if line:
                ln = "\n"
            else:
                ln = ''
            file = Archive.clean(filename)
            with open(filename, 'a', encoding="utf-8") as f:
                if not f.closed:
                    print("---Append connection---")
                f.write(content + "\n")
                if file in self.__data.keys():
                    self.__data[file] += ln + content
                else:
                    self.__data[file] = ln + content

        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except ValueError as e:
            print(e)
            print("STATUS: Crisis contained, system stabilized")

    def write_new_archiv(self, filename: str, content: str) -> None:
        """Create a new archive file and write its initial content.

        If the file already exists, no writing is performed.
        The content is written to disk and stored in memory.

        Args:
            filename (str): Name of the file to create.
            content (str): Initial content of the file.

        Handled Exceptions:
            OSError: Raised if the file cannot be created or written.
        """
        try:
            with open(filename, 'r'):
                print(f"{filename} already exist")
            return
        except OSError:
            print(f"{filename} file ready to be created")
        try:
            file = Archive.clean(filename)
            if filename is None:
                raise ValueError("RESPONSE: Unexpected system"
                                 + "anomaly detected")
            with open(filename, 'w', encoding="utf-8") as f:
                print("---Connection to create---")
                f.write(content + "\n")
                self.__data[file] = content
        except FileNotFoundError:
            print("RESPONSE: Archive not found in storage matrix")
            print("STATUS: Crisis handled, system stable")
        except PermissionError:
            print("RESPONSE: Security protocols deny access")
            print("STATUS: Crisis handled, security maintained")
        except ValueError as e:
            print(e)
            print("STATUS: Crisis contained, system stabilized")


if __name__ == "__main__":
    archive = Archive("Crisis Response Vault")
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print("\nSECURE PRESERVATION:")
    archive.write_new_archiv("secure_data.txt", "Initial secure content.")
    archive.append_file_ln("secure_data.txt", "Secured data 1.")
    archive.append_file_ln("secure_data.txt", "Secured data 2.")
    print("\n")
    archive.display_archi("secure_data.txt")
    print("\nMISSING ARCHIVE:")
    archive.add_archi("missing_archive.txt")
    print("\nPERMISSION ERROR:")
    archive.add_archi("/root/forbidden_data.txt")
    archive.append_file_ln("/root/forbidden_data.txt", "test")
    print("\nUNEXPECTED ERROR:")
    archive.add_archi(None)
