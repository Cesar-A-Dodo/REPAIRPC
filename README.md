# REPAIRPC - Sistema Web de Gerenciamento de Reparos

![Django](https://img.shields.io/badge/Django-4.2%2B-green.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-purple.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

Sistema web completo para gerenciamento de assistência técnica de computadores, desenvolvido em Django com interface moderna e responsiva.

## ✨ Funcionalidades Principais

- **Gestão Completa de Clientes**: Cadastro, edição e consulta de clientes
- **Controle de Equipamentos**: Registro de máquinas e computadores com detalhes técnicos
- **Sistema de Ordens de Serviço**: Criação e acompanhamento de reparos
- **Dashboard Interativo**: Visualização de métricas e status de serviços
- **Busca Avançada**: Filtros para clientes, máquinas e ordens de serviço
- **Interface Responsiva**: Compatível com desktop, tablet e mobile

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 4.2+, Django REST Framework, Python
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5.x
- **Banco de Dados**: SQLite (desenvolvimento) / PostgreSQL (produção)
- **Controle de Versão**: Git

## 📦 Instalação Rápida

```bash
# Clone o repositório
git clone https://github.com/Cesar-A-Dodo/REPAIRPC.git
cd REPAIRPC

# Crie e ative o ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt

# Execute migrações e inicie o servidor
python manage.py migrate
python manage.py runserver
```

Acesse: http://localhost:8000

## 👨‍💻 Autor

**Cesar Augusto Dodo**  
📧 cesaraugustododo@gmail.com  
🔗 [GitHub](https://github.com/Cesar-A-Dodo)
🔗 [LinkedIn](https://www.linkedin.com/in/cesaraugustododo/)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

**Status**: Em desenvolvimento ativo  
**Versão**: 1.0.0