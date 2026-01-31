class CustomerSchema:
    """Schema para validar dados de cliente"""
    
    @staticmethod
    def validate(data, is_update=False):
        errors = {}
        
        # Nome obrigatório apenas em criação
        if not is_update and not data.get('name'):
            errors['name'] = 'Nome é obrigatório'
        elif data.get('name') and len(data['name']) < 3:
            errors['name'] = 'Nome deve ter pelo menos 3 caracteres'
        
        # Telefone obrigatório apenas em criação
        if not is_update and not data.get('phone'):
            errors['phone'] = 'Telefone é obrigatório'
        
        # Validar email se fornecido
        if data.get('email'):
            if '@' not in data['email']:
                errors['email'] = 'Email inválido'
        
        return errors