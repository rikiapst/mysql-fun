# from datetime import date

# from session import Base, Session, engine
# from tables.topics import Topic
# from tables.conversations import Conversation
# from tables.personas import Persona
# from tables.tags import Tag
# from tables.users import User
# # from tables.upvotes import Upvote


# Base.metadata.create_all(engine)

# # session = Session()


# # Topics
# color_reality = Topic(
#     "Color Reality",
#     "Debate about colors",
#     date(2002, 10, 11)
# )


# plant_emotions = Topic(
#     "Plant Emotions",
#     "Deabte about plant",
#     date(2022, 11, 11)
# )


# relationship_necessity = Topic(
#     "Relationship necessity",
#     "Debate about humans and relationships?",
#     date(2021, 1, 10)
# )


# # # persists data
# # session.add(color_reality)
# # session.add(plant_emotions)
# # session.add(relationship_necessity)

# # # commit and close session
# # session.commit()
# # session.close()