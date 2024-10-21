from flask import Blueprint, request, jsonify
from models import db, Cliente

# instância(objeto) de Blueprint
cliente_bp = Blueprint('clientes', __name__)

# Decorator da rota produtos, que é do tipo POST (enviando dados)
@cliente_bp.route('/clientes', methods=['POST'])
def criar_cliente():
    
    cliente = request.json
    novo_cliente = Cliente(cliente_nome=cliente['cliente_nome'],
                           cliente_email=cliente['cliente_email'])
    db.session.add(novo_cliente)
    db.session.commit()
    
    return jsonify({'id': novo_cliente.cliente_id, 'nome': novo_cliente.cliente_nome, 'email': novo_cliente.cliente_email
                    }), 201

@cliente_bp.route('/clientes', methods=['GET'])
def listarClientes():
    clientes = Cliente.query.all()
    
    return jsonify([{'ID': c.cliente_id, 'Nome': c.cliente_nome} for c in clientes]), 200

# @cliente_bp.route('/produtos', methods=['GET'])
# def listar_produtos():
#     produtos = Produto.query.all()

#     return jsonify([{'ID': p.produto_id, 'Nome': p.produto_nome} for p in produtos]), 200 