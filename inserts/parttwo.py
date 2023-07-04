from datetime import date

from session import Base, Session, engine

from tables.conversations import Conversation
from tables.personas import Persona
from tables.tags import Tag
from tables.users import User
from tables.topics import Topic
from tables.upvotes import Upvote

from conversations import stacey_fields, marlow_hines, katey_turnip, color_reality, plant_emotions, relationship_necessity
from conversations import colors_tag, plants_tag, reality_tag, emotions_tag, relationships_tag, necessities_tag
# generate database schema
Base.metadata.create_all(engine)


# create a new session
# session = Session()


# create personas
matt_persona = Persona(
    "Matt", 
    "https://imageLinkToS3Bucket.com",
    "Person who belives colors are real",
    True,
    date(2002, 10, 11),
    stacey_fields.id
)


tommy_persona = Persona(
    "Tommy", 
    "https://imageLinkToS3Bucket.com",
    "Person who belives colors are not real",
    False,
    date(2002, 10, 11),
    stacey_fields.id
)


egan_persona = Persona(
    "Matt", 
    "https://imageLinkToS3Bucket.com",
    "Person who belives plants can feel",
    True,
    date(2002, 10, 11),
    marlow_hines.id
)


yadi_persona = Persona(
    "Tommy", 
    "https://imageLinkToS3Bucket.com",
    "Person who belives plants cannot feel",
    False,
    date(2002, 10, 11),
    marlow_hines.id
)


remi_persona = Persona(
    "Matt", 
    "https://imageLinkToS3Bucket.com",
    "Person who belives relationships are important",
    True,
    date(2002, 10, 11),
    katey_turnip.id
)


haley_persona = Persona(
    "Tommy", 
    "https://imageLinkToS3Bucket.com",
    "Person who belives relationships are not important",
    False,
    date(2002, 10, 11),
    katey_turnip.id
)



# create conversations

colors = Conversation(
    "https://LinkToS3Bucket.com", 
    "Are Colors Real?",
    True,
    date(2002, 10, 11),
    stacey_fields.id,
    color_reality.id
)


plants = Conversation(
    "https://LinkToS3Bucket.com", 
    "Do plants feel?",
    False,
    date(2022, 11, 11),
    marlow_hines.id,
    plant_emotions.id
)


relationships = Conversation(
    "https://LinkToS3Bucket.com", 
    "Do humans really need relationships?",
    True,
    date(2021, 1, 10),
    katey_turnip.id,
    relationship_necessity.id
)



# create upvotes 
upvote_a = Upvote(
    marlow_hines.id,
    relationships.id,
    yadi_persona.id,
    date(2002, 10, 11)
)


upvote_b = Upvote(
    katey_turnip.id,
    colors.id,
    remi_persona.id,
    date(2002, 10, 11)
)


upvote_c = Upvote(
    stacey_fields.id,
    plants.id,
    haley_persona.id,
    date(2002, 10, 11)
)


# persists data
# session.add(matt_persona)
# session.add(tommy_persona)
# session.add(egan_persona)
# session.add(yadi_persona)
# session.add(remi_persona)
# session.add(haley_persona)


# session.add(colors)
# session.add(plants)
# session.add(relationships)


# session.add(upvote_a)
# session.add(upvote_b)
# session.add(upvote_c)


# add values to conversation_persona table mapping
colors.followingPersona.append(matt_persona)
colors.followingPersona.append(tommy_persona)


plants.followingPersona.append(egan_persona)
plants.followingPersona.append(yadi_persona)


relationships.followingPersona.append(remi_persona)
relationships.followingPersona.append(haley_persona)


# add values to conversation_tags table mapping
colors.followingTag.append(colors_tag)
plants.followingTag.append(emotions_tag)
relationships.followingTag.append(relationships_tag)



# commit and close session
# session.commit()
# session.close()