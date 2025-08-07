from graphviz import Digraph

# Criação do objeto Digraph
fluxo = Digraph(
    name='Projeto Mini ERP',
    format='png',
    graph_attr={'rankdir': 'TB', 'bgcolor': 'white'},
    node_attr={'style': 'filled', 'fontname': 'Arial', 'fontsize': '10'},
    edge_attr={'color': 'black'}
)

# Etapas do projeto com cores
etapas = {
    'A': {
        'titulo': 'Análise de Requisitos',
        'cor': 'lightblue',
        'descricao': 'Criação de documentos, mini-mundos e modelos externos.\n\nA primeira etapa do projeto de banco de dados é a identificação dos requisitos que o banco de dados deve atender.'
    },
    'B': {
        'titulo': 'Projeto Conceitual',
        'cor': 'lightgreen',
        'descricao': 'Criação do modelo conceitual com base na análise.\n\nBaseia na especificação de requisitos criada na etapa anterior. A partir deste insumo de informações é gerado um esquema conceitual do banco de dados, difiniçao dos modelos de Entidade-Relacionamento.'
    },
    'C': {
        'titulo': 'Projeto Lógico',
        'cor': 'yellowgreen',
        'descricao': 'Criação do modelo interno.\n\nMapeamos o conceito dos modelos de entidade relacionamento em Objetivos de banco de dados. Nesta fase criamos os modelos internos de bancos de dados. Detalhes sobre tabelas, relacionamentos, regras, tipos de dados etc.'
    },
    'D': {
        'titulo': 'Projeto Físico',
        'cor': 'gold',
        'descricao': 'Criação de scripts, modelos fisicos, estrategias de armazenamento e Backup.\n\nDefini-se detalhes da implementação do banco de dados, os scripts de criação dos objetos(tables, views, column etc) e as permissões.'
    }
}



# Adicionando os nós
for id, etapa in etapas.items():
    fluxo.node(id, f"{etapa['titulo']}\n\n{etapa['descricao']}", fillcolor=etapa['cor'], shape='box')

# Adicionando conexões
fluxo.edge('A', 'B')
fluxo.edge('B', 'C')
fluxo.edge('C', 'D')

# Renderizar e salvar o diagrama
fluxo.render(filename='projeto_mini_erp', cleanup=True, view=True)
