#Oliver Fays Telnet Server

This is a simple server that one can connect to via telnet and run some commands

##Getting started

Pull the files into a local reposetory and open up a terminal in the same reposetory and run the command:

```bash
python server.py
```

##connecting to server

The server will run on port 5005 or whatever port you specify in server.py to connect run the command:

```bash
telnet 127.0.0.1 5005
```

to disconnect:

```bash
^]
close
```

##how to use

The server can handle certain specified comands such as variable assignment, math expressions, and more.

- author
- hello
- help
- x = 123
- 5 + 5

##testing

Run the executable file on the device you're using to connect to test full array of commands
The .expect script runs very slow but it will get there
I attepted using a .sh script but .expect is designed for telnet

```bash
./test.expect
```