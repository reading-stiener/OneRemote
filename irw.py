import sys
import lirc
if len(sys.argv) >= 3:
    sys.stderr.write("Usage: isrw.py [socket path]")
    sys.exit(1)
path = sys.argv[1] if len(sys.argv) == 2 else None
with lirc.RawConnection(path) as conn:
    while True:
        print(conn.readline())