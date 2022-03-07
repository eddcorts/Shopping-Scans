from typing import Optional
from . import BaseModel

class Emitente(BaseModel, table=True):
    social_name: str
    fantasy_name: Optional[str]
    cnpj: str
    address: str
    neighborhood: str
    cep: str
    city: str
    phone: str
    uf: str
    country: str
    state_registry: str
    substitutive_state_registry: Optional[str]
    city_registry: Optional[str]
    city_id_ICMS_generated: int
    fiscal_CNAE: Optional[str]
    tax_regime: str
