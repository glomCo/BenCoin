BenCoin
=======

Bitcoin is silly. Litecoin makes me laugh. Namecoin makes me fall to the ground. Bencoin makes me giggle. Bencoin is a centralized currency that you can use with your friends. It works by holding the user’s amount of bencoin in a ftp server. 


If bencoin is centralized why do you have mining?
I could not think of a better way the users could earn bencoin (without trade) so I created a silly thing of mining. Bencoin mining is essentially a random number generator comparing its output to another number. Once it's done mining the user is rewarded with a single bencoin!

Setup:
To setup bencoin copy and paste the source into a preferred directory, save it with a .py(python) extension and open it in a text editor. On line 36 enter your ftp server’s password and such.  Now log onto your ftp server and create a directory called "Bencoin" now go inside the new directory. To setup a new account for your users you must create two new files: thenewguyspassword.key and thenewguyspassword.dat . In thenewguyspassword.dat enter the amount of bencoin the user has. In thenewguyspassword.key enter the user’s key. If you do not want your users to know your ftp password you can use py2exe or something of such.
