# RUN ACS

## Tools required to RUN ACS
- [Python](https://www.python.org/downloads/)
- [MySQL Workbench](https://dev.mysql.com/downloads/workbench/). NOTE: Make note of the password you enter whilst setting up the MySQL.
- [VScode](https://code.visualstudio.com/)
- [Node JS](https://nodejs.org/en)
- [Tutorial on how to install React.JS](https://www.freecodecamp.org/news/install-react-with-create-react-app/) Thank you Freecodecamp.org

## Load the project 
- Load the [acs](/ACS\acs) project on VScode. 


## Configuring Database connection
1. Open the MySQL workbench.
2. Create new schema and name is acsdb.

![](/ACS/Images/createdb.png)


3. Open VScode and then in acs folder select backend folder.
4. Open _ _ init.py _ _ file. (Now we will tell acs that use the SQL schema we just created)
5. Locate the following line of code:

```
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/'
```

6. You will need to add password that you input whilst setting up SQL and also the name of schema you just created.

![](/ACS/Images/dbconfig.png)

7. Save the file and now the MySQL schema is linked with the backend

## Running Back-end
1. Locate and open the run.py file. 
2. Right Click on the opened file. 
3. Select the option of _Run Python_ then select the option of  _Run Python file in terminal_.
4. VScode's terminal window will pop up with the message showed in the imaage below:

![](/ACS/Images/BackEndRunning.png)

5. Now the backend is up and runing and time to run frontend. 


## Running Front-end
1. You will need to ppen a new terminal in VScode and you can open it by:

![](/ACS/Images/OpenAnotherTerminal.png)

2. In the new terminal, at first you will need to change to Frontend folder and you can do by using _cd_ command. 
3. Then use command _npm start_ to run the frontend and it wil look something like this:

![](/ACS/Images/RunFrontEnd.png)

4. At last your default browser window will pop up and you can now use ACS.

![](/ACS/Images/popup.png)
