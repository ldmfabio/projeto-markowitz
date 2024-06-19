## Projeto Markowitz

Aplicação web para gerenciamento de carteiras de investimentos que, com base nas classes de ativos informadas pelo usuário, oferece a composição ótima. Essa composição busca o melhor equilíbrio entre risco e retorno, conforme os princípios da Teoria Moderna do Portfólio desenvolvida por Markowitz.

#### Funcionalidades Atuais
Autenticação de Usuário: Sistema seguro de login e registro para garantir que apenas usuários autorizados acessem suas carteiras.
Gestão de Carteiras: Ferramentas para criar, visualizar e gerenciar carteiras de investimentos personalizadas.
Criação da Fronteira Eficiente: Geração da fronteira eficiente baseada na carteira selecionada, permitindo ao usuário visualizar o equilíbrio ótimo entre risco e retorno.

#### Tecnologias Utilizadas
- Streamlit
- Echarts
  
#### Objetivos do Projeto
- Facilitar o gerenciamento de investimentos, oferecendo análises detalhadas e recomendações baseadas na Teoria Moderna do Portfólio.
- Proporcionar uma interface amigável e intuitiva para que investidores possam otimizar suas carteiras com facilidade.

____

#### Para Testar o Projeto
Siga os passos abaixo para clonar e executar o projeto localmente:

1. **Clone o repositório do GitHub:**

```bash
git clone https://github.com/seu-usuario/projeto-markowitz.git
```

2. Navegue até o diretório do projeto:

```bash
cd projeto-markowitz
```

3. Instale as dependências usando PDM:
Se ainda não tiver o PDM instalado, instale-o primeiro:

```bash
pip install pdm
```

4. Em seguida, instale as dependências do projeto:

```bash
pdm install
```

5. Execute a aplicação:
Use o comando abaixo para iniciar a aplicação com o Streamlit:

```bash
pdm run streamlit run app.py
```

6. Acesse a aplicação:
Abra o navegador e vá para a URL fornecida pelo Streamlit (geralmente http://localhost:8501).

#### Notas Adicionais
Certifique-se de que você tem o Python instalado (versão 3.8 ou superior é recomendada).
PDM é um moderno gerenciador de pacotes e ambientes para Python. Se preferir, você pode usar pip e um ambiente virtual (venv) em vez de PDM.
Verifique as permissões de firewall e proxy que possam afetar a execução local do Streamlit.
