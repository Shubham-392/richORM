from richorm.db.models.fields.models import Field
from richorm.drivers.sqlite3.base import connections
from .utils import default_str


class BaseModel(type):
    """Metaclass for all models."""
    
    def __new__(cls, name:str, bases, attrs):
        default_db_table = name.lower() + "s"
        # Don't collect field info yet - just identify fields and check for duplicates
        non_duplicate_fields = set()
        
        field_attrs = {}
        
        primary_key_fields = []
        for key, value in attrs.items():
            if isinstance(value, Field):
                if key in non_duplicate_fields:
                    raise ValueError(
                        f"Duplicate field name '{key}' in model {name}"
                    )
                non_duplicate_fields.add(key)
                field_attrs[key] = value
                
                if getattr(value, 'primary_key', False):
                    primary_key_fields.append(key)
                    
        if len(primary_key_fields) > 1:
            primary_fields = {', '.join(primary_key_fields)}
            raise ValueError(
                f"Model '{name}' cannot have multiple primary key fields. "
                f"Found primary keys in fields:  {primary_fields}."
                f"Only one field can be marked as primary_key=True."
            )
            
        # default '__str__' to all Models
        if '__str__' not in attrs:
            attrs['__str__'] = default_str
        
        # Add basic meta info without field details
        attrs['_meta'] = {
            'table_name': default_db_table,
            'fields_info': [],
            'field_names':[]  
        }
        
        new_class = super().__new__(cls, name, bases, attrs)
        
        field_info = []
        fields_name = []
        for key, value in field_attrs.items():
            fields_name.append(key)
            field_meta_info = {
                "field_name": key,
                "field_value": value,
                "field_type": type(value).__name__ 
            }
            field_info.append(field_meta_info)
            
        new_class._meta['fields_info'] = field_info
        new_class._meta['field_names'] = fields_name
        return new_class
    
    
class Model(metaclass = BaseModel):
    
    def __init__(self, **kwargs):
        not_allowed_attrs = [key for key in kwargs.keys() if key not in self._meta['field_names']]
        if not_allowed_attrs:
            repr_attrs = ', '.join(not_allowed_attrs)
            raise ValueError(
                f'Unknown field(s): {repr_attrs}'
            )
        for key, value in kwargs.items():
            setattr(self, key, value)
            
            
    def save(self):
        table_name = self._meta['table_name']
        column_names = self._meta['field_names']
        for info in self._meta['fields_info']:
            field_name = info['field_name']
            field_type = info['field_type']
        cursor = connections.get_cursor()
        column_names = ', '.join(column_names)
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_names});"
        cursor.execute(create_table_query)
        
        
        
        
        