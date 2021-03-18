import uuid
import dataclasses


@dataclasses.dataclass
class Entity:
    dni: int
    name: str
    price: float

    @classmethod
    def from_dict(self,d):
        return self(**d)

    def to_dict(self):
        return  dataclasses.asdict(self)


pass
