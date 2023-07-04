# from datetime import date

# from session import Base, Session, engine
# from tables.personas import Persona
# from tables.conversations import Conversation
# # from tables.upvotes import Upvote
# from users import stacey_fields
# from users import marlow_hines
# from users import katey_turnip

# # generate database schema
# Base.metadata.create_all(engine)

# # create a new session
# session = Session()


# # create personas
# matt_persona = Persona(
#     "Matt", 
#     "https://imageLinkToS3Bucket.com",
#     "Person who belives colors are real",
#     True,
#     date(2002, 10, 11),
#     stacey_fields.id
# )

# tommy_persona = Persona(
#     "Tommy", 
#     "https://imageLinkToS3Bucket.com",
#     "Person who belives colors are not real",
#     False,
#     date(2002, 10, 11),
#     stacey_fields.id
# )

# egan_persona = Persona(
#     "Matt", 
#     "https://imageLinkToS3Bucket.com",
#     "Person who belives plants can feel",
#     True,
#     date(2002, 10, 11),
#     marlow_hines.id
# )

# yadi_persona = Persona(
#     "Tommy", 
#     "https://imageLinkToS3Bucket.com",
#     "Person who belives plants cannot feel",
#     False,
#     date(2002, 10, 11),
#     marlow_hines.id
# )

# remi_persona = Persona(
#     "Matt", 
#     "https://imageLinkToS3Bucket.com",
#     "Person who belives relationships are important",
#     True,
#     date(2002, 10, 11),
#     katey_turnip.id
# )

# haley_persona = Persona(
#     "Tommy", 
#     "https://imageLinkToS3Bucket.com",
#     "Person who belives relationships are not important",
#     False,
#     date(2002, 10, 11),
#     katey_turnip.id
# )


# # persists data
# session.add(matt_persona)
# session.add(tommy_persona)
# session.add(egan_persona)
# session.add(yadi_persona)
# session.add(remi_persona)
# session.add(haley_persona)

# # commit and close session
# session.commit()
# # session.close()