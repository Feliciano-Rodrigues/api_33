from flask import Blueprint, request, jsonify
from service.funcionario_service import FuncionarioService

funcionario_bp = Blueprint('funcionario', __name__)

@funcionario_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')

    if not email or not senha:
        return jsonify({"message": "Email e senha são obrigatórios"}), 400

    funcionario = FuncionarioService.login(email, senha)
    if funcionario:
        token = FuncionarioService.gerar_token(funcionario)
        return jsonify({"message": "Login bem-sucedido", "id": funcionario.id, "nome": funcionario.nome, "token": token}), 200
    return jsonify({"message": "Email ou senha inválidos"}), 400

@funcionario_bp.route('/criar', methods=['POST'])
def adicionar():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    cargo = data.get('cargo')

    if not nome or not email or not senha or not cargo:
        return jsonify({"message": "Todos os campos são obrigatórios"}), 400

    funcionario = FuncionarioService.adicionar(nome, email, senha, cargo)
    return jsonify({"message": "Funcionario adicionado", "id": funcionario.id}), 201


@funcionario_bp.route('/funcionario/<int:id>', methods=['PUT'])
def atualizar_funcionario(id):
    # Obtenha os dados enviados na requisição (geralmente JSON)
    dados = request.get_json()
    nome = dados.get('nome')
    email = dados.get('email')
    senha = dados.get('senha')
    cargo = dados.get('cargo')

    # Chame o método de serviço para atualizar os dados
    funcionario = FuncionarioService.atualizar(id, nome, email, senha, cargo)
    
    if funcionario:
        return jsonify({"message": "Funcionário atualizado com sucesso", "id": funcionario.id}), 200
    else:
        return jsonify({"message": "Funcionário não encontrado"}), 404



@funcionario_bp.route('/recuperar-senha', methods=['POST'])
def recuperar_senha():
    data = request.get_json()
    email = data.get('email')

    if not email:
        return jsonify({"message": "Email é obrigatório"}), 400

    funcionario = FuncionarioService.buscar_por_email(email)
    if funcionario:
        token = FuncionarioService.gerar_token_recuperacao(funcionario)
        return jsonify({"message": "Token de recuperação enviado", "token": token}), 200
    return jsonify({"message": "Email não encontrado"}), 400



@funcionario_bp.route('/atualizar-senha', methods=['POST'])
def atualizar_senha():
    data = request.get_json()
    token = data.get('token')
    nova_senha = data.get('nova_senha')

    if not token or not nova_senha:
        return jsonify({"message": "Token e nova senha são obrigatórios"}), 400

    funcionario = FuncionarioService.recuperar_senha(token, nova_senha)
    if funcionario:
        return jsonify({"message": "Senha atualizada com sucesso"}), 200
    return jsonify({"message": "Token inválido ou expirado"}), 400

@funcionario_bp.route('/funcionarios', methods=['GET'])
def listar_funcionarios():
    funcionarios = FuncionarioService.listar_todos()
    return jsonify(funcionarios)

@funcionario_bp.route('/funcionario/<int:id>', methods=['GET'])
def buscar_funcionario(id):
    funcionario = FuncionarioService.buscar_por_id(id)  # Usando o novo método
    if funcionario:
        return jsonify(funcionario.to_dict())  # Usando o método to_dict para a resposta JSON
    return jsonify({"message": "Funcionario não encontrado"}), 404

@funcionario_bp.route('/excluir/<int:funcionario_id>', methods=['DELETE'])
def excluir(funcionario_id):
    sucesso = FuncionarioService.excluir(funcionario_id)
    if sucesso: return jsonify({"message": "Funcionario excluído"}), 200
    return jsonify({"message": "Funcionario não encontrado"}), 404