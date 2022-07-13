from pydantic import BaseModel

class Settings(BaseModel):
    birthDate: str
    firstName: str
    middleName: str
    lastName: str
    passport: str
    id: str
    inn: str
    snils: str
    oms: str
    type: str

external_data = {
    "birthDate": "1984-01-09",
    "firstName": "Иванов",
     "id": 79262111317,
    "inn": "xxxxxxx",
    "lastName": "Иванов",
    "middleName": "Иванович",
    "oms": None,
    "passport": "xxxx xxxxxx",
    "snils": None,
    "type": "FULL"
}

settings = Settings(**external_data)
print(settings.id)