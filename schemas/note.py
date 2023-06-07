def note_entity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": item["title"],
        "desc": item["desc"],
        "important": item["important"]
    }


def notes_entity(items) -> list:
    return [notes_entity(item) for item in items]