# from datetime import date

# from session import Base, Session, engine

# from tables.users import User
# from tables.conversations import Conversation
# from tables.personas import Persona
# from tables.upvotes import Upvote
# from tables.tags import Tag


# # generate database schema
# Base.metadata.create_all(engine)

# # # create a new session
# session = Session()

# # creates users

# stacey_fields = User(
#     "staceTheAce", 
#     "Stacey", 
#     "Fields", 
#     "stac.fields@dummy.com", 
#     date(2022, 10, 8)
# )


# marlow_hines = User(
#     "handm", 
#     "Marlow", 
#     "Hines", 
#     "mars@dummy.com", 
#     date(2021, 5, 8)
# )


# katey_turnip = User(
#     "turnipsauce",
#     "Katey",
#     "Turnip",
#     "letsturnip@dummy.com",
#     date(2023, 1, 1)
# )


# # # persists data
# session.add(stacey_fields)
# session.add(marlow_hines)
# session.add(katey_turnip)


# # # commit and close session
# session.commit()
# # session.close()
