# ETL Streamlit App

Uma aplicação web interativa desenvolvida com Streamlit para demonstrar processos de ETL (Extract, Transform, Load) e análise de dados usando o dataset de pinguins.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 📋 Sobre o Projeto

Este projeto é uma aplicação web educativa que demonstra conceitos fundamentais de engenharia de dados, incluindo:

- **Extração de dados** de arquivos CSV
- **Transformação** e limpeza de dados
- **Carregamento** e visualização interativa
- **Análise** de qualidade de dados

A aplicação utiliza um dataset de pinguins para demonstrar problemas comuns em dados reais, como valores faltantes, e como tratá-los adequadamente.

## 🚀 Funcionalidades

### 🏠 Página Inicial
- Apresentação do projeto
- Descrição das tecnologias utilizadas
- Links para redes sociais

### 📊 DataFrame Original
- Visualização dos dados brutos
- Tabela interativa com funcionalidades de filtro e ordenação
- Identificação de problemas nos dados

### 🔧 DataFrame Melhorado (Engenharia de Dados)
- Análise de dados com valores faltantes
- Demonstração do processo de limpeza
- Comparação entre dados brutos e limpos
- Código exemplo para limpeza de dados

### 📈 Análise de Dados
- Visualizações estatísticas
- Gráficos interativos
- Insights dos dados

## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** - Framework para criação de aplicações web
- **[Pandas](https://pandas.pydata.org/)** - Manipulação e análise de dados
- **[st-aggrid](https://github.com/PablocFonseca/streamlit-aggrid)** - Tabelas interativas avançadas
- **[Streamlit Extras](https://github.com/arnaudmiribel/streamlit-extras)** - Componentes adicionais
- **[Plotly](https://plotly.com/)** - Visualizações interativas
- **[Altair](https://altair-viz.github.io/)** - Visualizações estatísticas

## 📁 Estrutura do Projeto

```
etl_streamlit/
├── streamlit_app.py          # Arquivo principal da aplicação
├── requirements.txt          # Dependências do projeto
├── README.md                # Documentação do projeto
├── assets/                  # Recursos estáticos
│   └── logo_dark.png        # Logo da aplicação
├── components/              # Componentes da aplicação
│   └── router.py           # Configuração de navegação
├── data/                   # Datasets
│   └── penguins.csv        # Dataset de pinguins
├── utils/                  # Utilitários
│   └── data_utils.py       # Funções para manipulação de dados
└── views/                  # Páginas da aplicação
    ├── 0_homepage.py       # Página inicial
    ├── 1_dataframe.py      # Visualização de dados originais
    ├── 2_improved_dataframe.py  # Dados após limpeza
    └── 3_data_analysis.py  # Análise e visualizações
```

## 🔧 Instalação e Configuração

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passo a Passo

1. **Clone o repositório**
   ```bash
   git clone <url-do-repositorio>
   cd etl_streamlit
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute a aplicação**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Acesse a aplicação**
   
   Abra seu navegador e acesse: `http://localhost:8501`

## 📊 Dataset

O projeto utiliza o dataset de pinguins que contém informações sobre:

- **Culmen Length (mm)**: Comprimento do bico em milímetros
- **Culmen Depth (mm)**: Profundidade do bico em milímetros  
- **Flipper Length (mm)**: Comprimento da nadadeira em milímetros
- **Body Mass (g)**: Massa corporal em gramas
- **Sex**: Sexo do pinguim (MALE/FEMALE)

### Problemas nos Dados

O dataset contém intencionalmente problemas comuns:
- Valores faltantes (NA)
- Linhas com dados incompletos
- Inconsistências que precisam ser tratadas

## 🎯 Conceitos Demonstrados

### ETL (Extract, Transform, Load)

1. **Extract**: Leitura de dados do arquivo CSV
2. **Transform**: 
   - Renomeação de colunas
   - Limpeza de dados (remoção de valores faltantes)
   - Validação de dados
3. **Load**: Apresentação dos dados em tabelas interativas

### Engenharia de Dados

- Identificação de problemas de qualidade
- Estratégias de limpeza de dados
- Comparação entre dados brutos e processados
- Documentação do processo de transformação

## 🚀 Executando em Produção

Para deploy em produção, você pode usar:

- **Streamlit Cloud**: Deploy gratuito e fácil
- **Heroku**: Plataforma de nuvem
- **AWS/GCP/Azure**: Serviços de nuvem
- **Docker**: Containerização da aplicação

### Deploy no Streamlit Cloud

1. Faça push do código para GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório
4. Configure o arquivo principal como `streamlit_app.py`

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

- **Autor**: Victor Bitt
- **LinkedIn**: https://www.linkedin.com/in/vicourtbitt/
- **GitHub**: https://github.com/VicourtBitt

## 🙏 Agradecimentos

- Comunidade Streamlit pelos recursos e documentação
- Contribuidores de todas as bibliotecas utilizadas

---

⭐ Se este projeto foi útil para você, não esqueça de dar uma estrela!