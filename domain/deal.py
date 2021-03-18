import dataclasses


@dataclasses.dataclass
class Deal:

    id: int
    name: str
    stage: str
    close_date: str
    amount: float
    deal_type: str

    @classmethod
    def from_dict(self,dict):
        return self(**dict)

    def to_dict(self):
        return dataclasses.asdict(self)


pass
