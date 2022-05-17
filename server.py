import socket
import threading
import datetime
import sqlite3


def create_db():
    con = sqlite3.connect('sqlite3_database.db')
    cur = con.cursor()
    # query to create table in the database
    cur.execute('''CREATE TABLE IF NOT EXISTS SERVER   
            (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            MESSAGE TEXT NOT NULL,
            DATE TIMESTAMP NOT NULL);''')
    cur.close()
    con.close()

def insert_values(message,time):
    con = sqlite3.connect('sqlite3_database.db')
    cur = con.cursor()
    qry = ('''INSERT INTO SERVER ('MESSAGE','DATE') VALUES (?, ?);''')
    cur.execute(qry,(message,time) )
    con.commit()
    cur.close()
    con.close()

myHostName = socket.gethostname()
IP = socket.gethostbyname(socket.gethostname())
print("Name of the localhost is {}".format(myHostName))
PORT = 12345
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        if msg == DISCONNECT_MSG:
            connected = False

        print(f"[{addr}] {msg}")
        time = datetime.datetime.now()
        insert_values(msg,str(time))
        msg = f"Msg received: {msg} + {str(time)}"
        conn.send(msg.encode(FORMAT))

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")
   

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    create_db()
    main()
    unittest.main(argv=['', '-v'])
