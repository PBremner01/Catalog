from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from cdatabase_setup import Catalog, Base, CItem, User

engine = create_engine('sqlite:///catalogs.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Rogue Raider", email="bremnerphilip@gmail.com",
             picture='https://lh5.googleusercontent.com/-Q1gLMJ7xkPE/AAAAAAAAAAI/AAAAAAAAABs/SSXQ0koHV-E/photo.jpg')
session.add(User1)
session.commit()

# Catalog for soccer
catalog1 = Catalog(user_id=1, name="Soccer")

session.add(catalog1)
session.commit()

CItem2 = CItem(user_id=1, name="Ball", description="High perfomance playing ball ",
                       title="Soccer Ball", catalog=catalog1)

session.add(CItem2)
session.commit()


CItem1 = CItem(user_id=1, name="Cleats", description="Soccer Cleats",
                       title="Soccer Cleats", catalog=catalog1)

session.add(CItem1)
session.commit()

CItem2 = CItem(user_id=1, name="Club Shirt", description="Custom soccer club shirt",
                       title="Club Shirt", catalog=catalog1)

session.add(CItem2)
session.commit()

CItem3 = CItem(user_id=1, name="Goal", description="Collapsable soccer goal",
                       title="Soccer Goal", catalog=catalog1)

session.add(CItem3)
session.commit()


# Catalog for basketball
catalog2 = Catalog(user_id=1, name="Basketball")

session.add(catalog2)
session.commit()


CItem1 = CItem(user_id=1, name="Basketball ball", description="Long lasting high performance basketball",
                       title="Basketball ball", catalog=catalog2)

session.add(CItem1)
session.commit()

CItem2 = CItem(user_id=1, name="Shirt",
                     description=" Team shirt",   title="Team Shirt", catalog=catalog2)

session.add(CItem2)
session.commit()

CItem3 = CItem(user_id=1, name="Sneakers", description="High performance basketball sneakers ",
                       title="Sneakers", catalog=catalog2)

session.add(CItem3)
session.commit()

CItem4 = CItem(user_id=1, name="Mouth Guard ", description="Mouth guard protector. ",
                       title="Mouth guard", catalog=catalog2)

session.add(CItem4)
session.commit()


# Catalog for Snowboarding
catalog3 = Catalog(user_id=1, name="Snowboarding")

session.add(catalog3)
session.commit()


CItem1 = CItem(user_id=1, name="Snowboard", description="Long lasting high performance snowboard",
                       title="Snowboard", catalog=catalog3)

session.add(CItem1)
session.commit()

CItem2 = CItem(user_id=1, name="Ski Jacquet",
                     description="Snoboarding Jacquet",   title="Jacquet", catalog=catalog3)

session.add(CItem2)
session.commit()

CItem3 = CItem(user_id=1, name="Boots", description="High performance snowboarding boots ",
                       title="Boots", catalog=catalog3)

session.add(CItem3)
session.commit()

CItem4 = CItem(user_id=1, name="Helmet", description="Snowboarding helmet.",
                       title="Snowboarding Helmet", catalog=catalog3)

session.add(CItem4)
session.commit()


print "Added catalog items!"
