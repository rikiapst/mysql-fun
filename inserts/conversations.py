from datetime import date

from session import Base, Session, engine

from tables.conversations import Conversation
from tables.personas import Persona
from tables.tags import Tag
from tables.users import User
from tables.topics import Topic
from tables.upvotes import Upvote


# generate database schema
Base.metadata.create_all(engine)


# create a new session
session = Session()

stacey_fields = User(
    "staceTheAce", 
    "Stacey", 
    "Fields", 
    "stac.fields@dummy.com", 
    date(2022, 10, 8)
)


marlow_hines = User(
    "handm", 
    "Marlow", 
    "Hines", 
    "mars@dummy.com", 
    date(2021, 5, 8)
)


katey_turnip = User(
    "turnipsauce",
    "Katey",
    "Turnip",
    "letsturnip@dummy.com",
    date(2023, 1, 1)
)

session.add(stacey_fields)
session.add(marlow_hines)
session.add(katey_turnip)

session.commit()

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

session.add(matt_persona)
session.add(tommy_persona)
session.add(egan_persona)
session.add(yadi_persona)
session.add(remi_persona)
session.add(haley_persona)

session.commit()



# create Topics
color_reality = Topic(
    "Color Reality",
    "Debate about colors",
    date(2002, 10, 11)
)


plant_emotions = Topic(
    "Plant Emotions",
    "Deabte about plant",
    date(2022, 11, 11)
)


relationship_necessity = Topic(
    "Relationship necessity",
    "Debate about humans and relationships?",
    date(2021, 1, 10)
)

session.add(color_reality)
session.add(plant_emotions)
session.add(relationship_necessity)

session.commit()


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

session.add(colors)
session.add(plants)
session.add(relationships)

session.commit()


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

session.add(upvote_a)
session.add(upvote_b)
session.add(upvote_c)

session.commit()


# Tags

colors_tag = Tag("Colors")

reality_tag = Tag("Reality")

emotions_tag = Tag("Emotions")

plants_tag = Tag("Plants")

necessities_tag = Tag("Necessities")

relationships_tag = Tag("Relationships")


session.add(colors_tag)
session.add(reality_tag)
session.add(emotions_tag)
session.add(plants_tag)
session.add(necessities_tag)
session.add(relationships_tag)

session.commit()

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
session.commit()
session.close()