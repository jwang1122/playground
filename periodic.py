# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = periodic_table_json_from_dict(json.loads(json_string))

from enum import Enum
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    if(x==None): return []
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Phase(Enum):
    GAS = "Gas"
    LIQUID = "Liquid"
    SOLID = "Solid"


class Element:
    name: str
    appearance: Optional[str]
    atomic_mass: float
    boil: Optional[float]
    category: str
    color: Optional[str]
    density: Optional[float]
    discovered_by: Optional[str]
    melt: Optional[float]
    molar_heat: Optional[float]
    named_by: Optional[str]
    number: int
    period: int
    phase: Phase
    source: str
    spectral_img: Optional[str]
    summary: str
    symbol: str
    xpos: int
    ypos: int
    shells: List[int]
    electron_configuration: str
    electron_affinity: Optional[float]
    electronegativity_pauling: Optional[float]
    ionization_energies: List[float]

    def __init__(self, name: str, appearance: Optional[str], atomic_mass: float, boil: Optional[float], category: str, color: Optional[str], density: Optional[float], discovered_by: Optional[str], melt: Optional[float], molar_heat: Optional[float], named_by: Optional[str], number: int, period: int, phase: Phase, source: str, spectral_img: Optional[str], summary: str, symbol: str, xpos: int, ypos: int, shells: List[int], electron_configuration: str, electron_affinity: Optional[float], electronegativity_pauling: Optional[float], ionization_energies: List[float]) -> None:
        self.name = name
        self.appearance = appearance
        self.atomic_mass = atomic_mass
        self.boil = boil
        self.category = category
        self.color = color
        self.density = density
        self.discovered_by = discovered_by
        self.melt = melt
        self.molar_heat = molar_heat
        self.named_by = named_by
        self.number = number
        self.period = period
        self.phase = phase
        self.source = source
        self.spectral_img = spectral_img
        self.summary = summary
        self.symbol = symbol
        self.xpos = xpos
        self.ypos = ypos
        self.shells = shells
        self.electron_configuration = electron_configuration
        self.electron_affinity = electron_affinity
        self.electronegativity_pauling = electronegativity_pauling
        self.ionization_energies = ionization_energies

    @staticmethod
    def from_dict(obj: Any) -> 'Element':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        appearance = from_union([from_none, from_str], obj.get("appearance"))
        atomic_mass = from_float(obj.get("atomic_mass"))
        boil = from_union([from_float, from_none], obj.get("boil"))
        category = from_str(obj.get("category"))
        color = from_union([from_none, from_str], obj.get("color"))
        density = from_union([from_float, from_none], obj.get("density"))
        discovered_by = from_union([from_none, from_str], obj.get("discovered_by"))
        melt = from_union([from_float, from_none], obj.get("melt"))
        molar_heat = from_union([from_float, from_none], obj.get("molar_heat"))
        named_by = from_union([from_none, from_str], obj.get("named_by"))
        number = from_int(obj.get("number"))
        period = from_int(obj.get("period"))
        phase = Phase(obj.get("phase"))
        source = from_str(obj.get("source"))
        spectral_img = from_union([from_none, from_str], obj.get("spectral_img"))
        summary = from_str(obj.get("summary"))
        symbol = from_str(obj.get("symbol"))
        xpos = from_int(obj.get("xpos"))
        ypos = from_int(obj.get("ypos"))
        shells = from_list(from_int, obj.get("shells"))
        electron_configuration = from_str(obj.get("electron_configuration"))
        electron_affinity = from_union([from_float, from_none], obj.get("electron_affinity"))
        electronegativity_pauling = from_union([from_float, from_none], obj.get("electronegativity_pauling"))
        ionization_energies = from_list(from_float, obj.get("ionization_energies"))
        return Element(name, appearance, atomic_mass, boil, category, color, density, discovered_by, melt, molar_heat, named_by, number, period, phase, source, spectral_img, summary, symbol, xpos, ypos, shells, electron_configuration, electron_affinity, electronegativity_pauling, ionization_energies)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["appearance"] = from_union([from_none, from_str], self.appearance)
        result["atomic_mass"] = to_float(self.atomic_mass)
        result["boil"] = from_union([to_float, from_none], self.boil)
        result["category"] = from_str(self.category)
        result["color"] = from_union([from_none, from_str], self.color)
        result["density"] = from_union([to_float, from_none], self.density)
        result["discovered_by"] = from_union([from_none, from_str], self.discovered_by)
        result["melt"] = from_union([to_float, from_none], self.melt)
        result["molar_heat"] = from_union([to_float, from_none], self.molar_heat)
        result["named_by"] = from_union([from_none, from_str], self.named_by)
        result["number"] = from_int(self.number)
        result["period"] = from_int(self.period)
        result["phase"] = to_enum(Phase, self.phase)
        result["source"] = from_str(self.source)
        result["spectral_img"] = from_union([from_none, from_str], self.spectral_img)
        result["summary"] = from_str(self.summary)
        result["symbol"] = from_str(self.symbol)
        result["xpos"] = from_int(self.xpos)
        result["ypos"] = from_int(self.ypos)
        result["shells"] = from_list(from_int, self.shells)
        result["electron_configuration"] = from_str(self.electron_configuration)
        result["electron_affinity"] = from_union([to_float, from_none], self.electron_affinity)
        result["electronegativity_pauling"] = from_union([to_float, from_none], self.electronegativity_pauling)
        result["ionization_energies"] = from_list(to_float, self.ionization_energies)
        return result


class PeriodicTableJSON:
    elements: List[Element]

    def __init__(self, elements: List[Element]) -> None:
        self.elements = elements

    @staticmethod
    def from_dict(obj: Any) -> 'PeriodicTableJSON':
        assert isinstance(obj, dict)
        elements = from_list(Element.from_dict, obj.get("elements"))
        return PeriodicTableJSON(elements)

    def to_dict(self) -> dict:
        result: dict = {}
        result["elements"] = from_list(lambda x: to_class(Element, x), self.elements)
        return result


def periodic_table_json_from_dict(s: Any) -> PeriodicTableJSON:
    return PeriodicTableJSON.from_dict(s)


def periodic_table_json_to_dict(x: PeriodicTableJSON) -> Any:
    return to_class(PeriodicTableJSON, x)
