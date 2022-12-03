import json


def load_candidates():
    with open('candidates.json', encoding='utf-8') as file:
        return json.load(file)


def get_all():
    list_of_candidates = load_candidates()
    return list_of_candidates



def get_by_pk(pk):
    for candidate in get_all():
        if candidate['pk'] == pk:
            return candidate




def get_by_skill(skill_name):
    candidates = []
    for candidate in get_all():
        if skill_name.lower() in candidate['skills'].lower().split(', '):
            candidates.append(candidate)

    return candidates
