from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///dados.db')
Base = declarative_base()
_Sesao = sessionmaker(engine)

class caes(Base):
    __tablename__ = 'caes'

    id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    raça = Column(String (150))
    sexo = Column (String(10))
    castrado = Column(String(3))
    aparencia = Column(String(150))
    obs = Column(String(150))

Base.metadata.create_all(engine)

with _Sesao () as sessao:
    caes = caes(nome = 'Amarelo', raça = 'SRD', sexo= 'Macho', castrado = 'não', aparencia = 'caramelo, peludo como um pastor alemão, grande porte', obs = 'não violenta')
    sessao.add(caes)
    sessao.commit()