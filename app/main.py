class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        name = person.get("name")
        age = person.get("age")
        if name is None or age is None:
            continue
        new_person = Person(name, age)
        result.append(new_person)

    for person_dict in people:
        name = person_dict.get("name")
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        current_person = Person.people.get(name)
        if current_person is None:
            continue

        if wife_name:
            current_person.wife = Person.people.get(wife_name)
        if husband_name:
            current_person.husband = Person.people.get(husband_name)

    return result
