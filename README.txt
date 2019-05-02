Arianne Arcebal: hharin@csu.fullerton.edu


Language: Python


Execution:
	First, run the server that wil listen to connections:
	$ python3 serv.py <PORT>

	Then, run the client that will connect to the server:
	$ python3 cli.py <SERVER MACHINE> <PORT>

	The client port number should match the server port number, else the conneciton will be refused.

	After the connection is established, the client prints "ftp>", allowing the user to execute the following commands:
	ftp> get <FILE NAME> :	downloads <FILE NAME> from the server
	ftp> put <FILE NAME> :	uploads <FILE NAME> from the client to the server
	ftp> ls		     :	lists fils on the server
	ftp> quit	     :	disconnects from the server and exits


Additional Notes:
	* client files are read from cliFiles
	* server files are read from servFiles
