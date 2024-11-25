from flask import Flask
from db import db, init_app
from flask_migrate import Migrate
from controller.funcionario_controller import funcionario_bp
from controller.consulta_controller import consulta_bp
from controller.paciente_controller import paciente_bp
from controller.veterinario_controller import veterinario_bp
from controller.cliente_controller import cliente_bp
from controller.exame_controller import exame_bp
from controller.administrador_controller import administrador_bp
from controller.agenda_controller import agenda_bp
from controller.auxiliar_veterinario_controller import auxiliar_veterinario_bp
from controller.cirurgia_controller import cirurgia_bp
from controller.financeiro_controller import financeiro_bp
from controller.internamento_controller import internamento_bp
from controller.medicamento_controller import medicamento_bp
from controller.prescricao_controller import prescricao_bp


app = Flask(__name__)

# Configurações do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/anim_clin22'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrigido para evitar warnings

# Inicializar banco de dados e migrações
init_app(app)
migrate = Migrate(app, db)

# Registrar os Blueprints
app.register_blueprint(funcionario_bp, url_prefix='/api/v1/funcionarios')  # Rotas para funcionários
app.register_blueprint(consulta_bp, url_prefix='/api/v1/consultas')        # Rotas para consultas
app.register_blueprint(veterinario_bp, url_prefix='/api/v1/veterinarios')  # Rotas para veterinários
app.register_blueprint(paciente_bp, url_prefix='/api/v1/pacientes')        # Rotas para pacientes
app.register_blueprint(cliente_bp, url_prefix='/api/v1/clientes')
app.register_blueprint(exame_bp, url_prefix='/api/v1/exames')          # Rotas para clientes
app.register_blueprint(administrador_bp, url_prefix='/api/v1/administradores')
app.register_blueprint(agenda_bp, url_prefix='/api/v1/agendas')
app.register_blueprint(auxiliar_veterinario_bp, url_prefix='/api/v1/auxiliar_veterinarios')
app.register_blueprint(cirurgia_bp, url_prefix='/api/v1/cirurgias')
app.register_blueprint(financeiro_bp, url_prefix='/api/v1/finaceiros')
app.register_blueprint(internamento_bp, url_prefix='/api/v1/internamentos')
app.register_blueprint(medicamento_bp, url_prefix='/api/v1/medicamentos')
app.register_blueprint(prescricao_bp, url_prefix='/api/v1/prescricaos')


if __name__ == "__main__":
    app.run(debug=True)
