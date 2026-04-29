class Patient:
    def __init__(self, name: str, age: int, severity: int):
        self.name = name
        self.age = age
        self.severity = severity

    def __repr__(self) -> str:
        return f"Patient(name={self.name!r}, age={self.age}, severity={self.severity})"


class Hospital:
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.occupied_beds = 0

    def has_space(self) -> bool:
        return self.occupied_beds < self.capacity

    def allocate_bed(self) -> bool:
        if self.has_space():
            self.occupied_beds += 1
            return True
        return False

    def discharge(self) -> bool:
        if self.occupied_beds > 0:
            self.occupied_beds -= 1
            return True
        return False

    def __repr__(self) -> str:
        return (
            f"Hospital(name={self.name!r}, capacity={self.capacity}, "
            f"occupied_beds={self.occupied_beds})"
        )
