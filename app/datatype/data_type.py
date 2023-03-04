from dataclasses import dataclass, field

@dataclass
class IDstore:
    id: str
    name: str
    description: str = ""