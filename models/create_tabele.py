from models.db import Base, ENGINE


def create_table():
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    create_table()
