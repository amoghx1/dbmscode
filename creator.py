import sqlite3

conn = sqlite3.connect('asset.db')

# create cursor
c = conn.cursor()

# create tables
c.execute(""" CREATE TABLE Holder (
    HolderID varchar(255) UNIQUE,
    Holder_Password varchar(255),
    Holder_Email varchar(255),
    Holder_Name varchar(255),
    Holder_Type varchar(255),
    PRIMARY KEY (HolderID)

)""")

c.execute("""CREATE TABLE Asset (
    assetname varchar(255) UNIQUE,
    assettype varchar(255),
    heldby varchar(255),
    detail varchar(255),
    yoy varchar(255),
    value int,
    PRIMARY KEY (assetname)
    

)""")

c.execute("""CREATE TABLE TradeListing (
    title varchar(255),
    listedBy varchar(255),
    assetlisted varchar(255),
    email varchar(255),
    listername varchar(255),
    listprice float int
    
    
)


""")

c.execute("""CREATE TABLE AssetBehaviour (
    AssetID int,
    Total_Appreciation_Deprecation float(10),
    YoY_Change float(10),
    Liquidity varchar(255),
    PRIMARY KEY (AssetID),
    FOREIGN KEY (AssetID) REFERENCES Asset(AssetID)

)""")



conn.commit()
conn.close()

