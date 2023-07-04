from datetime import date

from session import Base, Session, engine

# from tables.users import User
# from tables.conversations import Conversation
# from tables.personas import Persona
# from tables.upvotes import Upvote

# from users import stacey_fields
# from users import marlow_hines
# from users import katey_turnip
# from personas import matt_persona
# from personas import tommy_persona
# from personas import egan_persona
# from personas import yadi_persona
# from personas import remi_persona
# from personas import haley_persona
# from conversations import colors
# from conversations import relationships
# from conversations import plants



# # generate database schema
# Base.metadata.create_all(engine)

# # # create a new session
# session = Session()


# # add upvotes 
# upvote_a = Upvote(
#     marlow_hines.id,
#     relationships.id,
#     yadi_persona.id,
#     date(2002, 10, 11)
# )

# upvote_b = Upvote(
#     katey_turnip.id,
#     colors.id,
#     remi_persona.id,
#     date(2002, 10, 11)
# )

# upvote_c = Upvote(
#     stacey_fields.id,
#     plants.id,
#     haley_persona.id,
#     date(2002, 10, 11)
# )

# # # persists data
# session.add(upvote_a)
# session.add(upvote_b)
# session.add(upvote_c)

# # # commit and close session
# session.commit()
# # session.close()