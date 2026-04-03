import sys

if __name__ == "__main__":

    temp_err = sys.stderr
    err_file = None
    resp = ""
    f = None

    sys.stderr.write("Where would you like to archive the next data ?\n")
    record = sys.stdin.readline()
    out_file = None
    temp_out = sys.stdout

    try:
        out_file = open(record, 'a')
        sys.stdout = out_file
        print("Input channel test is successful !!!")
    except OSError as error:
        print(error, file=sys.stderr)
    finally:
        sys.stdout = temp_out
        if out_file:
            out_file.close()

    try:
        f = open("unknown.txt", 'r')
        f.close()
    except OSError as error:
        print("[ALERT] ", error, file=sys.stderr)

    try:
        print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")
        id = input("Input Stream active. Enter archivist ID:\t")
        report = input("Input Stream active. Enter status report:")
        f = open(id, 'a')
        f.writelines(report)
        f.close()
        f = open(id, 'r')
        sys.stdin = f
        print(f"[STANDARD] Archive status from {id}: {input()}",
              file=sys.stdout)
        print("[ALERT] System diagnostic: Communication channels verified",
              file=sys.stderr)
        print("[STANDARD] Data transmission complete")
    except (OSError, Exception) as e:
        print(e, file=sys.stderr)
    finally:
        if f is not None:
            f.close()
    print("\nThree-channel communication test successful.\n")
