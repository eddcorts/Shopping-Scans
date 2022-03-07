import aiohttp
import asyncio
import bs4

from .app.entity.Emitente import Emitente
from pydantic import parse_obj_as

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get(
            'https://ww1.receita.fazenda.df.gov.br/DecVisualizador/NfceCompleta/53211110258299000132650100001111211246275330?token=4d53bce03ec34c0a911182d4c228ee6c:r3E3kclgvp8WxC+xRFSe9g4mpbBaEuQuZP65Y4ENpk0=:85dca4f9f8b947e5a7c44933404f9b54:1644106751'
        ) as page:
            content = await page.text()
            soup = bs4.BeautifulSoup(content, 'html.parser')
            emitente_element = soup.select_one('div#abaEmitente div.card-body')
            emitente_data = {}

            for data_field in emitente_element.select('div.col'):
                data_name, data_value = (data.get_text(strip=True) for data in data_field.select('div'))
                data_name = data_name.lower()
                data_value = " ".join(data_value.split())

                field_name = (
                    'social_name' if 'social' in data_name else
                     'fantasy_name' if 'fantasia' in data_name else
                    'cnpj' if 'cnpj' == data_name else
                    'address' if 'endereço' == data_name else
                    'neighborhood' if 'bairro' in data_name else
                    'cep' if 'cep' == data_name else
                    'city' if 'município' == data_name else
                    'phone' if 'telefone' == data_name else
                    'uf' if 'uf' == data_name else
                    'country' if 'país' == data_name else
                    'state_registry' if 'inscrição estadual' == data_name else
                    'substitutive_state_registry' if 'substituto' in data_name else
                    'city_registry' if 'municipal' in data_name else
                    'city_id_ICMS_generated' if 'icms' in data_name else
                    'fiscal_CNAE' if 'cnae' in data_name else
                    'tax_regime' if 'regime' in data_name else None
                )

                if field_name:
                    emitente_data[field_name] = data_value

            x = parse_obj_as(Emitente, emitente_data)
            print(x)

if __name__ == '__main__':
    asyncio.run(main())
